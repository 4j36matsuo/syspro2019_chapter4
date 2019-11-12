import time
import RPi.GPIO as GPIO

def setservo(range):
	if -90<=range<=90:
		duty=2.5+(range+90)*(12.0-2.5)/180
		servo.ChangeDutyCycle(duty)


GPIO.setmode(GPIO.BCM)
GPIO.setup(2, GPIO.OUT)
servo = GPIO.PWM(2, 50)
servo.start(0.0)


for i in range(5):
	setservo(-90)
	time.sleep(1.0)
	setservo(45)
	time.sleep(1.0)
	setservo(0)
	time.sleep(1.0)
	setservo(-45)
	time.sleep(1.0)
	setservo(90)
	time.sleep(1.0)
