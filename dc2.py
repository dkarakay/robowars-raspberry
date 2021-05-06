import sys
import time
import RPi.GPIO as GPIO

mode = GPIO.getmode()

#GPIO.cleanup()

Forward = 23
Backward = 24
sleeptime = 1

GPIO.setmode(GPIO.BCM)
GPIO.setup(Forward, GPIO.OUT)
GPIO.setup(Backward, GPIO.OUT)


def forward(x):
    GPIO.output(Forward, GPIO.HIGH)
    print("Moving Forward")
    time.sleep(x)
    GPIO.output(Forward, GPIO.LOW)


def reverse(x):
    GPIO.output(Backward, GPIO.HIGH)
    print("Moving Backward")
    time.sleep(x)
    GPIO.output(Backward, GPIO.LOW)


while True:
    forward(5)
    reverse(5)
    #GPIO.cleanup()
