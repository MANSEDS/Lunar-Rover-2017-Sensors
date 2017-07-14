# read.py
# Created by Matthew Marshall, 2017
# Contributors:
#   Matthew Marshall
#
# This file handles acquiring and printing to stdout the data from the iNEMO inertial module chip.
# This chip contains an accelerometer, a magnetometer and a barometer.

from smbus import SMBus
from datetime import datetime

smbus = SMBus(1)

# Specify chip location info.
CHIP_LOC = 0b1101011

def twos_compliment_combine(msb, lsb):
    twos_compliment = 256 * msb + lsb
    if twos_compliment >= 32767:
        return twos_compliment - 65536
    return twos_compliment

def read_16bit_value(reg_msb, reg_lsb):
    return twos_compliment_combine(smbus.read_byte_data(CHIP_LOC, reg_msb), smbus.read_byte_data(CHIP_LOC, reg_lsb))

# We assume the chosen range of values of +/- 4g.
def read_acc_value(reg_msb, reg_lsb):
    return read_16bit_value(reg_msb, reg_lsb) * 0.122

# We assume the chosen range of values of 0 to 245 deg/s.
def read_gyr_value(reg_msb, reg_lsb):
    return read_16bit_value(reg_msb, reg_lsb) * 0.035

def read(num):
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
    acc_x = read_acc_value(ACC_X_MSB, ACC_X_LSB)
    acc_y = read_acc_value(ACC_Y_MSB, ACC_Y_LSB)
    acc_z = read_acc_value(ACC_Z_MSB, ACC_Z_LSB)

    # Read in acceleration data.
    gyr_x = read_gyr_value(GYR_X_MSB, GYR_X_LSB)
    gyr_y = read_gyr_value(GYR_Y_MSB, GYR_Y_LSB)
    gyr_z = read_gyr_value(GYR_Z_MSB, GYR_Z_LSB)

    # Read in temp data.
    temp  = read, TEMP_MSB),  smbus.read_byte_data(CHIP_LOC, TEMP_LSB))

    data = open("sensors.dat", "a")
    data.write("{} {} {} {} {} {} {} {} {}\n".format(num, acc_x, acc_y, acc_z, gyr_x, gyr_y, gyr_z, temp, datetime.now()))
