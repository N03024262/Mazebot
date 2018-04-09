import RPi.GPIO as GPIO
from time import sleep
 
GPIO.setmode(GPIO.BOARD)
 
Motor1A = 38
Motor1B = 36
Motor1E = 40

Motor2A = 35
Motor2B = 33
Motor2E = 37

Motor3A = 16
Motor3B = 18
Motor3E = 22

Motor4A = 21
Motor4B = 23
Motor4E = 19

GPIO.setup(Motor1A,GPIO.OUT)
GPIO.setup(Motor1B,GPIO.OUT)
GPIO.setup(Motor1E,GPIO.OUT)

GPIO.setup(Motor2A,GPIO.OUT)
GPIO.setup(Motor2B,GPIO.OUT)
GPIO.setup(Motor2E,GPIO.OUT)

GPIO.setup(Motor3A,GPIO.OUT)
GPIO.setup(Motor3B,GPIO.OUT)
GPIO.setup(Motor3E,GPIO.OUT)

GPIO.setup(Motor4A,GPIO.OUT)
GPIO.setup(Motor4B,GPIO.OUT)
GPIO.setup(Motor4E,GPIO.OUT)

print("All forward")
GPIO.output(Motor1A,GPIO.HIGH)
GPIO.output(Motor1B,GPIO.LOW)
GPIO.output(Motor1E,GPIO.HIGH)

GPIO.output(Motor2A,GPIO.HIGH)
GPIO.output(Motor2B,GPIO.LOW)
GPIO.output(Motor2E,GPIO.HIGH)

GPIO.output(Motor3A,GPIO.HIGH)
GPIO.output(Motor3B,GPIO.LOW)
GPIO.output(Motor3E,GPIO.HIGH)

GPIO.output(Motor4A,GPIO.HIGH)
GPIO.output(Motor4B,GPIO.LOW)
GPIO.output(Motor4E,GPIO.HIGH)

sleep(2)

print("Stopping")

GPIO.output(Motor1E,GPIO.LOW)
GPIO.output(Motor2E,GPIO.LOW)
GPIO.output(Motor3E,GPIO.LOW)
GPIO.output(Motor4E,GPIO.LOW)

 
GPIO.cleanup()
