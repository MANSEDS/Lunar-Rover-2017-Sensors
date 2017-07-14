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


def run():
    init.init()

    while True:
        read.read()

if __name__ == "__main__":
    run()
