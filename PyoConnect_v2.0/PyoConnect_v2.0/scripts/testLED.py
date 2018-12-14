from Phidget22.Phidget import *
from Phidget22.PhidgetException import *
from Phidget22.Devices.DigitalOutput import *



try:
    LED = DigitalOutput()
except RuntimeError as e:
    print("Runtime Error: %s" % e.message) 
try:
  LED.setDeviceSerialNumber(437969)
except PhidgetException as e:
  print ("Phidget Exception %i: %s" % (e.code, e.details))

def onAttachHandler(e):
    print("Phidget attached!")
    
LED.setOnAttachHandler(onAttachHandler)
LED.setChannel(0)
LED.openWaitForAttachment(5000)
LED.setState(True)
