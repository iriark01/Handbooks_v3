# Optimising application for throughput and power consumption

BLE (Bluetooth Low Energy) devices are usually battery powered so performance might mean different things in different
applications. You will need to decide what is more important in your application - minimising power consumption on one
or both sides of the communication or maximising throughput and/or latency. Some optimisation steps can in fact achieve
both.

This guide will discuss some trade-offs that should be considered and best practices that improve performance on all
fronts.

## Power consumption

Any radio activity will consume power. Depending on what the stack is doing you have to power the radio even when no
data is being sent. It is important to understand when radio is active.

### Connections

The most intuitive power consumption rate to understand is when using connections. Each device will take turns sending
and receiving at set interval.

```
    CENTRAL
    ┌────┐ ┌────┐           ┌────┐ ┌────┐         ┌────┐ ┌────┐ ┌────┐ ┌────┐
    │send│ │recv│           │send│ │recv│         │send│ │recv│ │send│ │recv│
    └────┘ └────┘           └────┘ └────┘         └────┘ └────┘ └────┘ └────┘
      connection interval
     ◄─────────────────────►

    PERIPHERAL
    ┌────┐ ┌────┐                                 ┌────┐ ┌────┐ ┌────┐ ┌────┐
    │recv│ │send│                                 │recv│ │send│ │recv│ │send│
    └────┘ └────┘                                 └────┘ └────┘ └────┘ └────┘
      slave latency
     ◄───────────────────────────────────────────►

    ▲                       ▲                     ▲
    connection event        connection event      connection event
```

To maintain a connection, regardless if there is data transfer to be transferred, the central needs to transmit and
receive once every connection interval.

The peripheral needs to acknowledge connection events to the central. Data ready to be transmitted is sent in the
acknowledgement. To save power, if the peripheral has no data to transmit it may skip up to `slaveLatency` connection
events.

More power is consumed if there is data to be exchanged. The exchange can continue until the next connection event would
take place.

It's worth considering if keeping the connection active is worth it. Connection in BLE has little overhead and there are
some cases when it is better to connect and disconnect each time you want to send a burst of data if for example you
want to conserve power on one of the devices. This way only one side will have to run advertising/scanning all the time
while the power limited device can turn the transmitter on only when it needs to.

The cost of the connection is proportionate to the negotiable connection interval. This can be set during `connect` or
later through `updateConnectionParameters`. The lower the interval the more often radio is active. This is especially
important for the peripheral which needs to enable the radio to receive packets.

This can be further helped by setting a high `slaveLatency` parameter. This allows the peripheral to skip
connection events and save power not just by not sending any packets but by not even listening. This is not free for
central as it increases latency of data transmission from central to peripheral. Central may have to attempt sending
data multiple times before the peripheral accepts the transmission. The peripheral may send data at any connection event
as the central must listen after every transmission.

### Advertising and scanning

Power draw during advertising affected by:
- the advertising interval - lower interval uses more power,
- use of Coded PHY which uses more power for extended effective range,
- amount of data sent,
- number of channels used - each advertising event is sent by default to three channels which you can limit to 2 or 1,
- whether extended advertising is used - this will send additional packets on regular channels,
- whether the type is connectable or scannable - it means the advertiser needs to listen on the radio after each
  advertisement for potential connection of scan requests.

```
               PERIPHERAL
                ┌────┐           advertising interval              ┌────┐
     channel 37 │adv │◄───────────────────────────────────────────►│adv │
                └────┘                                             └────┘
                      ┌────┐                                             ┌────┐
     channel 38       │adv │                                             │adv │
                      └────┘                                             └────┘
                            ┌────┐                                             ┌────┐
     channel 39             │adv │                                             │adv │
                            └────┘                                             └────┘

     non-advertising              ┌────────────────────┐
     channel                      │extended advertising│
     (indicated in regular        └────────────────────┘
      advertising payload)
```

Scanning power draw is proportional to time spent scanning. Additional power will be used if you run active scanning
which will send a scan request and listen for the reply.

The interaction between scanning an advertising means that the less power the advertiser spends advertising, the more
power the scanner will have to spend to see the advertising packets. The decision on balance will be dictated by your
design of your devices (which one is more constrained).

### Connection vs advertising

Instead of connecting to the device you can consider transferring data in advertising packets. This depends on the
nature of the data.

A transfer over a connection will allow you to use the ATT protocol, this can handle acknowledgement for you. This might
be a good choice if you're sending data that must get through reliably.

If your data is non-critical then advertising might be cheaper. You might have to accept less reliability and no built
in acknowledgment. Additional benefit is that multiple devices may receive the data and each scanner may make their own
decisions about power consumption.

### Periodic advertising

Periodic advertising allows you to get best of both worlds by having the power characteristics of advertising for the
peripheral but also saving power for the scanner. After finding periodic advertising through `createSync` the scanner
will only have to turn on the radio when the expected packet is due.

## Increasing throughput

### Modulation schemes

Depending on controller support different modulation schemes are available in BLE through `setPreferredPhys()` and
`setPhy()`. While the coded PHY will increase reliability in noisy environments and increase range at the cost of
power consumption, 2M PHY will increase the throughput saving power ber bit. If both devices support it and the signal
quality is good then this is recommended to be enabled. 

### Data length and ATT_MTU

Packet overhead strongly affects throughput. Newer controllers allow you to negotiate bigger MTUs thus decreasing the 
fragmentation overhead.

There are two separate MTUs to consider: the `ATT_MTU` (which affects ATT protocol operations) and data length extension
(which affects transport packets). Increasing the sizes will increase memory usage but greatly increase throughput.
`ATT_MTU` and data length are independent of each other.

The size of ATT_MTU doesn't have any other overhead than memory and should only be limited by your biggest attribute
and available memory.

The default value of data length supported by all controllers is 23 octets. If both controllers support data length
extension and a higher value is negotiated, the BLE stack will call `onDataLengthChange` in the `Gap::EventHandler`
registered by the user. The supported length is set in the link layer with a maximum of 251. For Cordio Link Layer it
is derived from the config option `cordio_ll.max-acl-size`.

Larger data length greatly increases throughput (although diminishing returns quickly set in above 80). The only
potential drawback is in noisy environments where longer packets may cause slower effective transfer due to
retransmissions (this is only related to data length, ATT_MTU does not affect this).

### ATT protocol

GATT client writes and GATT server updates come in two versions - with and without confirmation. Requiring confirmations
limits the throughput severely so to maximise throughput you can move reliability up from the stack to your application.
Without confirmations more than a single Peripheral <=> Central data exchange can be made per connection event. With
confirmations, the connection event ends when the peripheral replies as it needs to prepare the acknowledgement which
will be sent possibly in the next event.

### Packet timings

If you're not constrained by battery power it might be tempting to use maximum/minimum values where possible.
Advertising at maximum frequency and scanning continuously will speed up connecting. Setting intervals on connections
will minimise latency and maximise number of connection events.

One key thing to consider when setting the connection interval low is that you are creating a boundary between which a
sequence of packets must fit. This means that the last transfer must end before the next connection event starts
(plus 150us of inter packet space). This dead time may become significant if the connection interval is short and packet
length is long. 

The connection interval shouldn't be shorter than what your data requires in terms of latency.

# Test and measure

Due to complexity of the stack the only reliable way to truly maximise performance is to test your application with
representative data and measure the throughput and power usage. It's important to keep in mind that tweaking
parameters by trial and error and fine-tuning them will only be reliable for sequential operations on known stacks.

Many behaviours are implementation dependant and many operations are best effort and not guaranteed to succeed. The
stack has a lot of latitude to change its behaviour in accordance with resource constrains and other commitments. For
example your advertising may be severely affected by other operations that take precedence like keeping up a connection.

If your device needs to communicate with an unknown device or you run a non-trivial combination of concurrent
operations your fine-tuning should give way to sound principles since stack behaviours vary and you cannot test against
all stacks and sequences of operations.
