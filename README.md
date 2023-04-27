# WiFi-connected Web Server with LCD Screen Control

This project demonstrates how to create a simple WiFi-connected web server using a microcontroller, such as the Raspberry Pi Pico, and control an LCD screen attached to it via HTTP requests.

## Hardware

- Raspberry Pi Pico
- 16x2 LCD screen
- i2c Module 
- Breadboard and wires

## Software

- MicroPython (with `network`, `socket`, `time`, and `machine` modules installed)
- `lcd_api.py` and `pico_i2c_lcd.py` libraries for controlling the LCD screen

## Usage

1. Connect the LCD screen to the Raspberry Pi Pico as per the circuit diagram provided.
2. Flash the MicroPython firmware onto the Raspberry Pi Pico.
3. Copy the `lcd_api.py` and `pico_i2c_lcd.py` files to the board.
4. Copy the `main.py` file to the board and reset it.
5. Connect to the WiFi network using the provided credentials.
6. Open a web browser and go to the IP address displayed on the console.
7. Enter the desired text in the input field and click "Submit" to display it on the LCD screen.

## Circuit Diagram

![Circuit Diagram](https://github.com/batinay1337/picoW_WebsiteLCDWriter/blob/main/circuitdiagram/raspberry-pi-pico-w-website.jpg)

## Acknowledgments

This project was inspired by and adapted from the code examples provided in the [MicroPython documentation](https://docs.micropython.org/en/latest/esp8266/tutorial/network_basics.html#http-server) and the [Adafruit Learn](https://learn.adafruit.com/micropython-hardware-i2c-devices/overview) website.
