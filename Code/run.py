import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)

MLE = 40 # Motor Left E
MLA = 38 # Motor Left A
MLB = 36 # Motor Left B

MRE = 37 # Motor Right E
MRA = 35 # Motor Right A
MRB = 33 # Motor Right B

def gpioSetup():
    print("GPIO pins set up try")
    GPIO.setup(MLE,GPIO.OUT)
    GPIO.setup(MLA,GPIO.OUT)
    GPIO.setup(MLB,GPIO.OUT)

    GPIO.setup(MRE,GPIO.OUT)
    GPIO.setup(MRA,GPIO.OUT)
    GPIO.setup(MRB,GPIO.OUT)
    print("GPIO pins set up confirm")

def setForward():
    print("Motors set forward try")
    GPIO.output(MLE,GPIO.HIGH)
    GPIO.output(MLA,GPIO.HIGH)
    GPIO.output(MLB,GPIO.LOW)
    
    GPIO.output(MRE,GPIO.HIGH)
    GPIO.output(MRA,GPIO.HIGH)
    GPIO.output(MRB,GPIO.LOW)
    print("Motors set forward confirm")

def setBackward():
    print("Motors set backward try")
    GPIO.output(MLE,GPIO.HIGH)
    GPIO.output(MLA,GPIO.LOW)
    GPIO.output(MLB,GPIO.HIGH)
    
    GPIO.output(MRE,GPIO.HIGH)
    GPIO.output(MRA,GPIO.LOW)
    GPIO.output(MRB,GPIO.HIGH)
    print("Motors set backward confirm")

    
def adjustLeft():
    print("Motors set left adjust try")
    GPIO.output(MLE,GPIO.LOW)
    
    GPIO.output(MRE,GPIO.HIGH)
    GPIO.output(MRA,GPIO.HIGH)
    GPIO.output(MRB,GPIO.LOW)
    print("Motors set left adjust confirm")


def adjustRight():
    print("Motors set right adjust try")
    GPIO.output(MLE,GPIO.HIGH)
    GPIO.output(MLA,GPIO.HIGH)
    GPIO.output(MLB,GPIO.LOW)

    GPIO.output(MRE,GPIO.LOW)
    print("Motors set right adjust confirm")


def turnRight():
    print("Motors set right turn try")
    GPIO.output(MLE,GPIO.HIGH)
    GPIO.output(MLA,GPIO.HIGH)
    GPIO.output(MLB,GPIO.LOW)
    
    GPIO.output(MRE,GPIO.HIGH)
    GPIO.output(MRA,GPIO.LOW)
    GPIO.output(MRB,GPIO.HIGH)
    print("Motors set right turn confirm")


def stopAll():
    print("Motors set stop try")
    GPIO.output(MLE,GPIO.LOW)
    GPIO.output(MRE,GPIO.LOW)
    print("Motors set stop confirm")

def readSensors():
    reading = raw_input("Enter sensor bar reading:")
    return reading

def followLine():
    reading = readSensors()

    if reading = "10000000"
        adjustLeft()
    else if reading = "11000000"
        adjustLeft()
    else if reading = "01100000"
        adjustLeft()
    else if reading = "00110000"
        adjustLeft()
    else if reading = "00011000"
        setForward()
    else if reading = "00001100"
        adjustRight()
    else if reading = "00000110"
        adjustRight()
    else if reading = "00000011"
        adjustRight()
    else if reading = "00000001"
        adjustRight()


if __name__ == "__main__":
    starttime = time.time()
    while (time.time() - starttime) > 10:
        followLine()
    GPIO.cleanup()
    

