# FROM:
# http://www.netzmafia.de/skripten/hardware/RasPi/RasPi_GPIO_int.html
# https://raspberrypi.stackexchange.com/questions/63512/how-can-i-detect-how-long-a-button-is-pressed

import RPi.GPIO as GPIO
import time

# Zaehler-Variable, global
Counter = 0
Tic = 0
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


    if buttonTime >= 4:
        buttonStatus = 3        # 3= really long push
    elif buttonTime >= 2:
        buttonStatus = 2        # 2= Long push
    elif buttonTime >= .1:      # Ignore noise
        buttonStatus = 1        # 1= brief push

    buttonAction(buttonStatus)

def buttonAction(buttonActionStatus):
    if buttonActionStatus == 1:
        print("Button Short")
    elif buttonActionStatus == 2:
        print("Button Long")
    elif buttonActionStatus == 3:
        print("Button Very Long")

GPIO.add_event_detect(24, GPIO.FALLING, callback=myInterrupt, bouncetime=500)


# Endlosschleife, bis Strg-C gedrueckt wird
try:
  while True:
      pass
    # nix Sinnvolles tun
    # Tic = Tic + 1
    # print "Tic %d" % Tic
    # time.sleep(1)
except KeyboardInterrupt:
  GPIO.cleanup()
  print "\nBye"
