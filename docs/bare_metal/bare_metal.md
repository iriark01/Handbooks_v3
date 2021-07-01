# Mbed OS bare metal profile

Bare metal is a profile of Mbed OS for ultraconstrained hardware: compact and without an RTOS. It represents a different way of working with Mbed OS: the bare metal profile builds only the smallest set of APIs that applications require - driver APIs, platform APIs and a subset of the RTOS APIs. This gives you better control of the application's final size than the full profile, which relies on the build time linker to remove classes that are not used and are not a dependency.

The bare metal profile implements a subset of Mbed OS's RTOS APIs that are useful in non-threaded applications, such as semaphores (calling the release API from interrupts) and tickers (to set up a recurring interrupt). It does not include [Keil RTX](https://www2.keil.com/mdk5/cmsis/rtx), and is therefore suitable for applications that do not require complex thread management. Instead of the RTOS's scheduler, all activities are polled or interrupt-driven. This simplifies application code and allows using APIs that are not thread safe. Just as important, you can use the code-optimized versions of the C standard libraries, `microlib` and `newlib-nano`, which are much smaller than the thread safe equivalents the full profile requires.

The Mbed OS build tools - Mbed CLI, Mbed Online Compiler and Mbed Studio - all support working with the bare metal profile.

## Features

For a breakdown of supported APIs, please see [the full API list](../apis/index.html). To enable individual APIs, [see the usage instructions](../bare-metal/using-the-bare-metal-profile.html).

<span class="notes">**Note:** Because bare metal uses some APIs that Mbed OS classifies as RTOS APIs, some class names that traditionally belong in RTOS programming are used in bare metal. For example, bare metal uses the class `ThisThread` despite not using threads.</span>

&#10004; : Supported - by default or manually | &#10007; : Not supported

<table>
    <thead>
        <tr>
            <th colspan="2">Features</th>
            <th>Support details</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td rowspan="6">Core</td>
            <td>Drivers</td>
            <td>&#10004;</td>
        </tr>
        <tr>        
            <td>Events</td>
            <td>&#10004; (can be manually enabled)</td>
        </tr>
        <tr>        
            <td>HAL</td>
            <td>&#10004; (can be manually enabled)</td>
        </tr>
        <tr>        
            <td>Platform</td>
            <td>&#10004;</td>
        </tr>
            <tr>        
            <td>RTOS APIs</td>
            <td>Enabled by default: Semaphore, Mutex, EventFlags, ThisThread.<br><br> All other APIs not supported.</td>
        </tr>
        <tr>        
            <td>Storage</td>
            <td>&#10004; (can be manually enabled)</td>
        <tr>
            <td rowspan="8">Connectivity</td>
            <td>802.15.4_RF</td>
            <td>&#10007;</td>
        </tr>
        <tr>
            <td>Wifi</td>
            <td>&#10007;</td>
        </tr>
        <tr>
            <td>Cellular</td>
            <td>&#10007;</td>
        </tr>
        <tr>
            <td>LoRa</td>
            <td>&#10004; (can be manually enabled)</td>
        </tr>
        <tr>
            <td>LWIP stack</td>
            <td>&#10007;</td>
        </tr>
        <tr>
            <td>Nanostack</td>
            <td>&#10007;</td>
        </tr>
        <tr>
            <td>Network Socket</td>
            <td>&#10007;</td>
        </tr>
        </tr>
        <tr>
            <td>BLE</td>
            <td>&#10004; (can be manually enabled)<br>Except the BlueNRG-MS component</td>
        </tr>    
        <tr>
            <td>NFC</td>
            <td>&#10004; (can be manually enabled)</td>
        </tr>
        <tr>
            <td rowspan="4">Security</td>
            <td>PSA</td>
            <td>&#10007;</td>
        </tr>
        <tr>
            <td>Mbed Crypto</td>
            <td>&#10004; (can be manually enabled)</td>
        </tr>
        <tr>
            <td>Devicekey</td>
            <td>&#10004; (can be manually enabled)</td>
        </tr>  
        <tr>
            <td>Mbed TLS</td>
            <td>&#10004; (can be manually enabled)</td>
        </tr>
    </tbody>
</table>


## Documentation

The bare metal documentation covers:

- A [bare metal usage guide](../bare-metal/using-the-bare-metal-profile.html) that shows how to set up a bare metal application, or migrate an Mbed 2 application, and enable non-default APIs.
- [A short review of small C libraries](../bare-metal/using-small-c-libraries.html).
- [A porting guide for Mbed OS 2 targets](../bare-metal/porting-a-target-from-mbed-os-2-to-mbed-os-6-bare-metal.html).

Additionally, our [quick starts](../quick-start/index.html) include a bare metal version of the Blinky example application.
