# Glossary

## A

**API** - [Application programming interface](../apis/index.html).

**Application** - An executable software module built out of libraries that acts as a final product.

**Arm Mbed CLI** - The name of the Arm Mbed [command-line tool](../build-tools/mbed-cli-1.html), packaged as `mbed-cli`.

**Arm Mbed interface** - The extra chip that sits on all [Mbed Enabled development boards](index.html). It's what makes the target chip (for example, K64F) look like a USB drive. It usually runs a separate piece of software that generally doesn't change. That software is usually `DAPLink`, `CMSIS-DAP` or `STLink`.

**Arm Mbed Online Compiler** - [Arm’s online tool](../build-tools/mbed-online-compiler.html), which you can use to create and compile your code.

**Arm Mbed OS** - Arm's [operating system](https://os.mbed.com/docs) for the Internet of Things.

**Arm Mbed Studio** - A local development environment for Mbed OS programs written in C/C++. Mbed Studio [has its own documentation](https://os.mbed.com/docs/mbed-studio/).

**Arm Mbed TLS** - A [comprehensive SSL/TLS solution](../apis/tls.html) that makes it easy for developers to include cryptographic and SSL/TLS capabilities in their software and embedded products. As an SSL library, it provides an intuitive API, readable source code and a minimal and highly configurable code footprint.

## B

**Bit** - A basic unit of digital information that can be one of two values: `0` (`false`) or `1` (`true`).

**BLE** - [Bluetooth Low Energy](../apis/ble.html).

**Blinky** - An [example application](../quick-start/index.html) that you can use to get to know Arm Mbed OS and the development tools. It’s one of the simplest examples of Mbed OS.

**Block Device** - A [file](../porting/porting-storage.html) that represents a device, with data that can be read or written to it in blocks.

**Board** - Hardware that can run an Mbed OS application. Usually refers to an [Mbed Enabled development board](https://os.mbed.com/platforms/), but can also be a custom board. Its software representation in the build tools is as a build target.

**Boolean** - A binary variable, having two possible values called `true` and `false`.

**Bootloader** - [The program](../tutorials/bootloader.html) that loads Mbed OS when a board is turned on.

**Build** - The full process of converting an application's source code into a binary that can be flashed onto a board. The build cannot be board-agnostic; it is always done for a specific board, represented as the build target (see **Build target**).

**Build Profile** - Mbed OS supports three primary [build profiles](../program-setup/build-profiles-and-rules.html): develop, debug and release.

**Build Script** - A build automation and generation utility.

**Build target** or **target** - A destination for a software build, for example an MCU, development board or custom board. Build targets are defined in either `targets.json` or `custom_targets.json`. A build (with Mbed CLI, the Online Compiler and Mbed Studio) is always done for a specific target.

**Byte** - A unit of digital information that consists of 8 bits (see `Bit`).

## C

**Callback** - Any [executable code](../apis/callback.html) that is passed as an argument to other code, which is expected to call back (execute) the argument at a given time.

**CAN** - [Controller-area network](../apis/other-driver-apis.html).

**CI** - Continuous integration.

**Class** - An extensible program-code-template for creating objects, providing initial values for state and implementations of behavior.

**CLI** - Command-line interface.

**Component**

    - In hardware: See [https://os.mbed.com/components/](https://os.mbed.com/components/).
    - In software: An implementation of a hardware component.

**CMSIS-DAP** - The precursor to DAPLink, this [project](https://github.com/mbedmicro/cmsis-dap) is deprecated due to known bugs. You should not use it in any new designs.

## D

**DAPLink** - An Arm maintained [project](https://github.com/mbedmicro/DAPLink) that is under active development.

**Debugging** - The [process](../debug-test/index.html) of finding and solving problems in code.

**Deprecation** - Marking a piece of code as out of date. You should not write new code that depends on deprecated APIs. We will remove deprecated APIs when our code no longer depends on them.

## E

**Exporter** - Use the Arm Mbed [exporters](../build-tools/third-party-build-tools.html#about-the-exporters) to export your code to various third party tools and IDEs.

## G

**GitHub** - A web-based [Git development platform](https://github.com/armmbed/mbed-os) for version-controlled repositories.

**GPIO** - General-purpose input/output, a generic pin that is controllable by the user at run-time.

**Greentea** - **G**eneric **re**gression **en**vironment for **te**st **a**utomation. [Greentea](../debug-test/greentea-for-testing-applications.html) is the automated testing tool for Arm Mbed OS development.

## H

**Hardware** - See `board`.

**htrun** - An Mbed OS command used to drive test binary flashing, hardware reset and test execution.

## I

**I2C** - [Interintegrated Circuit](../apis/i2c.html) (short-distance, intraboard communication).

**IDE** - Integrated Development Environment.

**int** - Short for "integer", it is a variable type that can be used to define numeric variables holding whole numbers.

## L

**Library** - A software module that you can use to build applications.

**LoRA** - Long range (low power wireless platform).

## M

**Makefile** - A file containing a set of directives used with the make build automation tool.

**Mesh** - A network topology in which each node relays data for the network.

**Module**
    - In software: A self-contained unit of code containing classes and functions.
    - In hardware: A microcontroller, IoT centric connectivity and required onboard memory. See [https://os.mbed.com/modules/](https://os.mbed.com/modules/).

## N

**Nibble** - A unit of digital information that consists of 4 bits (see `Bit`).

## P

**Platform** - See `board`.

**Porting** - A process to add target support to Mbed OS.

**Program** - See `application`.

**Pull Request** - Used by version-controlled repositories to propose and collaborate on changes.

## Q

**Quick start** - A getting started guide to Mbed OS.

## R

**RAII** - Resource Acquisition Is Initialization.

**REST** - Representational State Transfer (API).

**RTOS** - [Real-Time Operating System](../apis/scheduling-concepts.html).

**RTX** - [Keil RTX](https://www2.keil.com/mdk5/cmsis/rtx) is a royalty-free, deterministic Real-Time Operating System designed for Arm Cortex-M devices.

## S

**Serial** - A protocol used in data transmission for the transfer of individual bits of information. The Serial API has been deprecated; please see the BufferedSerial and UnbufferedSerial APIs.

**SPI** - [Serial Peripheral Interface](../apis/spi.html).

**Static Memory** - The allocation of memory at compile time, before the program is executed.

**SSL** - Secure sockets layer.

**STLink** - STMicro's [firmware](http://www.st.com/content/st_com/en/products/embedded-software/development-tool-software/stsw-link007.html) that performs the same tasks as DAPLink but uses a different [driver](http://www.st.com/content/st_com/en/products/embedded-software/development-tool-software/stsw-link009.html).

## T

**Target** - See `build target`.

**Terminal Application** - [Applications](../program-setup/serial-communication.html#using-terminal-applications) that run on your host PC that provide a window where your Mbed board can print and where you can type characters back to your board.

**Timeout** - The [maximum amount of time](../apis/timeout.html) an operation can take before it is considered a failure and stopped.

**TLS** - Transport Layer Security.

**Toolchain** - A [group of programming tools](../build-tools/third-party-build-tools.html#setting-up-a-local-debug-toolchain).

**Travis CI** - a continuous integration service used to build and test software projects hosted at GitHub (see `GitHub`).

## U

**utest** - A [test harness](../debug-test/utest-asynchronous-c-test-harness.html) you can use to execute a specified series of (asynchronous) C++ test cases.
