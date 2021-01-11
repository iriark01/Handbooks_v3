# CMake target porting

See below instructions to add support for Mbed targets to build with CMake using mbed-tools.

Important variables provided for Mbed target:

- `MBED_TARGET_LABELS`: a list of labels added to a given Mbed target coming from the Mbed target default configuration file `targets.json`.
- `MBED_TARGET_DEFINITIONS`: a list of macro definitions added to a given Mbed target coming from the Mbed target default configuration file `targets.json`.

- `MBED_CONFIG_DEFINITIONS`: a list of macro definitions added to a given Mbed target coming from various Mbed library configuration files.
- `MBED_TARGET_SUPPORTED_C_LIBS`: a list of C library types supported by a given Mbed target coming from the Mbed target default configuration file `targets.json`.
- `MBED_TARGET_SUPPORTED_APPLICATION_PROFILES` a list of application profiles supported by a given Mbed target coming from the Mbed target default configuration file `targets.json`.

Note: All the CMake variables above are generated by mbed-tools and their values can be overridden using an application configuration file (mbed_app.json) in the same manner.

## Mbed targets CMake input file structure

### Vendor selection

Vendor selection is handled in [`targets/CMakeLists.txt`](https://github.com/ARMmbed/mbed-os/blob/master/targets/CMakeLists.txt) using a conditional statement to verify that one of the labels used by a given Mbed target matches a given partner directory. The matching directory is added to directories to build.
e.g

```
if("Cypress" IN_LIST MBED_TARGET_LABELS)
    add_subdirectory(TARGET_Cypress)   
endif()
```
Add an `elseif` conditional statement to add a vendor directory.

### MCU family targets

`targets/TARGET_<VENDOR_NAME>` usually contains different MCU or Mbed target families. The structure of the vendor directory is up to the vendor but it is preferable that it has logical separations.
For example, the content of `targets/TARGET_Cypress/TARGET_PSOC6` can be listed as follows:

```
if("SCL" IN_LIST MBED_TARGET_LABELS)
    add_subdirectory(COMPONENT_SCL EXCLUDE_FROM_ALL)
endif()

if("WHD" IN_LIST MBED_TARGET_LABELS)
    add_subdirectory(COMPONENT_WHD EXCLUDE_FROM_ALL)
    add_subdirectory(common/COMPONENT_WHD EXCLUDE_FROM_ALL)
endif()

if("CY8CKIT064B0S2_4343W" IN_LIST MBED_TARGET_LABELS)
    add_subdirectory(TARGET_CY8CKIT064B0S2_4343W)
elseif("CY8CKIT_062S2_43012" IN_LIST MBED_TARGET_LABELS)
    add_subdirectory(TARGET_CY8CKIT_062S2_43012)
...
endif()

# Add the include directories accessible from this directory that are not specific to an MCU family or Mbed target
target_include_directories(mbed-core
    INTERFACE
        ...
)

# Add the source files accessible from this directory that are not specific to an MCU family or Mbed target
target_sources(mbed-core
    INTERFACE
        ...
)
```

## Add target's CMakeLists.txt

Add `CMakeLists.txt` files to the top level directory of a given vendor directory. List all files found in the directory in this CMake input source file, adding additional CMake input source file if it is MCU or Mbed target specific and has a great number of files which will make the top level `CMakeLists.txt` too complex. Think when you decide to create functions in a computer software code to remove complexity.

See [`targets/TARGET_Cypress/CMakeLists.txt`](https://github.com/ARMmbed/mbed-os/blob/master/targets/TARGET_Cypress/CMakeLists.txt) for examples.

### Add your sources and includes

A whole directory can be added to the build using `add_subdirectory()` if it is specific to an MCU family (or Mbed target) and has a complex structure containing more directories and files. Otherwise simply list the files contained in the directory.
See an example below:

```
if("<VENDOR_MCU_VARIANT>" IN_LIST MBED_TARGET_LABELS)
    add_subdirectory(TARGET_<VENDOR_MCU_VARIANT>)
endif()

target_include_directories(mbed-core
    INTERFACE
        .
        subdirectory
)

target_sources(mbed-core
    INTERFACE
        file1.c

        subdirectory/file2.c
)
```

Sources are listed using CMake's `target_sources()` function and added to the `mbed-core` CMake target as shown above. Header files are not explicitly listed, the directory where they can be found is listed instead. This is also shown above.


### Linker script file

A global CMake property named `MBED_TARGET_LINKER_FILE` must be set for each linker file. This linker file must be listed with its absolute path, this is achieved by adding the sub-path obtained by the CMake variable `${CMAKE_CURRENT_SOURCE_DIR}`.
e.g

``` 
if(${MBED_TOOLCHAIN} STREQUAL "ARM")
    set(LINKER_FILE relative/path/to/TOOLCHAIN_ARM_STD/linker_file.sct)
elseif(${MBED_TOOLCHAIN} STREQUAL "GCC_ARM")
    set(LINKER_FILE relative/path/to/TOOLCHAIN_GCC_ARM/linker_file.ld)
endif()

set_property(GLOBAL PROPERTY MBED_TARGET_LINKER_FILE ${CMAKE_CURRENT_SOURCE_DIR}/${LINKER_FILE})
```

#### ARMClang linker file

The shebang in the ARM toolchain linker file, also known as scatter file, needs to update the interpreter program from `armcc` to `armclang` and pass it different optional arguments.
Replace `armcc -E` with `#! armclang -E --target=arm-arm-none-eabi -x c -mcpu=<CORE_TYPE_FLAG>` where <CORE_TYPE_FLAG> is the MCU core type for a given Mbed target. Once you have determined which MCU core your Mbed target is based on, head to [tools/cmake/cores/](https://github.com/ARMmbed/mbed-os/tree/master/tools/cmake/cores) and open the CMake module your Mbed target is based on and look what the `-mcpu` is set to.

### Adding pre-compiled target libraries

Pre-compiled libraries and object files are listed using CMake's `target_link_libraries()` function with an absolute path of the file added.
e.g

```
target_link_libraries(mbed-core
    INTERFACE
        ${CMAKE_CURRENT_SOURCE_DIR}/libprecompiled.ar
        ${CMAKE_CURRENT_SOURCE_DIR}/file_object.o
)
```