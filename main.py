import RPi.GPIO as GPIO
from time import sleep

in1 = 24
in2 = 23
ena = 25
in3 = 27
in4 = 22
enb = 17

GPIO.setmode(GPIO.BCM)

GPIO.setup(in1,GPIO.OUT)
GPIO.setup(in2,GPIO.OUT)
GPIO.setup(ena,GPIO.OUT)
GPIO.output(in1,GPIO.LOW)
GPIO.output(in2,GPIO.LOW)

GPIO.setup(in3,GPIO.OUT)
GPIO.setup(in4,GPIO.OUT)
GPIO.setup(enb,GPIO.OUT)
GPIO.output(in3,GPIO.LOW)
GPIO.output(in4,GPIO.LOW)

p = GPIO.PWM(ena,1000)
p2 = GPIO.PWM(enb,1000)


p.start(0)
p2.start(0)

print(" s: stop\n f: forward\n b: backward\n l: low\n m: medium\n h: high\n e: exit\n")

try:
    while True:
        x = input()

        if x == 's':
            print("stop")
            GPIO.output(in1,GPIO.LOW)
            GPIO.output(in2,GPIO.LOW)
            GPIO.output(in3,GPIO.LOW)
            GPIO.output(in4,GPIO.LOW)
        elif x == 'f':
            print("forward")
            GPIO.output(in1,GPIO.HIGH)
            GPIO.output(in2,GPIO.LOW)
            GPIO.output(in3,GPIO.HIGH)
            GPIO.output(in4,GPIO.LOW)
        elif x == 'b':
            print("backward")
            GPIO.output(in1,GPIO.LOW)
            GPIO.output(in2,GPIO.HIGH)
            GPIO.output(in3,GPIO.LOW)
            GPIO.output(in4,GPIO.HIGH)
        elif x == 'l':
            print("low")
            p.ChangeDutyCycle(40)
            p2.ChangeDutyCycle(40)
        elif x == 'm':
            print("medium")
            p.ChangeDutyCycle(75)
            p2.ChangeDutyCycle(75)
        elif x == 'h':
            print("high")
            p.ChangeDutyCycle(100)
            p2.ChangeDutyCycle(100)
        elif x == 'q':
            GPIO.cleanup()
            print("GPIO Clean up")
            break

except KeyboardInterrupt:
    GPIO.cleanup()
    print("GPIO Clean up")
    p.stop()
    p2.stop()
