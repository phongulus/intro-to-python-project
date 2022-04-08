# Raspberry Pi Snake

A game of snake played on Raspberry Pi Zero's!
(This project was made for YSC2221 Introduction to Python)

<img width="300" alt="image" src="https://user-images.githubusercontent.com/70936859/162477682-a27cdc2b-f1f8-4c79-89dc-e5619e063397.png">

## Components used

- Two Raspberry Pi Zero's (RPi's for short).
- Two Maker pHAT's (https://sg.cytron.io/p-maker-phat-simplifying-raspberry-pi-for-education?r=1).
- One UnicornHat 8x8 LED matrix module (https://shop.pimoroni.com/products/unicorn-hat?variant=932565325).
- One Adafruit 128x64 OLED Bonnet (https://www.adafruit.com/product/3531).

## Communicating with the Raspberry Pi's

Each of the two RPi's has a Maker pHAT connected to it, to facilitate serial communication with a computer. We used SSH via serial throughout this project.

On a Windows system, we used MobaXTerm (https://mobaxterm.mobatek.net/). After plugging in the RPi via USB, we go to `Session` -> `Serial`, then select the serial port of the RPi and a `Speed (bps)` of 115200.

On MacOS, we go to the Terminal app and type `ls /dev/tty.*` to get the list of available serial ports. To access the RPi via serial, run `screen /dev/tty.[rpi port here] 115200`.

We now have access to the RPi terminal.

## Setting up the Raspberry Pi's

In addition to the Maker pHAT, one RPi will be connected to the 8x8 LED matrix; this will be our remote display for the snake game. The other RPi will be connected to the Adafruit Bonnet, acting as the controller. (Note: The controller RPi will also be where the game logic is computed. The other RPi's only role is to receive display data and show it on the LED matrix.)

Both RPi's must be set up in the following way:

- I2C must be enabled.
- Connect the two RPi's to the same network, either via WiFi or Ethernet.
- A static IP address for both RPi's must be set up. We followed the instructions here: https://pimylifeup.com/raspberry-pi-static-ip-address/. The chosen IP addresses are `192.168.43.200` for the receiver RPi (the one with the UnicornHat) and `192.168.43.199` for the controller RPi. If other static addresses are used, `unicorn.py` and `receive.py` must be updated accordingly.
- Make sure that Python 3.9 is installed on the RPi's, and run `pip3 install -r requirements.txt` from the project root directory.

## Running the game

1. On the receiver RPi, run `receive.py` with `sudo python receive.py`. The `sudo` is required!
2. On the controller RPi, run `snake_demo.py` with `python snake_demo.py`.
3. Enjoy!

The tests can be run by running `pytest` from the root project directory.
