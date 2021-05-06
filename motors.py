import RPi.GPIO as GPIO
from time import sleep
from random import randint

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)

pwm=GPIO.PWM(11, 50)
pwm.start(0)

def setAngle(angle):
    duty = angle / 18 + 3
    GPIO.output(11, True)
    pwm.ChangeDutyCycle(duty)
    sleep(1)
    GPIO.output(11, False)
    pwm.ChangeDutyCycle(duty)

while True:
    sleep(1)
    x = randint(0,180)
    setAngle(x)


pwm.stop()
GPIO.cleanup()