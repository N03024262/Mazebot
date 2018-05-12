import RPi.GPIO as GPIO
import time
from time import sleep
GPIO.setmode(GPIO.BOARD)
pin = [22, 32, 29, 31, 15, 13, 11, 7]
run = True
threshold = 0.01045 # The maximum value that can be white as opposed to black
readColors = True # When true ReadAll() will return the color values (0 = White, 1 = Black) and when False ReadAll() will return time data

# -----------

# Global values. I should change this later when I'm better with python
state = "FollowLine"
intersection = ""

MLE = 40 # Motor Left E
MLA = 38 # Motor Left A
MLB = 36 # Motor Left B

MRE = 33 # Motor Right E
MRA = 35 # Motor Right A
MRB = 37 # Motor Right B

def gpioSetup():
    print("GPIO pins set up try")
    GPIO.setup(MLE,GPIO.OUT)
    GPIO.setup(MLA,GPIO.OUT)
    GPIO.setup(MLB,GPIO.OUT)

    GPIO.setup(MRE,GPIO.OUT)
    GPIO.setup(MRA,GPIO.OUT)
    GPIO.setup(MRB,GPIO.OUT)
    print("GPIO pins set up confirm")

def forward():
    print("Motors set forward try")
    GPIO.output(MLE,GPIO.HIGH)
    GPIO.output(MLA,GPIO.HIGH)
    GPIO.output(MLB,GPIO.LOW)
    
    GPIO.output(MRE,GPIO.HIGH)
    GPIO.output(MRA,GPIO.HIGH)
    GPIO.output(MRB,GPIO.LOW)
    print("Motors set forward confirm")
    sleep(.1)
    stopAll()

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
    sleep(.1)
    stopAll()


def adjustRight():
    print("Motors set right adjust try")
    GPIO.output(MLE,GPIO.HIGH)
    GPIO.output(MLA,GPIO.HIGH)
    GPIO.output(MLB,GPIO.LOW)

    GPIO.output(MRE,GPIO.LOW)
    print("Motors set right adjust confirm")
    sleep(.1)
    stopAll()


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
    readingArray = ReadAllAccurate()
    readingString = ""
    for i in range(0,8):
        readingString = readingString + str(readingArray[i])
    print(readingString)
    printReading(readingArray)
    return readingString


# This follows the line and changes the state if it thinks it got to an intersection
def followLine():
    reading = readSensors()

    # These are for staying on the line

    # ----- Adjust cases for 1 black -----
    # Adjust left
    if reading == "10000000":
        adjustLeft()
    elif reading == "01000000":
        adjustLeft()
    elif reading == "00100000":
        adjustLeft()
    # Forward
    elif reading == "00010000":
        forward()
    elif reading == "00001000":
        forward()
    # Adjust right
    elif reading == "00000100":
        adjustRight()
    elif reading == "00000010":
        adjustRight()
    elif reading == "00000001":
        adjustRight()
    
    # ----- Adjust cases for 2 black -----
    # Adjust left
    elif reading == "11000000":
        adjustLeft()
    elif reading == "01100000":
        adjustLeft()
    elif reading == "00110000":
        adjustLeft()
    # Forward
    elif reading == "00011000":
        forward()
    # Adjust right
    elif reading == "00001100":
        adjustRight()
    elif reading == "00000110":
        adjustRight()
    elif reading == "00000011":
        adjustRight()
    
    # ----- Adjust cases for 3 black -----
    # Adjust left
    elif reading == "11100000":
        adjustLeft()
    elif reading == "01110000":
        adjustLeft()
    # Forward
    elif reading == "00111000":
        forward()
    elif reading == "00011100":
        forward()
    # Adjust right
    elif reading == "00001110":
        adjustRight()
    elif reading == "00000111":
        adjustRight()
    
    # Handles unexpected results
    else:
        stopAll()
# -----------

def ReadAll():
    
    #Set your chosen pin to an output
    GPIO.setup(pin[0], GPIO.OUT)
    GPIO.setup(pin[1], GPIO.OUT)
    GPIO.setup(pin[2], GPIO.OUT)
    GPIO.setup(pin[3], GPIO.OUT)
    GPIO.setup(pin[4], GPIO.OUT)
    GPIO.setup(pin[5], GPIO.OUT)
    GPIO.setup(pin[6], GPIO.OUT)
    GPIO.setup(pin[7], GPIO.OUT)
    
    #Drive the output high, charging the capacitor
    GPIO.output(pin[0], True)
    GPIO.output(pin[1], True)
    GPIO.output(pin[2], True)
    GPIO.output(pin[3], True)
    GPIO.output(pin[4], True)
    GPIO.output(pin[5], True)
    GPIO.output(pin[6], True)
    GPIO.output(pin[7], True)
    
    # set the start time and reset readings.
    starttime = time.time()
    reading = [99, 99, 99, 99, 99, 99, 99, 99]
    check = [False, False, False, False, False, False, False, False]
    
    #wait for the cap to charge.
    time.sleep(0.01)

    # set pin to input
    GPIO.setup(pin[0], GPIO.IN)
    GPIO.setup(pin[1], GPIO.IN)
    GPIO.setup(pin[2], GPIO.IN)
    GPIO.setup(pin[3], GPIO.IN)
    GPIO.setup(pin[4], GPIO.IN)
    GPIO.setup(pin[5], GPIO.IN)
    GPIO.setup(pin[6], GPIO.IN)
    GPIO.setup(pin[7], GPIO.IN)
    
    while (check[0] and check[1] and check[2] and check[3] and check[4] and check[5] and check[6] and check[7]) == False:
        for i in range(0,8):
            if GPIO.input(pin[i]) == False and check[i] == False:
                endtime = time.time()
                if endtime - starttime < reading[i]:
                    reading[i] = endtime - starttime
                    check[i] = True

    colors = [0, 0, 0, 0, 0, 0, 0, 0]
    for i in range(0,8):
        if reading[i] < threshold:
            colors[i] = 0
        else:
            colors[i] = 1

    
    if readColors == True:
        return colors
    else:
        return reading

def ReadAllAccurate():
    
    while readColors:
        reading1 = ReadAll()
        reading2 = ReadAll()
        reading3 = ReadAll()
        if reading1 == reading2 and reading2 == reading3:
            return reading1

    return ReadAll()

def printReading(reading):
    print("Readings:")
    for i in range(0,8):
        print("Sensor " + str(i) + " = " + str(reading[i]))

if __name__ == "__main__":
    gpioSetup()
    print("Start")
    for i in range(0,50):
        followLine()
        # reading = ReadAllAccurate()
        # printReading(reading)
    print("End")
    # printReading(ReadAllAccurate())
    # print("Start")
    # followLine()
    # sleep(3)
    # stopAll()
    # print("Stop")
    GPIO.cleanup()
