# FROM:
# http://razzpisampler.oreilly.com/ch07.html
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:
    input_state = GPIO.input(24)
    if input_state == False:
        print('Button Pressed')
        time.sleep(0.2)
