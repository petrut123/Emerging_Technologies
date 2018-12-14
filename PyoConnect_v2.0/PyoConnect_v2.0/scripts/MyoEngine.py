from Phidget22.Phidget import *
from Phidget22.PhidgetException import *
from Phidget22.Devices.RCServo import *
from Phidget22.Devices.DigitalOutput import *


#Create an RCServo object
try:
    userMotor = RCServo()
    randomMotor = RCServo()
except RuntimeError as e:
    print("Runtime Error: %s" % e.message)
#Each object needs a serial number so that the Phidget knows what that is
try:
    userMotor.setDeviceSerialNumber(393344)
    randomMotor.setDeviceSerialNumber(393344)
except PhidgetException as e:
    print ("Phidget Exception %i: %s" % (e.code, e.details))

def onAttachHandler(e):
    print("Phidget attached!")
    
userMotor.setOnAttachHandler(onAttachHandler)
randomMotor.setOnAttachHandler(onAttachHandler)
#Set the channel (the motors need to be plugged in the same channel)
userMotor.setChannel(1)
randomMotor.setChannel(7)
#Open the channel
try:
    userMotor.openWaitForAttachment(5000)
    randomMotor.openWaitForAttachment(5000)
except PhidgetException as e:
    print("Phidget Exception %i: %s" % (e.code, e.details))

#Set both motors to a default position
randomMotor.setTargetPosition(90)
randomMotor.setEngaged(True)
userMotor.setTargetPosition(90)
userMotor.setEngaged(True)
    
#Create a led object
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
#Declare score
score = 0
command = ""
LED.setState(True)
def gameLoop(command):
    #This function gets called when a round starts and one of the players need to input a command
    global score
    if(command == "lost"):
        print("Your score is %i!" % (score - 1))
        score = 0
        userMotor.close()
        randomMotor.close()
        LED.close()
        return
    elif(command == "right"):
        randomMotor.setTargetPosition(180)
        randomMotor.setEngaged(True)
        score += 1
    elif(command == "left"):
        randomMotor.setTargetPosition(0)
        randomMotor.setEngaged(True)
        score += 1
    elif(command == "back"):
        randomMotor.setTargetPosition(90)
        randomMotor.setEngaged(True)
        score += 1
    
def onPoseEdge(pose, edge):
        global command
        #Gets called whenever the gesture is changed(Myo)
        if (pose == "waveOut") and (edge == "on"):
            gameLoop(command)
            SteerRight()
        if (pose == "waveIn") and (edge == "on"):
            gameLoop(command)
            SteerLeft()
        if (pose == "fist") and (edge == "on"):
            gameLoop("back")
            Back()
        if (pose == "doubleTap") and (edge == "on"):
            print("Start round!\n")
            command = raw_input("Introduce command \n")
            
                                 
#Stops Myo from locking itself after 3 seconds
def onUnlock():
    myo.setLockingPolicy("none")

#Moves the motor a certain amount of degrees
def SteerRight():
    userMotor.setTargetPosition(180)
    userMotor.setEngaged(True)
    
def SteerLeft():
    userMotor.setTargetPosition(0)
    userMotor.setEngaged(True)
    
def Back():
    userMotor.setTargetPosition(90)
    userMotor.setEngaged(True)