# Importing modules
import spidev # To communicate with SPI devices
from numpy import interp  # To scale values
#from time import sleep  # To add delay
import time
#ML training
from sklearn import svm
from sklearn.svm import SVC
import pandas as pd
import requests
import json

def ml(values):
    data = pd.read_csv('test.csv')
    x=data.drop(columns=('status'))
    y=data['status']
    clf = svm.SVC()
    clf.fit(x,y)
    p = clf.predict([values])
    print("called")
    return(p)
    
# from firebase import firebase
# FBConn=firebase.FirebaseApplication("https://console.firebase.google.com/u/2/project/raspberrypi-ade35/database/raspberrypi-ade35-default-rtdb/data/~2F/")
# # Start SPI connection
spi=spidev.SpiDev() # Created an object
spi.open(0,0) 
# Read MCP3008 data
def analogInput(channel):
  spi.max_speed_hz = 1350000
  adc = spi.xfer2([1,(8+channel)<<4,0])
  data = ((adc[1]&3) << 8) + adc[2]
  return data
while True:
  output = analogInput(0) # Reading from CH0 rainfall
  output1 = 0 #analogInput(1) # Reading from CH1 vibration
  output2 = analogInput(2) # Reading from CH2 moisture
  output = interp(output, [224, 1023], [100, 0]) #rain
  output1 = interp(output1, [0, 0], [0, 0]) #vibration
  output2 = interp(output2, [270, 1023], [100, 0]) #soil
  output=str(output) #rain
  output1=str(output1) #vibration
  output2=str(output2) #soil
  print("Rainfall:", output) #rain
  print("Vibration:",output1) #vibration
  print("Moisture:", output2) #soil
  status = ml([output, output1, output2])
  print(status)
  url = "https://earthq1.herokuapp.com/api/v0/Data/"

  payload = json.dump({
    "rainfall": output,
    "vibration": output1,
    "moisture": output2,
    "status": status
  })
  headers = {
    'Content-Type': 'application/json'
  }

  response = requests.request("POST", url, headers=headers, data=payload)

  time.sleep(0)
