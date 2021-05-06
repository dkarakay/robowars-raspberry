import RPi.GPIO as GPIO
from time import sleep
from random import randint

GPIO.setmode(GPIO.BOARD)
GPIO.setup(12, GPIO.OUT)

pwm=GPIO.PWM(12, 50)
pwm.start(0)

def setAngle(angle):
    duty = angle / 18 + 3
    GPIO.output(12, True)
    pwm.ChangeDutyCycle(duty)
    sleep(1)
    GPIO.output(12, False)
    pwm.ChangeDutyCycle(duty)

while True:
    sleep(1)
    x = randint(0,180)
    print(x)
    setAngle(x)


pwm.stop()
GPIO.cleanup()
