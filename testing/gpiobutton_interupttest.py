# FROM:
# http://www.netzmafia.de/skripten/hardware/RasPi/RasPi_GPIO_int.html
# https://raspberrypi.stackexchange.com/questions/63512/how-can-i-detect-how-long-a-button-is-pressed

import RPi.GPIO as GPIO
import time

import shlex
from subprocess import Popen
from subprocess import run

# Button-Variable, global
buttonStatus = 0

# Pinreferenz waehlen
GPIO.setmode(GPIO.BCM)

# GPIO 18 (Pin 12) als Input definieren und Pullup-Widerstand aktivieren
GPIO.setup(24, GPIO.IN, pull_up_down = GPIO.PUD_UP)

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
    pscmd = shlex.split("sudo halt")
    run(pscmd)

def startap():
    print("gpiobutton: executing switchap.sh ap")
    pscmd = shlex.split("sudo /home/pi/zerocam/script/switchap.sh ap")
    run(pscmd)


GPIO.add_event_detect(24, GPIO.FALLING, callback=myInterrupt, bouncetime=500)


# Endlosschleife, bis Strg-C gedrueckt wird
try:
  input("Waiting for GPIO Interrupt event")
except KeyboardInterrupt:
  GPIO.cleanup()

