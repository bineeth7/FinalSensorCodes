import time
import board
import busio
import adafruit_adxl34x

i2c = busio.I2C(board.SCL, board.SDA)
accelerometer = adafruit_adxl34x.ADXL345(i2c)

while True:
    print("%f %f %f"%accelerometer.acceleration)
    time.sleep(1)

    # ADXL345 Python example 
#
# author:  Jonathan Williamson
# license: BSD, see LICENSE.txt included in this package
# 
# This is an example to show you how to use our ADXL345 Python library
# http://shop.pimoroni.com/products/adafruit-triple-axis-accelerometer

# from adxl345 import ADXL345
  
# adxl345 = ADXL345()
    
# axes = adxl345.getAxes(True)
# print "ADXL345 on address 0x%x:" % (adxl345.address)
# print "   x = %.3fG" % ( axes['x'] )
# print "   y = %.3fG" % ( axes['y'] )
# print "   z = %.3fG" % ( axes['z'] )