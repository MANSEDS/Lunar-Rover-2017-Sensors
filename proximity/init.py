# inertial/run.py
# Created by Ethan Ramsay, 2017
# Contributors:
#   Ethan Ramsay
#   Matthew Marshall
#
# This file initiailises the proximity sensors.
# The proximity sensors are digital and of two classes: 5cm trigger and 10cm trigger distances.

from datetime import datetime
import os
import sys
import time

import RPi.GPIO as GPIO

sys.path.insert(0, "../../Robotics/Motor_brake.py")

# Edit these as necessary for changing pin locations.
NEAR_PINS = [0, 0, 0]
FAR_PINS = [0, 0, 0]

num = 0

def handle_5cm():
    global num
    motor_brake()
    with open("/var/www/html/proximity.dat", "a+") as handle:
        handle.write("{} {} {}", num, 1, datetime.now())
    num += 1

def handle_10cm():
    global num
    with open("/var/www/html/proximity.dat", "a+") as handle:
        handle.write("{} {} {}", num, 2, datetime.now())
    num += 1

# This must be ran in a process that will not be killed as the event detection handles only exist as long as this script does.
def init():
    global num

    if os.path.isfile("/var/www/html/proximity.dat"):
        with open("/var/www/html/proximity.dat", "r") as handle:
            lines = handle.readlines()
            num = int(lines[-1].split()[0]) + 1

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(NEAR_PINS, GPIO.IN)
    GPIO.setup(FAR_PINS,  GPIO.IN)

    GPIO.add_event_detect(NEAR_PINS[0], GPIO.FALLING, callback=handle_5cm)
    GPIO.add_event_detect(NEAR_PINS[1], GPIO.FALLING, callback=handle_5cm)
    GPIO.add_event_detect(NEAR_PINS[2], GPIO.FALLING, callback=handle_5cm)
    GPIO.add_event_detect(FAR_PINS[0], GPIO.FALLING, callback=handle_10cm)
    GPIO.add_event_detect(FAR_PINS[1], GPIO.FALLING, callback=handle_10cm)
    GPIO.add_event_detect(FAR_PINS[2], GPIO.FALLING, callback=handle_10cm)

if __name__ == "__main__":
    init()

    # For running this file as an executable, just infinite loop to keep it going.
    while True:
        time.sleep(1)
