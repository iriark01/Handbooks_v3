# GattClient

You can use Generic Attribute Profile (GATT) to discover services, characteristics and descriptors and to perform operations on them. The interaction happens between two peers, one of which is the client (which initiates interactions) and the other is the server (which responds). You can use Attribute Protocol (ATT) to implement this interaction. `GattClient` defines procedures required for interacting with a remote `GattServer`.

## Discovery procedures

A GattServer hosts a fixed set of services. These services are a logical composition of characteristics that may be discovered, read or written and can broadcast their state to a connected client. These characteristics may also contain metainformation and named characteristic descriptors. A characteristic descriptor may indicate the unit used for a characteristic value, describe the characteristic purpose in a textual form or allow a client to register for update notifications for the characteristic value.

Prior to any interaction with a server characteristic, a GattClient discovers the layout of the services and characteristics present on the server.

The layout of the descriptors of a characteristic may also be issued as an extra discovery step.

## Attribute manipulation

As a result of the discovery process, the client can start interacting with the characteristic discovered. Depending on the characteristic properties (acquired during discovery), a client can read or write the value of a given characteristic.

Mbed BLE abstracts read and write operations to offer a single API that can be used to read or write characteristic values. The application code does not have to handle the necessary fragmentation or reassembly process if the attribute value to be transported can't fit in a single data packet.

## Attribute Protocol Maximum Transmission Unit (ATT_MTU)

`ATT_MTU` is the maximum size of the attribute protocol packet. Operation on attributes too large to fit into a single packet are split across multiple operations.

This is independent of the data length, which controls the over-the-air packet payload size (which the GAP handles). An L2CAP packet containing the attribute protocol packet is fragmented over many packets if required.

Only `GattClient` can trigger the exchange of `ATT_MTU` between client and server. Depending on the implementation of the bluetooth stack, the client may trigger the exchange upon connection. You may also manually request the exchange using `negotiateAttMtu`. If an exchange happens, the biggest value possible across both devices will be used. Negotiation is only a best-effort process and does not guarantee a higher value being set.

`ATT_MTU` is at least 23 octets by default. If a larger size is negotiated, the user application will be informed through the `onAttMtuChange` function called in the `GattClient::EventHandler`. (`GattServer::EventHandler` is also informed.)

## Server initiated events

When a server updates a characteristic value, it can forward the new value to any registered clients. Clients may register for these updates on a per-characteristic basis. The server sends the updates by using notifications (no confirmation from client) or indications (client confirms receipt). This mechanism minimizes the number of transactions between a client and a server by avoiding polling.

Clients register for these updates by setting the Client Characteristic Configuration Descriptor (CCCD) value. This is an attribute, and the client needs to discover its descriptor. It is present in the characteristic if its notify or indicate properties are set.

## GattClient class reference

[![View code](https://www.mbed.com/embed/?type=library)](https://os.mbed.com/docs/mbed-os/development/mbed-os-api-doxy/classble_1_1_gatt_client.html)

## GattClient examples

### Characteristic writes

[![View code](https://www.mbed.com/embed/?url=https://github.com/ARMmbed/mbed-os-example-ble/blob/mbed-os-6.7.0/BLE_GattClient_CharacteristicWrite/source/)](https://github.com/ARMmbed/mbed-os-example-ble/blob/mbed-os-6.7.0/BLE_GattClient_CharacteristicWrite/source/main.cpp)

### Characteristic updates

[![View code](https://www.mbed.com/embed/?url=https://github.com/ARMmbed/mbed-os-example-ble/blob/mbed-os-6.7.0/BLE_GattClient_CharacteristicUpdates/source/)](https://github.com/ARMmbed/mbed-os-example-ble/blob/mbed-os-6.7.0/BLE_GattClient_CharacteristicUpdates/source/main.cpp)
