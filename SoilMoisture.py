# Importing modules
import spidev # To communicate with SPI devices
from numpy import interp  # To scale values
from time import sleep  # To add delay
#from firebase import firebase
#FBConn=firebase.FirebaseApplication("https://sensor-readings-142b2.firebaseio.com/")


# Start SPI connection
spi=spidev.SpiDev() # Created an object
spi.open(0,0) 

# Read MCP3008 data
def analogInput(channel):
  spi.max_speed_hz = 1350000
  adc = spi.xfer2([1,(8+channel)<<4,0])
  data = ((adc[1]&3) << 8) + adc[2]
  return data

while True:
  output = analogInput(0) # Reading from CH0
  output = interp(output, [270, 1023], [100, 0])
  output=int(output)
  print("Moisture:", output)
  output=str(output)
  output=output + " %"
  print(output)
  #FBConn.put('https://sensor-readings-142b2.firebaseio.com',"Moisture",output)