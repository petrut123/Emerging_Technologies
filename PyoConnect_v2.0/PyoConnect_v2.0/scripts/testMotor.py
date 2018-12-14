from Phidget22.Phidget import *
from Phidget22.PhidgetException import *
from Phidget22.Devices.RCServo import *


try:
    ch = RCServo()	
except RuntimeError as e:
    print("Runtime Error: %s" % e.message) 
try:
  ch.setDeviceSerialNumber(393344)
except PhidgetException as e:
  print ("Phidget Exception %i: %s" % (e.code, e.details))

def onAttachHandler(e):
    print("Phidget attached!")
    
ch.setOnAttachHandler(onAttachHandler)
ch.setChannel(7)
ch.openWaitForAttachment(5000)

myPos = 35
#ch.setEngaged(True)
#ch.setAcceleration(25.0)
#ch.setTargetPosition(myPos)
