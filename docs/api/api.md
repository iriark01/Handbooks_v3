# Full API list

This is the full list of APIs Mbed OS offers application writers (it does not include the internal APIs, which are not intended for use by application code). The list indicates which of the APIs the [bare metal profile](../bare-metal/index.html) supports, and which of those are manually enabled (as opposed to enabled by default). For consistency, we also show the full profile's API support, although that is - and is expected to remain - all APIs.

For a list of APIs that were removed in Mbed OS 6, see [the deprecated APIs list at the bottom of this page](#deprecated-apis).

## Scheduling

The Mbed OS scheduling capabilities include managing objects such as threads, synchronization objects and timers. It also provides interfaces for attaching an application-specific idle hook function, reads the OS tick count and implements functionality to report RTOS errors.

### RTOS

| API | Full profile | Bare metal profile |
| - | - | - |
| [ConditionVariable](../apis/rtos-apis.html) | &#10004; | |
| [EventFlags](../apis/eventflags.html) | &#10004; | &#10004; |
| [Idle loop](../apis/idle-loop.html) | &#10004; |   |
| [Kernel interface functions](../apis/kernel-interface-functions.html) | &#10004; | `get_ms_count` only |
| [Mail](../apis/mail.html) | &#10004; | |
| [Mutex](../apis/mutex.html) | &#10004; | &#10004; |
| [Queue](../apis/queue.html) | &#10004; | |
| [Semaphore](../apis/semaphore.html) | &#10004; | &#10004;  |
| [ThisThread](../apis/thisthread.html) | &#10004; | &#10004;  |
| [Thread](../apis/thread.html) | &#10004; | |

### Event handling

| API | Full profile | Bare metal profile |
| - | - | - |
| [Event](../apis/event-handling-apis.html) | &#10004; | &#10004; (can be manually enabled) |
| [EventQueue](../apis/eventqueue.html) | &#10004; | &#10004; (can be manually enabled) |
| [UserAllocatedEvent](../apis/userallocatedevent.html) | &#10004; | &#10004; (can be manually enabled) |

## Drivers

Driver APIs include analog and digital inputs and outputs on development boards, as well as digital interfaces to a computer or external devices.

### Serial (UART) drivers

| API | Full profile | Bare metal profile |
| - | - | - |
| [BufferedSerial](../apis/serial-uart-apis.html) | &#10004; | &#10004;  |
| [UnbufferedSerial](../apis/unbufferedserial.html) | &#10004; | &#10004;  |

### SPI drivers

| API | Full profile | Bare metal profile |
| - | - | - |
| [QuadSPI (QSPI)](../apis/spi-apis.html) | &#10004; | &#10004; |
| [SPI](../apis/spi.html) | &#10004; | &#10004;  |
| [SPISlave](../apis/spislave.html) | &#10004; | &#10004;  |

### Input/Output drivers

| API | Full profile | Bare metal profile |
| - | - | - |
| [AnalogIn](../apis/i-o-apis.html) | &#10004; | &#10004; |
| [AnalogOut](../apis/analogout.html) | &#10004; | &#10004; |
| [BusIn](../apis/busin.html) | &#10004; | &#10004; |
| [BusOut](../apis/busout.html) | &#10004; | &#10004; |
| [BusInOut](../apis/businout.html) | &#10004; | &#10004; |
| [DigitalIn](../apis/digitalin.html) | &#10004; | &#10004; |
| [DigitalOut](../apis/digitalout.html) | &#10004; | &#10004; |
| [DigitalInOut](../apis/digitalinout.html) | &#10004; | &#10004; |
| [InterruptIn](../apis/interruptin.html) | &#10004; | &#10004;  |
| [PortIn](../apis/portin.html) | &#10004; | &#10004;  |
| [PortOut](../apis/portout.html) | &#10004; | &#10004;  |
| [PortInOut](../apis/portinout.html) | &#10004; | &#10004;  |
| [PwmOut](../apis/pwmout.html) | &#10004; | &#10004;  |

### USB drivers

| API | Full profile | Bare metal profile |
| - | - | - |
| [USBAudio](../apis/usb-apis.html) | &#10004; | &#10004;  |
| [USBCDC](../apis/usbcdc.html) | &#10004; | &#10004;  |
| [USBCDC_ECM](../apis/usbcdc-ecm.html) | &#10004; |  |
| [USBHID](../apis/usbhid.html) | &#10004; | &#10004;  |
| [USBKeyboard](../apis/usbkeyboard.html) | &#10004; | &#10004;  |
| [USBMIDI](../apis/usbmidi.html) | &#10004; | &#10004;  |
| [USBMouse](../apis/usbmouse.html) | &#10004; | &#10004;  |
| [USBMouseKeyboard](../apis/usbmousekeyboard.html) | &#10004; | &#10004;  |
| [USBMSD](../apis/usbmsd.html) | &#10004; | &#10004; |
| [USBSerial](../apis/usbserial.html) | &#10004; | &#10004;  |

### Other drivers

| API | Full profile | Bare metal profile |
| - | - | - |
| [CAN](../apis/other-driver-apis.html)| &#10004; | &#10004;  |
| [Flash IAP](../apis/flash-iap.html) | &#10004; | &#10004;  |
| [I2C](../apis/i2c.html) | &#10004; | &#10004;  |
| [I2CSlave](../apis/i2cslave.html) | &#10004; | &#10004;  |
| [MbedCRC](../apis/mbedcrc.html) | &#10004; | &#10004;  |
| [ResetReason](../apis/resetreason.html) | &#10004; | &#10004;  |
| [Watchdog](../apis/watchdog.html) | &#10004; | &#10004; |

## Platform

Platform APIs provide general purpose MCU management infrastructure, common data structures and a consistent user experience on top of different standard libraries and toolchains.

### Time

| API | Full profile | Bare metal profile |
| - | - | - |
| [RTC](../apis/time-apis.html) | &#10004; | &#10004;  |
| [Ticker](../apis/ticker.html) | &#10004; | &#10004;  |
| [Time](../apis/time.html) | &#10004; | &#10004;  |
| [Timeout](../apis/timeout.html) | &#10004; | &#10004; |
| [Timer](../apis/timer.html) | &#10004; | &#10004; |
| [Wait](../apis/wait.html) | &#10004; | &#10004;  |

### Power

| API | Full profile | Bare metal profile |
| - | - | - |
| [DeepSleepLock](../apis/power-apis.html) | &#10004; | &#10004;  |
| [LowPowerTicker](../apis/lowpowerticker.html) | &#10004; | &#10004;  |
| [LowPowerTimeout](../apis/lowpowertimeout.html) | &#10004; | &#10004;  |
| [LowPowerTimer](../apis/lowpowertimer.html) | &#10004; | &#10004;  |
| [Power management (sleep)](../apis/power-management-sleep.html) | &#10004; | &#10004; |

### Memory

| API | Full profile | Bare metal profile |
| - | - | - |
| [mbed_mem_trace (Memory tracing)](../apis/memory-apis.html) | &#10004; | &#10004;  |
| [mpug_mgmt (MPU management)](../apis/mpu-management.html) | &#10004; | &#10004;  |
| [MemoryPool](../apis/memorypool.html) | &#10004; |   |
| [mbed_stats (Mbed statistics)](../apis/mbed-statistics.html) | &#10004; | &#10004;  |

### Other Platform APIs

| API | Full profile | Bare metal profile |
| - | - | - |
| [Assert](../apis/other-platform-apis.html) | &#10004; | &#10004;  |
| [ATCmdParser](../apis/atcmdparser.html) | &#10004; | &#10004;  |
| [Callback](../apis/callback.html) | &#10004; | &#10004; |
| [CircularBuffer](../apis/circularbuffer.html) | &#10004; | &#10004;  |
| [CriticalSectionLock](../apis/criticalsectionlock.html) | &#10004; | &#10004;  |
| [Debug](../apis/debug.html) | &#10004; | &#10004;  |
| [Error handling](../apis/error-handling.html) | &#10004; | &#10004;  |
| [FileHandle](../apis/filehandle.html) | &#10004; | &#10004;  |
| [NonCopyable](../apis/noncopyable.html) | &#10004; | &#10004;  |
| [PlatformMutex](../apis/platformmutex.html) | &#10004; | &#10004;  |
| [Poll](../apis/poll.html) | &#10004; | &#10004;  |
| [ScopedRamExecutionLock](../apis/scopedramexecutionlock.html) | &#10004; | &#10004;  |
| [ScopedRomWriteLock](../apis/scopedromwritelock.html) | &#10004; | &#10004;  |
| [SharedPtr (Shared pointer)](../apis/shared-pointer.html) | &#10004; | &#10004;  |
| [Span](../apis/span.html) | &#10004; | &#10004; |

## Data storage

The storage APIs include file system APIs, for file system operations, and block devices, which provide the raw storage for the file systems.

### File system APIs

| API | Full profile | Bare metal profile |
| - | - | - |
| [Dir](../apis/file-system-apis.html) | &#10004; | &#10004; (can be manually enabled)|
| [FATFileSystem](../apis/fatfilesystem.html) | &#10004; | &#10004; (can be manually enabled) |
| [File](../apis/file.html) | &#10004; | &#10004; (can be manually enabled) |
| [FileSystem](../apis/filesystem.html) | &#10004; | &#10004; (can be manually enabled) |
| [KVStore](../apis/kvstore.html) | &#10004; | &#10004; (can be manually enabled) |
| [kvstore_global_api (Static Global API)](../apis/static-global-api.html) | &#10004; | &#10004; (can be manually enabled) |
| [LittleFileSystem](../apis/littlefilesystem.html) | &#10004; |&#10004; (can be manually enabled) |

### BlockDevice (block-based storage) APIs

| API | Full profile | Bare metal profile |
| - | - | - |
| [BlockDevice](../apis/blockdevice-apis.html) | &#10004; | &#10004; (can be manually enabled) |
| [BufferedBlockDevice](../apis/bufferedblockdevice.html) | &#10004; | &#10004; (can be manually enabled) |
| [ChainingBlockDevice](../apis/chainingblockdevice.html) | &#10004; | &#10004; (can be manually enabled) |
| [DataFlashBlockDevice](../apis/dataflashblockdevice.html) | &#10004; |&#10004; (can be manually enabled) |
| [FlashIAPBlockDevice](../apis/flashiapblockdevice.html) | &#10004; | &#10004; (can be manually enabled) |
| [FlashSimBlockDevice](../apis/flashsimblockdevice.html) | &#10004; | &#10004; (can be manually enabled) |
| [HeapBlockDevice](../apis/heapblockdevice.html) | &#10004; | &#10004; (can be manually enabled) |
| [MBRBlockDevice](../apis/mbrblockdevice.html) | &#10004; | &#10004; (can be manually enabled) |
| [ProfilingBlockDevice](../apis/profilingblockdevice.html) | &#10004; | &#10004; (can be manually enabled) |
| [QSPIFBlockDevice](../apis/qspifblockdevice.html) | &#10004; |&#10004; (can be manually enabled) |
| [SDBlockDevice](../apis/sdblockdevice.html) | &#10004; | &#10004; (can be manually enabled) |
| [SlicingBlockDevice](../apis/slicingblockdevice.html) | &#10004; | &#10004; (can be manually enabled) |
| [SPI Flash block device](../apis/spi-flash-block-device.html)| &#10004; | &#10004; (can be manually enabled) |

### PSA compliant

| API | Full profile | Bare metal profile |
| - | - | - |
| [PSA internal storage](../apis/psa-compliant-apis.html) | &#10004; |  |
| [PSA protected storage](../apis/psa-protected-storage.html) | &#10004; |  |

## Connectivity

Connectivity APIs include:

- Network socket: The application programming interface for IP networking, supporting both TCP and UDP protocols.
- Network interface: The application level APIs where you choose the driver, connectivity method and IP stack. These include Ethernet, Wi-Fi, cellular and Mesh interfaces.
- Secure socket: DTLS and TLS streams over the existing Socket transport.
- DNS: Perform DNS host name resolutions to convert resource names to IP addresses.
- Bluetooth low energy (BLE): A low power wireless technology standard for building personal area networks.
- NFC: Near-Field Communication (NFC), a short-range radio technology for use cases such as contactless payments, access control and device pairing.
- LoRaWAN: A technology designed for low-power battery-powered devices that operate in an unlicensed spectrum, creating high density wide-area networks.

### Network socket

| API | Full profile | Bare metal profile |
| - | - | - |
| [Non-IP cellular socket](../apis/network-socket-apis.html) | &#10004; | |
| [Socket](../apis/socket.html) | &#10004; | |
| [SocketAddress](../apis/socketaddress.html) | &#10004; | |
| [SocketStats](../apis/socketstats.html) | &#10004; | |
| [TCPSocket](../apis/tcpsocket.html) | &#10004; |  |
| [UDPSocket](../apis/udpsocket.html) | &#10004; |  |

### Network interface

| API | Full profile | Bare metal profile |
| - | - | - |
| [Cellular](../apis/network-interface-apis.html) | &#10004; | |
| [Ethernet](../apis/ethernet.html) | &#10004; | |
| [Mesh](../apis/mesh-api.html) | &#10004; | |
| [Network status](../apis/network-status.html) | &#10004; | |
| [Wi-Fi](../apis/wi-fi.html) | &#10004; | |

### Secure socket

| API | Full profile | Bare metal profile |
| - | - | - |
| [DTLSSocket](../apis/secure-socket-apis.html) | &#10004; |  |
| [TLSSocket](../apis/tlssocket.html) | &#10004; | |

### DNS

| API | Full profile | Bare metal profile |
| - | - | - |
| [DNS Resolver](../apis/dns-apis.html) | &#10004; | |

### Bluetooth (BLE)

| API | Full profile | Bare metal profile |
| - | - | - |
| [BatteryService](../apis/bluetooth-apis.html) | &#10004; | &#10004; (can be manually enabled) |
| [BLE](../apis/ble.html) | &#10004; | &#10004; (can be manually enabled) |
| [GAP](../apis/gap.html) | &#10004; | &#10004; (can be manually enabled) |
| [GattClient](../apis/gattclient.html) | &#10004; | &#10004; (can be manually enabled) |
| [GattServer](../apis/gattserver.html) | &#10004; | &#10004; (can be manually enabled) |
| [HeartRateService](../apis/heartrateservice.html) | &#10004; | &#10004; (can be manually enabled) |
| [SecurityManager](../apis/securitymanager.html) | &#10004; | &#10004; (can be manually enabled) |

### NFC

| API | Full profile | Bare metal profile |
| - | - | - |
| [MessageBuilder](../apis/nfc-apis.html) | &#10004; | |
| [MessageParser](../apis/messageparser.html) | &#10004; | |
| [NFCController](../apis/nfccontroller.html) | &#10004; |&#10004; (can be manually enabled) |
| [NFC EEPROM](../apis/nfc-eeprom.html) | &#10004; | &#10004; (can be manually enabled) |
| [SimpleMessageParser](../apis/simplemessageparser.html) | &#10004; | |

### LoRaWAN

| API | Full profile | Bare metal profile |
| - | - | - |
| [LoRaWANInterface](../apis/lorawan-apis.html) | &#10004; | |
| [LoRaRadio](../apis/loraradio.html) | &#10004; | |

## Security

With Arm Mbed TLS, a comprehensive SSL/TLS solution, you can include cryptographic and SSL/TLS capabilities in your code.

| API | Full profile | Bare metal profile |
| - | - | - |
| [DeviceKey](../apis/security-apis.html) | &#10004; | &#10004; (can be manually enabled) |
| [Mbed Crypto](../apis/mbed-crypto.html) | &#10004; |&#10004; (can be manually enabled) |
| [PSA initial attestation](../apis/psa-initial-attestation.html) | &#10004; | |
| [PSA lifecycle](../apis/psa-lifecycle.html) | &#10004; |  |
| [TLS](../apis/tls.html) | &#10004; | &#10004; (can be manually enabled) |

<h2 id="deprecated-apis">Deprecated APIs: moving from Mbed OS 5 to 6</h2>

If you're moving your program from Mbed OS 5 to 6, you will need to replace deprecated APIs. The table lists classes that have been completely removed. Functions and methods that have been removed from other classes are listed in each class's Doxygen ouput, and [summarised here](../mbed-os-api-doxy/deprecated.html).

| Deprecated API | Replaced by |
| - | - |
| `Serial` |`printf` and `puts` to access the console. <br> `BufferedSerial` for blocking applications.<br> `UnbufferedSerial` for bypassing locks in IRQ or short of RAM. |
| `RawSerial` | `UnbufferedSerial` |
| `UARTSerial` | `BufferedSerial` |
| `Ethernet` | `EthInterface` to get an Ethernet object. <br> `NetworkInterface` to get an instance of an appropriate network interface (WiFi or Ethernet). |
| BLE services: `iBeacon`, `UARTService`, `URIBeaconConfigService` | No replacement available |
| `TCPServer` | `TCPSocket` |
| `NVStore` | `KVStore` |
| `RtosTimer` | `EventQueue` |
| `InterruptManager` | No replacement. |
| `CallChain` | No replacement. |
