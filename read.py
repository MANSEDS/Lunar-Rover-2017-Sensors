# read.py
# Created by Matthew Marshall, 2017
# Contributors:
#   Matthew Marshall
#
# This file handles acquiring and printing to stdout the data from the iNEMO inertial module chip.
# This chip contains an accelerometer, a magnetometer and a barometer.

from smbus import SMBus
from datetime import datetime

def twos_compliment_combine(msb, lsb):
    twos_compliment = 256 * msb + lsb
    if twos_compliment >= 32767:
        return twos_compliment - 65536
    return twos_compliment

def read():
    smbus = SMBus(1)

    # Specify chip location info.
    CHIP_LOC = 0b1101011

    # List of registers for data to be read off chip.
    # Accelerometer
    ACC_X_LSB = 0x28
    ACC_X_MSB = 0x29
    ACC_Y_LSB = 0x2A
    ACC_Y_MSB = 0x2B
    ACC_Z_LSB = 0x2C
    ACC_Z_MSB = 0x2D
    # Gyroscope
    GYR_X_LSB = 0x22
    GYR_X_MSB = 0x23
    GYR_Y_LSB = 0x24
    GYR_Y_MSB = 0x25
    GYR_Z_LSB = 0x26
    GYR_Z_MSB = 0x27
    # Temperature Gauge
    TEMP_LSB = 0x20
    TEMP_MSB = 0x21

    # Read in magnetic field data.
    acc_x = twos_compliment_combine(smbus.read_byte_data(CHIP_LOC, ACC_X_MSB), smbus.read_byte_data(CHIP_LOC, ACC_X_LSB))
    acc_y = twos_compliment_combine(smbus.read_byte_data(CHIP_LOC, ACC_Y_MSB), smbus.read_byte_data(CHIP_LOC, ACC_Y_LSB))
    acc_z = twos_compliment_combine(smbus.read_byte_data(CHIP_LOC, ACC_Z_MSB), smbus.read_byte_data(CHIP_LOC, ACC_Z_LSB))

    # Read in acceleration data.
    gyr_x = twos_compliment_combine(smbus.read_byte_data(CHIP_LOC, GYR_X_MSB), smbus.read_byte_data(CHIP_LOC, GYR_X_LSB))
    gyr_y = twos_compliment_combine(smbus.read_byte_data(CHIP_LOC, GYR_Y_MSB), smbus.read_byte_data(CHIP_LOC, GYR_Y_LSB))
    gyr_z = twos_compliment_combine(smbus.read_byte_data(CHIP_LOC, GYR_Z_MSB), smbus.read_byte_data(CHIP_LOC, GYR_Z_LSB))

    # Read in temp data.
    temp  = twos_compliment_combine(smbus.read_byte_data(CHIP_LOC, TEMP_MSB),  smbus.read_byte_data(CHIP_LOC, TEMP_LSB))

    data = open("sensors.dat", "a")
    data.write("{} {} {} {} {} {} {} {}\n".format(acc_x, acc_y, acc_z, gyr_x, gyr_y, gyr_z, temp, datetime.now()))
