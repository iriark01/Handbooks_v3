# BLE 

Bluetooth low energy (BLE) is a low power wireless technology standard for building personal area networks. Typical
applications of BLE are health care, fitness trackers, beacons, smart home, security, entertainment, proximity sensors,
industrial and automotive.

Arm Mbed BLE is the Bluetooth Low Energy software solution for Mbed. Many Mbed
[targets and components](https://os.mbed.com/platforms/?mbed-enabled=15&connectivity=3) support Mbed BLE. Developers can
use it to create new BLE enabled applications.

## BLE API

Mbed's BLE API is available through C++ classes. It hides the BLE stack’s complexity and is compatible with all
BLE-enabled Mbed board. It automatically configures the clocks, timers and other hardware peripherals to work at their
lowest power consumption.

### BLE API headers

BLE API is accessible through several header files:

- [BLE.h](https://github.com/ARMmbed/mbed-os/blob/master/connectivity/FEATURE_BLE/include/ble/BLE.h) - acquire the BLE
  instance, perform initialisation
- [Gap.h](https://github.com/ARMmbed/mbed-os/blob/master/connectivity/FEATURE_BLE/include/ble/Gap.h) - advertising,
  scanning, connecting
- [GattClient.h](https://github.com/ARMmbed/mbed-os/blob/master/connectivity/FEATURE_BLE/include/ble/GattClient.h) -
  GATT operations as client
- [GattServer.h](https://github.com/ARMmbed/mbed-os/blob/master/connectivity/FEATURE_BLE/include/ble/GattServer.h) -
  GATT operations as server
- [SecurityManager.h](https://github.com/ARMmbed/mbed-os/blob/master/connectivity/FEATURE_BLE/include/ble/SecurityManager.h) -
  authentication, keys, encryption

Specific documentation for each component is available inside each of these headers.

### Thread safety

BLE implementation does not provide thread safety and assumes single thread execution. Event processing and API calls
must be dispatched from the same thread.

### Asynchronous calls

Many API calls are asynchronous and provide results through callbacks. These are implemented as events. To receive these
events register an EventHandler that is specific to that component. For example to receive events from Gap, use
`Gap::setEventHandler()` passing in your implementation that inherits from `Gap::EventHandler`. Your class will override
the events (methods) you are interested in, the others will inherit the do-nothing implementations provided by the parent.

### Instancing a BLE device

All BLE operations are executed on an instance of BLE accessible through a function in the header `ble/BLE.h`.

```c
#include "ble/BLE.h"

BLE& mydevicename = BLE::Instance();
```

### BLE stacks

To build and application using BLE  you will be using the Mbed OS BLE API and an implementation of the BLE stack
appropriate for your board. The implementation is split into Host and Controller part. They can both run on the same
chip or two separate ones. They will be both communicating through HCI (Host Controller Interface, a well defined
protocol that is part of the Bluetooth specification). Read more about the HCI interface in Mbed OS
[here](https://github.com/ARMmbed/mbed-os/blob/master/connectivity/FEATURE_BLE/include/ble/driver/doc/HCIAbstraction.md).

Currently, all implementation use the Cordio stack for the Host part. The Controller implementation may be either also
Cordio or any other vendor supplier one. Each board will have a driver that implements the communication channel
between the Host and its implementation of the controller. To add support for a new board please refer to the
[BLE porting guide](https://github.com/ARMmbed/mbed-os/blob/master/connectivity/FEATURE_BLE/include/ble/driver/doc/PortingGuide.md).

## Debugging

To learn about debugging with mbed go to:

[Debugging Mbed OS](../debug-test/index.html)

However, keep in mind when trying to debug connectivity issues that if more than one device is involved it might
not be possible to stop your target without the communication breaking down. A less invasive way to help you understand
what is happening might be to use tracing.

## Tracing

To debug issues (or to understand what the stack is doing) it may be helpful to enable tracing.

To enable traces override configuration options in you mbed_app.json:

```
    "target_overrides": {
        "*": {
            "mbed-trace.enable": true,
            "mbed-trace.max-level": "TRACE_LEVEL_DEBUG",
            "cordio.trace-hci-packets": false,
            "cordio.trace-cordio-wsf-traces": false,
            "ble.trace-human-readable-enums": true
        }
    }
```

Compile your application with `--profile debug`. Please note that with all options enabled your application may become
too big - disable some options or lower the `mbed-trace.max-level`. Detailed documentation is available in the tracing
[README.md](https://github.com/ARMmbed/mbed-os/blob/master/platform/mbed-trace/README.md).

All BLE modules contain tracing, each of the modules prefixed with a unique tag:
- `BLE ` - general BLE traces  
- `BLGP` - GAP
- `BLGS` - GATT Server
- `BLGC` - GATT Client
- `BLSM` - Security Manager
- `BLDB` - Security Database
- `BLHC` - HCI
- `BLCO` - Cordio stack
- `BLDM` - GAP pal
- `BLAT` - ATT client

Any contributions to BLE should include appropriate tracing code.

## BLE examples

We have placed all of our BLE examples in a single GitHub repository:
- [GitHub repository](https://github.com/ARMmbed/mbed-os-example-ble)

Use the release version matching the mbed-os version you plan to use.

Development happens on the `development` branch. If you report an issue or open a PR, please check the version on the
`development` branch and target it for any proposed changes.

## BLE class reference

[![View code](https://www.mbed.com/embed/?type=library)](https://os.mbed.com/docs/mbed-os/development/mbed-os-api-doxy/classble_1_1_b_l_e.html)
