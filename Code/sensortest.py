import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)

LEDON = 21

GPIO.setup(LEDON,GPIO.OUT)


print("LED on")
GPIO.output(LEDON,GPIO.HIGH)

sleep(45)

print("LED off")
GPIO.output(LEDON,GPIO.LOW)

GPIO.cleanup()
