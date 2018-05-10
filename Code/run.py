import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BOARD)

MLE = 40 # Motor Left E
MLA = 38 # Motor Left A
MLB = 36 # Motor Left B

MRE = 37 # Motor Right E
MRA = 35 # Motor Right A
MRB = 33 # Motor Right B

def gpioSetup():
    GPIO.setup(MLE,GPIO.OUT)
    GPIO.setup(MLA,GPIO.OUT)
    GPIO.setup(MLB,GPIO.OUT)

    GPIO.setup(MRE,GPIO.OUT)
    GPIO.setup(MRA,GPIO.OUT)
    GPIO.setup(MRB,GPIO.OUT)

def setForward():
    GPIO.output(MLE,GPIO.HIGH)
    GPIO.output(MLA,GPIO.HIGH)
    GPIO.output(MLB,GPIO.LOW)
    
    GPIO.output(MRE,GPIO.HIGH)
    GPIO.output(MRA,GPIO.HIGH)
    GPIO.output(MRB,GPIO.LOW)

def setBackward():
    GPIO.output(MLE,GPIO.HIGH)
    GPIO.output(MLA,GPIO.LOW)
    GPIO.output(MLB,GPIO.HIGH)
    
    GPIO.output(MRE,GPIO.HIGH)
    GPIO.output(MRA,GPIO.LOW)
    GPIO.output(MRB,GPIO.HIGH)


def turnRight():
    GPIO.output(MLE,GPIO.HIGH)
    GPIO.output(MLA,GPIO.HIGH)
    GPIO.output(MLB,GPIO.LOW)
    
    GPIO.output(MRE,GPIO.HIGH)
    GPIO.output(MRA,GPIO.LOW)
    GPIO.output(MRB,GPIO.HIGH)

def turnLeft():
    GPIO.output(MLE,GPIO.HIGH)
    GPIO.output(MLA,GPIO.LOW)
    GPIO.output(MLB,GPIO.HIGH)
    
    GPIO.output(MRE,GPIO.HIGH)
    GPIO.output(MRA,GPIO.HIGH)
    GPIO.output(MRB,GPIO.LOW)


def stopAll():
    GPIO.output(MLE,GPIO.LOW)
    GPIO.output(MRE,GPIO.LOW)

while True:
    gpioSetup()

    while True:
        setForward()
        sleep(2)
        turnRight()
        sleep(2)
        turnLeft()
        sleep(2)
        setBackward()
        sleep(2)
        stopAll()
        sleep(2)
    
    GPIO.cleanup()
