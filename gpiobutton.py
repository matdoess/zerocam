# FROM:
# http://www.netzmafia.de/skripten/hardware/RasPi/RasPi_GPIO_int.html
# https://raspberrypi.stackexchange.com/questions/63512/how-can-i-detect-how-long-a-button-is-pressed

import RPi.GPIO as GPIO
import time

import shlex
from subprocess import Popen
from subprocess import run

from threading import Event

# Button-Variable, global
buttonStatus = 0

# Pinreferenz waehlen
GPIO.setmode(GPIO.BCM)

# GPIO 3 (Pin 5) als Input definieren und Pullup-Widerstand aktivieren
GPIO.setup(3, GPIO.IN, pull_up_down = GPIO.PUD_UP)

def myInterrupt(channel):
    global buttonStatus
    start_time = time.time()

    while GPIO.input(channel) == 0: # Wait for the button up
        pass

    buttonTime = time.time() - start_time    # How long was the button down?

    if buttonTime >= 2:
        startap()        # long push
    elif buttonTime >= .1:      # Ignore noise
        shutdown()        # brief push

def shutdown():
    print("gpiobutton: executing sudo halt")
    GPIO.cleanup()
    pscmd = shlex.split("sudo halt")
    run(pscmd)

def startap():
    print("gpiobutton: executing switchap.sh ap")
    GPIO.cleanup()
    pscmd = shlex.split("sudo /home/pi/zerocam/script/switchap.sh ap")
    run(pscmd)

GPIO.add_event_detect(3, GPIO.FALLING, callback=myInterrupt, bouncetime=500)


# Endlosschleife, bis Strg-C gedrueckt wird
try:
    while True:
        ## 3 options for the while loop
        #time.sleep(1)
        Event().wait()
        #GPIO.wait_for_edge(3, GPIO.FALLING) #can't be used with GPIO.add_event_detect
except KeyboardInterrupt:
    GPIO.cleanup()
finally:
    GPIO.cleanup()

