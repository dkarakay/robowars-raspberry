import RPi.GPIO as GPIO
from time import sleep
from random import randint
from setup import get_from_firebase

# Servo Pin
servo_pin = 17

# L298N Pin
in1 = 22
in2 = 23
ena = 27

# GPIO Pin numaralandırma sistemini kullandık
GPIO.setmode(GPIO.BCM)

# Pinleri kontrol etmek için output olarak kullanma
GPIO.setup(servo_pin, GPIO.OUT)
GPIO.setup(in1, GPIO.OUT)
GPIO.setup(in2, GPIO.OUT)
GPIO.setup(ena, GPIO.OUT)

# Default olarak DC Motoru çalıştırma
GPIO.output(in1, GPIO.LOW)
GPIO.output(in2, GPIO.LOW)
p = GPIO.PWM(ena, 1000)
p.start(50)

# Servo'yu varsayılan olarak 0 derecede başlatma
ang = 0
pwm = GPIO.PWM(servo_pin, 50)
pwm.start(0)


def set_angle(s_ang: float):
    # Girdiğimiz açı değerine uygun dönüş sağlama
    duty = s_ang / 18 + 3

    GPIO.output(servo_pin, True)
    pwm.ChangeDutyCycle(duty)
    sleep(1)
    GPIO.output(servo_pin, False)
    pwm.ChangeDutyCycle(duty)
    print("Servo dönüyor")


def forward():
    print("İleri")
    GPIO.output(in1, GPIO.HIGH)
    GPIO.output(in2, GPIO.LOW)


def backward():
    print("Geri")
    GPIO.output(in1, GPIO.LOW)
    GPIO.output(in2, GPIO.HIGH)


def stop():
    print("Dur")
    GPIO.output(in1, GPIO.LOW)
    GPIO.output(in2, GPIO.LOW)


# Sonsuza kadar çalıştır
while True:
    # 100ms bekle
    sleep(0.1)

    # Firebase üzerinden dataları çekmek
    objects = get_from_firebase()

    angle = float(objects['angle'])
    direction = objects['direction']
    motor_state = objects['motor_state']

    # Çekilen datayı yazdırarak kontrol edin
    print(f"angle:{angle}")
    print(f"direction:{direction}")
    print(f"motor_state:{motor_state}")

    # Eğer motorlar açıksa
    if motor_state == "running":
        # İleri
        if direction == "forward":
            forward()
        # Geri
        elif direction == "backward":
            backward()
        # Dur
        else:
            stop()
        # Eğer açı değişirse
        if ang != angle:
            set_angle(angle)
            ang = angle
    # Dur
    else:
        stop()
