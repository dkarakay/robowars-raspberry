import RPi.GPIO as GPIO
from time import sleep
from random import randint
from setup import get_from_firebase

servo_pin = 17
in1 = 24
in2 = 23
en = 25

GPIO.setmode(GPIO.BCM)
GPIO.setup(servo_pin, GPIO.OUT)
GPIO.setup(in1, GPIO.OUT)
GPIO.setup(in2, GPIO.OUT)
GPIO.setup(en, GPIO.OUT)
GPIO.output(in1, GPIO.LOW)
GPIO.output(in2, GPIO.LOW)

p = GPIO.PWM(en, 1000)
p.start(25)

pwm = GPIO.PWM(servo_pin, 50)
pwm.start(0)


def set_angle(ang: float):
    duty = ang / 18 + 3

    GPIO.output(servo_pin, True)
    pwm.ChangeDutyCycle(duty)
    sleep(1)
    GPIO.output(servo_pin, False)
    pwm.ChangeDutyCycle(duty)


def forward():
    print("forward")
    GPIO.output(in1, GPIO.HIGH)
    GPIO.output(in2, GPIO.LOW)


def backward():
    print("backward")
    GPIO.output(in1, GPIO.LOW)
    GPIO.output(in2, GPIO.HIGH)


def stop():
    print("stop")
    GPIO.output(in1, GPIO.LOW)
    GPIO.output(in2, GPIO.LOW)


while True:
    sleep(0.05)
    objects = get_from_firebase()

    angle = float(objects['angle'])
    direction = objects['direction']
    motor_state = objects['motor_state']

    print(f"angle:{angle}")
    print(f"direction:{direction}")
    print(f"motor_state:{motor_state}")

    if motor_state == "running":
        if direction == "forward":
            forward()
        elif direction == "backward":
            backward()
    else:
        stop()

    set_angle(angle)

pwm.stop()
GPIO.cleanup()
