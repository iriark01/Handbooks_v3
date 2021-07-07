# Docker use in Mbed OS

The easiest and quickest way to get a build environment setup for Mbed OS projects is through the use of Docker.

We maintain an Mbed OS image which includes the following tooling:
* Arm Embedded GCC Toolchain
* CMake
* Mbed CLI 2
* Greentea
* PyOCD

Our image is maintained [on GitHub](https://github.com/ARMmbed/mbed-os-docker-images) and [is open for contributions](https://github.com/ARMmbed/mbed-os-docker-images/pulls).

The image is built and tested for the following architectures:
* 64-bit ARM / aarch64
* 64-bit x86 / x86_64

<span class="notes">**Note:** Our Docker image leverages Mbed CLI 2, so only supports projects built with Mbed OS 6.4 or more recent.</span>

## Using the image
### Command line

The Mbed OS Docker container can be used using Docker Desktop on any supported platform (Windows, Linux & Mac).

#### Examples

Run interactively in current directory and compile the current application:

```
git clone https://github.com/ARMmbed/mbed-os-example-blinky.git && cd mbed-os-example-blinky

docker run -i -t --mount=type=bind,source="$(pwd)",destination=/var/mbed,consistency=delegated -w /var/mbed mbedos/mbed-os-env-cmake

mbed-tools compile -t GCC_ARM -m DISCO_L475VG_IOT01A
```

Build an Mbed OS application directly:

```
docker run -i -t --mount=type=bind,source="$(pwd)",destination=/var/mbed,consistency=delegated -w /var/mbed mbedos/mbed-os-env-cmake mbed-tools compile -t GCC_ARM -m DISCO_L475VG_IOT01A
```

### Continuous integration

We are in the process of moving our CI to use the GitHub container, and this can provide a great basis for your own CI for your Mbed-based projects.

#### Examples

A simple example of a GitHub Actions workflow for building your app would look like:
```
XXX
```

For a real-life example you can check out the [following GitHub Actions workflow for the xxx Mbed OS example.

### Visual Studio Code & GitHub Codespaces

Visual Studio Code now supports [Remote Containers Extensions](https://code.visualstudio.com/docs/remote/containers) which lets you load a workspace inside a container environment.

If you have access to [GitHub CodeSpaces](https://github.com/features/codespaces) you can open your development environment directly from GitHub!

#### Examples

The [Mbed OS Blinky example]() TODO!

## Limitations

### USB Devices

There are various limitations with connecting targets to a Docker container.
You can explicitely attach devices using the `--device` flag, however your milage may vary in terms of using it in practice. On Mac, you will need to capture the device first in the underlying VM.

For this reason, running PyOCD or GreenTea from the Docker container is not trivial at the moment! We will be looking at future-proof solutions.

