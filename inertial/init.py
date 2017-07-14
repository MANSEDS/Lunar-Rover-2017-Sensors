# inertial/init.py
# Created by Matthew Marshall, 2017
# Contributors:
#   Matthew Marshall
#
# This file handles initialising the iNEMO inertial module chip.
# This chip contains an accelerometer and a gyroscope.

from smbus import SMBus

def verify_who(chip_addr, whoami_val, smbus_obj):
    return smbus_obj.read_byte_data(chip_addr, 0x0F) == whoami_val

def init():
    smbus = SMBus(1)

    # Specify chip address and WHO_AM_I value.
    CHIP_LOC = 0b1101010
    WHOAMI   = 0b01101001

    # Specify control register addresses for chip.
    CTRL_1  = 0x10 # Output data rate of accelerometer, scale selection and anti-aliasing filter..
    CTRL_2  = 0x11 # 
    CTRL_3  = 0x12 # 
    CTRL_4  = 0x13 #
    CTRL_5  = 0x14
    CTRL_6  = 0x15
    CTRL_7  = 0x16
    CTRL_8  = 0x17
    CTRL_9  = 0x18
    CTRL_10 = 0x19

    if (not verify_who(CHIP_LOC, WHOAMI, smbus)):
        print("iNEMO Sensor not detected!")
        return -1
    else:
        # Prep the chip...
        smbus.write_byte_data(CHIP_LOC, CTRL_1, 0b01011000)   # 208Hz sample rate, +/- 4g, 400Hz bandwidth selection for anti-aliasing.
        smbus.write_byte_data(CHIP_LOC, CTRL_2, 0x01010010)   # 208Hz sample rate, 245 degrees per second selection.
        #smbus.write_byte_data(CHIP_LOC, CTRL_3, 0b00000000)  # Leave defaults.
        #smbus.write_byte_data(CHIP_LOC, CTRL_4, 0b00000000)  # Leave defaults.
        #smbus.write_byte_data(CHIP_LOC, CTRL_5, 0b00000000)  # Leave defaults.
        #smbus.write_byte_data(CHIP_LOC, CTRL_6, 0b00000000)  # Leave defaults.
        #smbus.write_byte_data(CHIP_LOC, CTRL_7, 0b00000000)  # Leave defaults.
        #smbus.write_byte_data(CHIP_LOC, CTRL_8, 0b00000000)  # Leave defaults.
        #smbus.write_byte_data(CHIP_LOC, CTRL_9, 0b00000000)  # Leave defaults.
        #smbus.write_byte_data(CHIP_LOC, CTRL_10, 0b00000000) # Leave defaults.

        return 0
