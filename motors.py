import RPi.GPIO as GPIO
from time import sleep
from random import randint
from setup import get_from_firebase

servo_pin = 11

GPIO.setmode(GPIO.BOARD)
GPIO.setup(servo_pin, GPIO.OUT)

pwm = GPIO.PWM(servo_pin, 50)
pwm.start(0)


def set_angle(angle):
    duty = angle / 18 + 3

    GPIO.output(servo_pin, True)
    pwm.ChangeDutyCycle(duty)
    sleep(1)
    GPIO.output(servo_pin, False)
    pwm.ChangeDutyCycle(duty)


while True:
    objects = get_from_firebase()
    angle = objects['angle']

    sleep(1)
    set_angle(angle)

pwm.stop()
GPIO.cleanup()
