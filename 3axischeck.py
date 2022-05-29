#!/usr/bin/env python3.7

import time
import spidev
import RPi.GPIO as gpio

pin = 12

gpio.setwarnings(False) # stop warnings when the script runs multiple times
gpio.setmode(gpio.BCM)
gpio.setup(pin, gpio.OUT)

spi = spidev.SpiDev()
spi.open(0,0)
spi.mode = 3
spi.max_speed_hz = 5000000

READBIT = 0x01
WRITEBIT = 0x00

def check_adxl355(pin):
    '''gets true if DEVID_MST is 0x1D'''
    address  = 0x01 << 1 | READBIT
    gpio.output(pin, gpio.LOW)
    id_ = spi.xfer2([address ,0])
    gpio.output(pin, gpio.HIGH)
    return id_[1] == 0x1D

def configure_adxl355(pin):
    '''configure the accelerometer '''
    RANGE = 0x2C << 1 | WRITEBIT
    gpio.output(pin, gpio.LOW)
    o_ = spi.xfer2([RANGE, 0x01]) # RANGE_2G
    gpio.output(pin, gpio.HIGH)

    POWER_CTL = 0x2D << 1 | WRITEBIT
    gpio.output(pin, gpio.LOW)
    o_ = spi.xfer2([POWER_CTL, 0x06]) 
    gpio.output(pin, gpio.HIGH)

print("ADXL355 : {}".format(check_adxl355(pin)))
configure_adxl355(pin)

# read data from the ADXL355
AXIS_START = 0x08 << 1 | READBIT
while 1:
    gpio.output(pin, gpio.LOW)
    axisBytes = spi.xfer2([AXIS_START, 0, 0, 0, 0, 0, 0, 0, 0, 0])[1:] # read 9 bytes
    gpio.output(pin, gpio.HIGH)

    X = (axisBytes[0] << 16 | axisBytes[1] << 8 | axisBytes[2]) >> 4
    Y = (axisBytes[3] << 16 | axisBytes[4] << 8 | axisBytes[5]) >> 4
    Z = (axisBytes[6] << 16 | axisBytes[7] << 8 | axisBytes[8]) >> 4

    print(">> {} {} {}".format(X, Y, Z))

    time.sleep(1)