import init
import read
import os

init.init()

num = 0

if os.path.isfile("/var/www/html/sensors.dat"):
    with open("/var/www/html/sensors.dat", "r") as handle:
        lines  = handle.readlines()
        num = int(lines[-1].split()[0])

while True:
    read.read(num)
    num += 1
