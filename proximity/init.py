# inertial/run.py
# Created by Ethan Ramsay, 2017
# Contributors:
#   Ethan Ramsay
#   Matthew Marshall
#
# This file initiailises the proximity sensors.
# The proximity sensors are digital and of two classes: 5cm trigger and 10cm trigger distances.

import RPi.GPIO as GPIO
import os

# Edit these as necessary for changing pin locations.
near_pins = [0, 0, 0]
far_pins = [0, 0, 0]

num = 0

if os.path.isfile("/var/www/html/proximity.dat"):
    with open("/var/www/html/proximity.dat", "r") as handle:
        lines = handle.readlines()
        num = int(lines[-1].split()[0])


# GPIO setup
GPIO.setmode(GPIO.BCM)
GPIO.setup(near_pins, GPIO.IN)
GPIO.setup(far_pins, GPIO.IN)


def handle_5cm():
    


def handle_10cm():
    


# Main
if __name__ == "__main__":
    GPIO.add_event_detect(near_pins, GPIO.FALLING, callback=stop)
    GPIO.add_event_detect(far_pins, GPIO.FALLING, callback=warn)
    
