from gpiozero import LED
from bluedot import BlueDot
from adxl345 import ADXL345
import datetime
import adxl345
import time
import csv
import os

accel.setRange(adxl345.RANGE_4G) #sets the maximum to 4G

led1 = LED(18)
led2 = LED(17)

def blink():
 for i in xrange(3):
   led1.on()
   time.sleep(1)
   led1.off()
   time.sleep(1)

def millisec():
  nowTime = datetime.datetime.now()
  ms = nowTime-startTime
  ms = int(ms.total_seconds()*1000)

def gravity(): #gets the readings and the number of ms elapsed, puts them in a csv file
  timestamp = time.strftime("%H:%M:%S")
  startTime = datetime.datetime.now()
  for i in xrange(600):
    led1.on()
    axes = accel.getAxes(True)
    nowTime = datetime.datetime.now()
    ms = int((nowTime-startTime).total_seconds()*1000)
    x = axes['x']
    y = axes['y']
    z = axes['z']
    print(ms,x,y,z)
    time.sleep(0.1)
    led1.off()
    with open('/home/pi/'+timestamp+'templog.csv','a') as csvfile:
      csvwriter = csv.writer(csvfile,delimiter=',',
      quotechar='|', quoting=csv.QUOTE_MINIMAL)
      csvwriter.writerow([ms,x,y,z])

blink() #blink LED1 3 times
bd = BlueDot()
bd.wait_for_press()
gravity()
led2.on()
time.sleep(5)
led2.off()