# inertial/run.py
# Created by Matthew Marshall, 2017
# Contributors:
#   Matthew Marshall
#
# This file runs the initialisation and read-in scripts for the iNEMO inertial module chip.
# This chip contains an accelerometer, a magnetometer and a barometer.

import init
import read
import os

init.init()

num = 0

if os.path.isfile("/var/www/html/inertial.dat"):
    with open("/var/www/html/inertial.dat", "r") as handle:
        lines  = handle.readlines()
        num = int(lines[-1].split()[0])

while True:
    read.read(num)
    num += 1
