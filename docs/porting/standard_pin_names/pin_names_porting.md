# Standard Pin Names

This porting guide aims to help vendors to comply with the new pin naming guidelines.

There is a set of generic guidelines that apply to all boards, and further sets of guidelines that additionally apply to boards that have certain compatible connectors.

## Generic Pin Names

The generic guidelines currently define rules for the naming of LED pins, button pins and UART pins. In summary, the rules are:
* LED pins are defined as `LEDx` (e.g. `LED0`, `LED1`)
* Button pins are defined as `BUTTONx` (e.g. `BUTTON0`, `BUTTON1`)
* UART pins for console communication with host are defined as `CONSOLE_TX` and `CONSOLE_RX`
* Pin aliases are allowed (e.g. `#define RED_LED LED1`)
* Pin definitions must be a `#define`, not an `enum`
* A physical MCU pin can be assigned to no more than one LED, button or UART pin definition
* A pin cannot be assigned to itself
* A pin cannot be defined as `NC` (not connected)

### Definition of LEDs

Only add LEDs that are available on the board. This is an example on how to define LEDs in PinNames.h:

    // Px_xx relates to the processor pin connected to the LED
    #define LED1 Px_xx  // LED1
    #define LED2 Px_xx  // LED2
    #define LED3 Px_xx  // LED3
    #define LED4 Px_xx  // LED4
    .  
    .  
    #define LEDN Px_xx  // LEDN

### Definition of buttons

Only add buttons that are available on the board. This is an example on how to define buttons in PinNames.h:

    // Px_xx relates to the processor pin connected to the button  
    #define BUTTON1 Px_xx  // BUTTON1
    #define BUTTON2 Px_xx  // BUTTON2
    #define BUTTON3 Px_xx  // BUTTON3
    #define BUTTON4 Px_xx  // BUTTON4
    .  
    .  
    #define BUTTONN Px_xx  // BUTTONN
### Definition of UART pins

This is an example on how to define UART names in PinNames.h:

    typedef enum {
    ...
    // Px_xx relates to the processor pin connected to the UART
    CONSOLE_TX = Px_xx,
    CONSOLE_RX = Px_xx,
    ...
    } PinName;

### Non-valid definitions

If either LEDs or buttons are not available, they should not be defined.
This allows for unavailable LEDs or BUTTONs to be caught in Mbed OS allowing the corresponding errors to be generated.
   
    #define LED1 PB_0  // LED1 is valid
    #define LED2 LED1  // Not valid as it's duplicate and LED2 does not exist on the board
    #define LED3 PB_0  // Not valid as it's duplicate and LED3 does not exist on the board
    #define LED4 NC    // Not valid definition as LED4 does not exist

    #define BUTTON1 PB_1    // BUTTON1 is valid
    #define BUTTON2 BUTTON1 // Not valid as it's duplicate and BUTTON2 does not exist on the board
    #define BUTTON3 PB_1    // Not valid as it's duplicate and BUTTON3 does not exist on the board
    #define BUTTON4 NC      // Not valid as BUTTON4 does not exist

## Arduino Uno Pin Names
The Arduino Uno guidelines currently define rules for the naming of the Arduino Uno connector pins, the functionality that each pin must support and the definition of Arduino Uno pin aliases. In summary, rules that apply to all Arduino pins are:
* All ARDUINO_UNO_XXX pins are defined
* A pin cannot be assigned to itself
* A pin cannot be defined as `NC` (not connected)

In Arduino Uno compliant development boards, the `ARDUINO_UNO` name should be defined as a supported form factor in targets.json file:

    "supported_form_factors": [
            "ARDUINO_UNO"
        ],

### Digital and Analog pins
* Pins must be defined in a `PinName` enum
* Digital pins must be defined as `ARDUINO_UNO_Dxx`
* Analog pins must be defined as `ARDUINO_UNO_Ax`
* Analog pins must provide ADC functionality
* A physical MCU pin can be assigned to no more than one Arduino Uno pin

The Arduino Uno (Rev3) form factor for Mbed boards must support and define both D0-D15 pins for digital GPIO and A0-A5 pins for analog input as part of the default standard. These pins should be defined in PinNames.h file within a PinName enum. The prefix `ARDUINO_UNO_` distinguishes these pins from pins defined for other custom or common connectors that may have similar pin names. 

The analog input signals in the Arduino Uno connector must be supported on at least the Ax pins.

    #ifdef TARGET_FF_ARDUINO_UNO
    // Arduino Uno (Rev3) pins
    // Px_xx relates to the processor pin connected to the Arduino Uno (Rev3) connector pin
    ARDUINO_UNO_D0 = Px_xx,
    ARDUINO_UNO_D1 = Px_xx,
    ARDUINO_UNO_D2 = Px_xx,
    ARDUINO_UNO_D3 = Px_xx,
    ARDUINO_UNO_D4 = Px_xx,
    ARDUINO_UNO_D5 = Px_xx,
    ARDUINO_UNO_D6 = Px_xx,
    ARDUINO_UNO_D7 = Px_xx,
    ARDUINO_UNO_D8 = Px_xx,
    ARDUINO_UNO_D9 = Px_xx,
    ARDUINO_UNO_D10 = Px_xx,
    ARDUINO_UNO_D11 = Px_xx,
    ARDUINO_UNO_D12 = Px_xx,
    ARDUINO_UNO_D13 = Px_xx,
    ARDUINO_UNO_D14 = Px_xx,
    ARDUINO_UNO_D15 = Px_xx,

    ARDUINO_UNO_A0 = Px_xx,
    ARDUINO_UNO_A1 = Px_xx,
    ARDUINO_UNO_A2 = Px_xx,
    ARDUINO_UNO_A3 = Px_xx,
    ARDUINO_UNO_A4 = Px_xx,
    ARDUINO_UNO_A5 = Px_xx,
    #endif // TARGET_FF_ARDUINO_UNO

If the development board has the Arduino Uno connector in hardware, but does not comply with the Arduino Uno standard, whether it be with alternate functionality pins or non connected pins, the board should not be defined as Arduino Uno compliant and `ARDUINO_UNO` should not be added as a supported form factor in targets.json. Note this may result in a warning being generated at compile time to inform the user.

### I2C, SPI and UART pins
* Pins D14, D15 must provide I2C functionality (SDA, SCL)
* Pins D10, D11, D12, D13 must provide SPI functionality (CS, MOSI, MISO, SCK)
* Pins D0, D1 must provide UART functionality (RX, TX) 

All I2C, SPI and UART pin name alias definitions for the Arduino Uno (Rev3) connector pins is defined in the Mbed OS HAL (hal/include/hal/ArduinoUnoAliases.h) and are common to all Arduino Uno compliant targets:

    #ifdef TARGET_FF_ARDUINO_UNO
    // Arduino Uno I2C signals aliases
    #define ARDUINO_UNO_I2C_SDA ARDUINO_UNO_D14
    #define ARDUINO_UNO_I2C_SCL ARDUINO_UNO_D15

    // Arduino Uno SPI signals aliases
    #define ARDUINO_UNO_SPI_CS   ARDUINO_UNO_D10
    #define ARDUINO_UNO_SPI_MOSI ARDUINO_UNO_D11
    #define ARDUINO_UNO_SPI_MISO ARDUINO_UNO_D12
    #define ARDUINO_UNO_SPI_SCK  ARDUINO_UNO_D13

    // Arduino Uno UART signals aliases
    #define ARDUINO_UNO_UART_TX ARDUINO_UNO_D1
    #define ARDUINO_UNO_UART_RX ARDUINO_UNO_D0
    #endif // TARGET_FF_ARDUINO_UNO

### Other pins
* Mbed boards may provide PWM and timer functionality on certain Dx pins
* Applications cannot assume consistent availability of PWM and timer pins across Mbed boards
* The reset pin must be wired correctly in hardware but is not required to be defined in `PinNames.h`

In the Arduino Uno standard there are only 6 PWM and timers available on pins D3, D5, D6, D9, D10 and D11.
Mbed boards may support the usage of PWM and timers functions in some Dx pinnames. Although this is recomended as per the Arduino Uno standard, it's not a mandatory as requirement to be compliant with the Arduino Uno standard for Mbed boards.

Note this might be one of the main differencess accross Mbed boards and therefore the application should not assume the same behaviour for PWM and Timers for them.

The Reset signal in the Arduino Uno header is a bidirectional reset that will put both a connected Arduino Uno shield and the Mbed board into a reset state. There is a hardware requirement to wire this signal correctly; however there is no need to define the Reset signal in the BSP for the Mbed board.

The Vin signal is defined in the Arduino Uno standard and should be implemented between 7V to 12V. In some cases this signal may be implemented as a bi-directional power supply.
A warning should be included in the Mbed platform's website if it isn't implemented in the correct voltage range.
Note if a Partner or developer designs an Arduino Uno shield and expects 7V-12V on the Vin, it will have power issues with a controller board supplying less then 7V and will likely cause the Arduino Uno shield to not power up correctly

## Target markers

PinNames.h files must include a comment that lists the names of the targets (as they appear in targets.json) the file is linked to. This marker comment must be placed somewhere in the file and follow the below format:

```
/* MBED TARGET LIST: K64F, K66F */

/* MBED TARGET LIST: DISCO_L475VG_IOT01A */
```

## Compliance Testing

After you have updated the `PinNames.h` files of your targets according to the above guidelines, you can check the files for compliance using two different methods.
* Python script: performs syntax checks on pin definitions according pre-defined coding style rules
* Greentea: performs build and run time checks on Mbed boards to make sure pins names and integration with Drivers work as expected

### Using pinvalidate<span>.py</span> Python script
This is a Python script which you can use to quickly check the compliance of `PinNames.h` files with the above rules.

The script can be found in `mbed-os/hal/tests/TESTS/pin_names`.

The script has a number of options which you can see in the help output (`pinvalidate.py -h`).

You can validate `PinNames.h` files either by passing the path to the files with the `-p` flag, or by passing the name of the targets with the `-t` flag and letting the script automatically discover the corresponding `PinNames.h` file.

The following examples would validate the same file:
`pinvalidate.py -t L4S5I`
`pinvalidate.py -p targets/TARGET_STM/TARGET_STM32L4/TARGET_STM32L4S5xI/TARGET_B_L4S5I_IOT01A/PinNames.h`

Multiple targets or paths can be separated by comma:
`pinvalidate.py -t L475,L4S5I,K22F,NUCLEO_F411RE`

You can also pass the `-a` flag, instead of `-p` or `-t`, to validate all `PinNames.h` files. The script will process every `PinNames.h` file that is discovered in the `mbed-os/targets` directory (and subdirectories).

There are currently two test suites that you can run against a `PinNames.h` file:
* The Generic Pin Names test suite (`generic`)
* The Arduino Uno Pin Names test suite (`arduino_uno`)

The tool will automatically run the appropriate test suites by reading the supported form factors from the target definition in `targets.json`. If this information is not available, the tool will only run the `generic` test suite by default.

You can manually choose which test suites to run using the `-n` flag:
`pinvalidate.py -t L475 -n generic`
`pinvalidate.py -t L475 -n generic,arduino`

The scripts supports several output formats. The default output format is `prettytext`. You can choose the output format with the `-o` flag:
`pinvalidate.py -t L4S5I -o json`
`pinvalidate.py -t L4S5I -o html`

You may also want to use the `-w` flag to write the output to a file when choosing HTML or JSON output:
`pinvalidate.py -t L4S5I -o html -w output.html`

The `prettytext` format supports four levels of detail/verbosity, selected with the usual `-v` flag:
`pinvalidate.py -t L4S5I` (level 0)
`pinvalidate.py -t L4S5I -v` (level 1)
`pinvalidate.py -t L4S5I -vvv` (level 3)
* At the default level (0), the script will output a short summary table showing a PASS/FAIL outcome for each of the validated files/targets.
* At level 1, the script will output a summary table showing a PASS/FAIL outcome for each test suite ran against a target.
* At level 2, the script will output a table showing a PASS/FAIL outcome for each test case ran against a target.
* At level 3, the script will output all of the above information, with details of each individual error.

When HTML output is chosen, the script will output the report as an interactive HTML table that you can view in a web browser. Each row is the output from one test case, with a PASS/FAIL outcome. You can view the details of any errors by expanding the last cell of the row.

JSON and HTML output always include the highest level of detail.

To verify that the target markers in PinNames.h files are valid, run `pinvalidate.py -m`.

### Using Greentea

There is also a Greentea test to facilitate runtime compliance testing on actual hardware. This test will typically be run in the final stages of the migration, after the `PinNames.h` file is already passing the `pinvalidate.py` test. The Greentea test checks that every required pin is defined and then checks that the pins support the features specified in the Arduino Uno standard by making some basic API calls. For example, for pins that are supposed to provide PWM functionality, the test case will configure them as such and then do some basic calls to generate a waveform on those pins.

After setting up your environment to be able to run Greentea tests, you can compile run the standard pin names compliance test suites:

`mbed test -t GCC_ARM -m DISCO_L475VG_IOT01A -n "*pin_names*" --compile`

`mbed test -t GCC_ARM -m DISCO_L475VG_IOT01A -n *pin_names* --run`

You can expect the following output:

```mbed test -t GCC_ARM -m DISCO_L475VG_IOT01A -n "*pin_names*" --run
mbedgt: greentea test automation tool ver. 1.8.1
mbedgt: test specification file './BUILD/tests/DISCO_L475VG_IOT01A/GCC_ARM/test_spec.json' (specified with --test-spec option)
mbedgt: using './BUILD/tests/DISCO_L475VG_IOT01A/GCC_ARM/test_spec.json' from current directory!
mbedgt: detecting connected mbed-enabled devices...
mbedgt: detected 1 device
mbedgt: processing target 'DISCO_L475VG_IOT01A' toolchain 'GCC_ARM' compatible platforms... (note: switch set to --parallel 1)
mbedgt: test case filter (specified with -n option)
	*pin_names*
	test filtered in 'hal-tests-tests-pin_names-arduino_uno'
mbedgt: running 1 test for platform 'DISCO_L475VG_IOT01A' and toolchain 'GCC_ARM'
mbedgt: mbed-host-test-runner: started
;mbedgt: checking for GCOV data...
mbedgt: test on hardware with target id: 07640221706D696D4F29FF34
mbedgt: test suite 'hal-tests-tests-pin_names-arduino_uno' ........................................... OK in 32.23 sec
	test case: 'ADC A0' .......................................................................... OK in 0.05 sec
	test case: 'ADC A1' .......................................................................... OK in 0.05 sec
	test case: 'ADC A2' .......................................................................... OK in 0.05 sec
	test case: 'ADC A3' .......................................................................... OK in 0.05 sec
	test case: 'ADC A4' .......................................................................... OK in 0.04 sec
	test case: 'ADC A5' .......................................................................... OK in 0.05 sec
	test case: 'GPIO A0' ......................................................................... OK in 0.06 sec
	test case: 'GPIO A1' ......................................................................... OK in 0.06 sec
	test case: 'GPIO A2' ......................................................................... OK in 0.05 sec
	test case: 'GPIO A3' ......................................................................... OK in 0.05 sec
	test case: 'GPIO A4' ......................................................................... OK in 0.05 sec
	test case: 'GPIO A5' ......................................................................... OK in 0.04 sec
	test case: 'GPIO D0' ......................................................................... OK in 0.05 sec
	test case: 'GPIO D1' ......................................................................... OK in 0.05 sec
	test case: 'GPIO D10' ........................................................................ OK in 0.05 sec
	test case: 'GPIO D11' ........................................................................ OK in 0.04 sec
	test case: 'GPIO D12' ........................................................................ OK in 0.05 sec
	test case: 'GPIO D13' ........................................................................ OK in 0.05 sec
	test case: 'GPIO D14' ........................................................................ OK in 0.05 sec
	test case: 'GPIO D15' ........................................................................ OK in 0.05 sec
	test case: 'GPIO D2' ......................................................................... OK in 0.05 sec
	test case: 'GPIO D3' ......................................................................... OK in 0.06 sec
	test case: 'GPIO D4' ......................................................................... OK in 0.04 sec
	test case: 'GPIO D5' ......................................................................... OK in 0.05 sec
	test case: 'GPIO D6' ......................................................................... OK in 0.05 sec
	test case: 'GPIO D7' ......................................................................... OK in 0.06 sec
	test case: 'GPIO D8' ......................................................................... OK in 0.04 sec
	test case: 'GPIO D9' ......................................................................... OK in 0.04 sec
	test case: 'I2C' ............................................................................. OK in 0.07 sec
	test case: 'PWM D10' ......................................................................... OK in 0.05 sec
	test case: 'PWM D11' ......................................................................... OK in 0.04 sec
	test case: 'PWM D3' .......................................................................... OK in 0.05 sec
	test case: 'PWM D5' .......................................................................... OK in 0.05 sec
	test case: 'PWM D6' .......................................................................... OK in 0.05 sec
	test case: 'PWM D9' .......................................................................... OK in 0.04 sec
	test case: 'SPI' ............................................................................. OK in 0.09 sec
	test case: 'UART' ............................................................................ OK in 0.07 sec
mbedgt: test case summary: 37 passes, 0 failures
mbedgt: all tests finished!
mbedgt: shuffle seed: 0.8352342017
mbedgt: test suite report:
| target                      | platform_name       | test suite                            | result | elapsed_time (sec) | copy_method |
|-----------------------------|---------------------|---------------------------------------|--------|--------------------|-------------|
| DISCO_L475VG_IOT01A-GCC_ARM | DISCO_L475VG_IOT01A | hal-tests-tests-pin_names-arduino_uno | OK     | 32.23              | default     |
mbedgt: test suite results: 1 OK
mbedgt: test case report:
| target                      | platform_name       | test suite                            | test case | passed | failed | result | elapsed_time (sec) |
|-----------------------------|---------------------|---------------------------------------|-----------|--------|--------|--------|--------------------|
| DISCO_L475VG_IOT01A-GCC_ARM | DISCO_L475VG_IOT01A | hal-tests-tests-pin_names-arduino_uno | ADC A0    | 1      | 0      | OK     | 0.05               |
| DISCO_L475VG_IOT01A-GCC_ARM | DISCO_L475VG_IOT01A | hal-tests-tests-pin_names-arduino_uno | ADC A1    | 1      | 0      | OK     | 0.05               |
| DISCO_L475VG_IOT01A-GCC_ARM | DISCO_L475VG_IOT01A | hal-tests-tests-pin_names-arduino_uno | ADC A2    | 1      | 0      | OK     | 0.05               |
| DISCO_L475VG_IOT01A-GCC_ARM | DISCO_L475VG_IOT01A | hal-tests-tests-pin_names-arduino_uno | ADC A3    | 1      | 0      | OK     | 0.05               |
| DISCO_L475VG_IOT01A-GCC_ARM | DISCO_L475VG_IOT01A | hal-tests-tests-pin_names-arduino_uno | ADC A4    | 1      | 0      | OK     | 0.04               |
| DISCO_L475VG_IOT01A-GCC_ARM | DISCO_L475VG_IOT01A | hal-tests-tests-pin_names-arduino_uno | ADC A5    | 1      | 0      | OK     | 0.05               |
| DISCO_L475VG_IOT01A-GCC_ARM | DISCO_L475VG_IOT01A | hal-tests-tests-pin_names-arduino_uno | GPIO A0   | 1      | 0      | OK     | 0.06               |
| DISCO_L475VG_IOT01A-GCC_ARM | DISCO_L475VG_IOT01A | hal-tests-tests-pin_names-arduino_uno | GPIO A1   | 1      | 0      | OK     | 0.06               |
| DISCO_L475VG_IOT01A-GCC_ARM | DISCO_L475VG_IOT01A | hal-tests-tests-pin_names-arduino_uno | GPIO A2   | 1      | 0      | OK     | 0.05               |
| DISCO_L475VG_IOT01A-GCC_ARM | DISCO_L475VG_IOT01A | hal-tests-tests-pin_names-arduino_uno | GPIO A3   | 1      | 0      | OK     | 0.05               |
| DISCO_L475VG_IOT01A-GCC_ARM | DISCO_L475VG_IOT01A | hal-tests-tests-pin_names-arduino_uno | GPIO A4   | 1      | 0      | OK     | 0.05               |
| DISCO_L475VG_IOT01A-GCC_ARM | DISCO_L475VG_IOT01A | hal-tests-tests-pin_names-arduino_uno | GPIO A5   | 1      | 0      | OK     | 0.04               |
| DISCO_L475VG_IOT01A-GCC_ARM | DISCO_L475VG_IOT01A | hal-tests-tests-pin_names-arduino_uno | GPIO D0   | 1      | 0      | OK     | 0.05               |
| DISCO_L475VG_IOT01A-GCC_ARM | DISCO_L475VG_IOT01A | hal-tests-tests-pin_names-arduino_uno | GPIO D1   | 1      | 0      | OK     | 0.05               |
| DISCO_L475VG_IOT01A-GCC_ARM | DISCO_L475VG_IOT01A | hal-tests-tests-pin_names-arduino_uno | GPIO D10  | 1      | 0      | OK     | 0.05               |
| DISCO_L475VG_IOT01A-GCC_ARM | DISCO_L475VG_IOT01A | hal-tests-tests-pin_names-arduino_uno | GPIO D11  | 1      | 0      | OK     | 0.04               |
| DISCO_L475VG_IOT01A-GCC_ARM | DISCO_L475VG_IOT01A | hal-tests-tests-pin_names-arduino_uno | GPIO D12  | 1      | 0      | OK     | 0.05               |
| DISCO_L475VG_IOT01A-GCC_ARM | DISCO_L475VG_IOT01A | hal-tests-tests-pin_names-arduino_uno | GPIO D13  | 1      | 0      | OK     | 0.05               |
| DISCO_L475VG_IOT01A-GCC_ARM | DISCO_L475VG_IOT01A | hal-tests-tests-pin_names-arduino_uno | GPIO D14  | 1      | 0      | OK     | 0.05               |
| DISCO_L475VG_IOT01A-GCC_ARM | DISCO_L475VG_IOT01A | hal-tests-tests-pin_names-arduino_uno | GPIO D15  | 1      | 0      | OK     | 0.05               |
| DISCO_L475VG_IOT01A-GCC_ARM | DISCO_L475VG_IOT01A | hal-tests-tests-pin_names-arduino_uno | GPIO D2   | 1      | 0      | OK     | 0.05               |
| DISCO_L475VG_IOT01A-GCC_ARM | DISCO_L475VG_IOT01A | hal-tests-tests-pin_names-arduino_uno | GPIO D3   | 1      | 0      | OK     | 0.06               |
| DISCO_L475VG_IOT01A-GCC_ARM | DISCO_L475VG_IOT01A | hal-tests-tests-pin_names-arduino_uno | GPIO D4   | 1      | 0      | OK     | 0.04               |
| DISCO_L475VG_IOT01A-GCC_ARM | DISCO_L475VG_IOT01A | hal-tests-tests-pin_names-arduino_uno | GPIO D5   | 1      | 0      | OK     | 0.05               |
| DISCO_L475VG_IOT01A-GCC_ARM | DISCO_L475VG_IOT01A | hal-tests-tests-pin_names-arduino_uno | GPIO D6   | 1      | 0      | OK     | 0.05               |
| DISCO_L475VG_IOT01A-GCC_ARM | DISCO_L475VG_IOT01A | hal-tests-tests-pin_names-arduino_uno | GPIO D7   | 1      | 0      | OK     | 0.06               |
| DISCO_L475VG_IOT01A-GCC_ARM | DISCO_L475VG_IOT01A | hal-tests-tests-pin_names-arduino_uno | GPIO D8   | 1      | 0      | OK     | 0.04               |
| DISCO_L475VG_IOT01A-GCC_ARM | DISCO_L475VG_IOT01A | hal-tests-tests-pin_names-arduino_uno | GPIO D9   | 1      | 0      | OK     | 0.04               |
| DISCO_L475VG_IOT01A-GCC_ARM | DISCO_L475VG_IOT01A | hal-tests-tests-pin_names-arduino_uno | I2C       | 1      | 0      | OK     | 0.07               |
| DISCO_L475VG_IOT01A-GCC_ARM | DISCO_L475VG_IOT01A | hal-tests-tests-pin_names-arduino_uno | PWM D10   | 1      | 0      | OK     | 0.05               |
| DISCO_L475VG_IOT01A-GCC_ARM | DISCO_L475VG_IOT01A | hal-tests-tests-pin_names-arduino_uno | PWM D11   | 1      | 0      | OK     | 0.04               |
| DISCO_L475VG_IOT01A-GCC_ARM | DISCO_L475VG_IOT01A | hal-tests-tests-pin_names-arduino_uno | PWM D3    | 1      | 0      | OK     | 0.05               |
| DISCO_L475VG_IOT01A-GCC_ARM | DISCO_L475VG_IOT01A | hal-tests-tests-pin_names-arduino_uno | PWM D5    | 1      | 0      | OK     | 0.05               |
| DISCO_L475VG_IOT01A-GCC_ARM | DISCO_L475VG_IOT01A | hal-tests-tests-pin_names-arduino_uno | PWM D6    | 1      | 0      | OK     | 0.05               |
| DISCO_L475VG_IOT01A-GCC_ARM | DISCO_L475VG_IOT01A | hal-tests-tests-pin_names-arduino_uno | PWM D9    | 1      | 0      | OK     | 0.04               |
| DISCO_L475VG_IOT01A-GCC_ARM | DISCO_L475VG_IOT01A | hal-tests-tests-pin_names-arduino_uno | SPI       | 1      | 0      | OK     | 0.09               |
| DISCO_L475VG_IOT01A-GCC_ARM | DISCO_L475VG_IOT01A | hal-tests-tests-pin_names-arduino_uno | UART      | 1      | 0      | OK     | 0.07               |
mbedgt: test case results: 37 OK
mbedgt: completed in 34.33 sec
```
