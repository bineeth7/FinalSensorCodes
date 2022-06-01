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
  output1 = analogInput(1) # Reading from CH1
  output = interp(output, [224, 1023], [100, 0]) #rain
  output1 = interp(output1, [270, 1023], [100, 0]) #soil
  output=str(output) #rain
  output1=str(output1) #soil
  print("Rainfall:", output) #rain
  print("Moisture:", output1) #soil
 #output=str(output) #rain
 #output1=str(output1) #soil
 #output=output + " %" #rain
 #output1=output1 + " %" #soil
  print(output)
  print(output1) #soil
  #FBConn.put('https://sensor-readings-142b2.firebaseio.com',"Moisture",output)
  #soil mositure code
# Importing modules

# import spidev # To communicate with SPI devices

# from numpy import interp  # To scale values

# from time import sleep  # To add delay

#from firebase import firebase

#FBConn=firebase.FirebaseApplication("https://sensor-readings-142b2.firebaseio.com/")

# Start SPI connection

# spi=spidev.SpiDev() # Created an object

# spi.open(0,0) 

# Read MCP3008 data
#def analogInput(channel):

#  spi.max_speed_hz = 1350000

#  adc = spi.xfer2([1,(8+channel)<<4,0])

#  data = ((adc[1]&3) << 8) + adc[2]
#  return data

# while True:

 
  #FBConn.put('https://sensor-readings-142b2.firebaseio.com',"Moisture",output)
