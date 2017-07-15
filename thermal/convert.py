import subprocess32 as subprocess

def convert(i):
    subprocess.call("convert /home/pi/sensors/thermal/thermal_img.pgm /home/pi/sensors/thermal/stream/thermal_img_" + str(i) + ".jpg", shell=True)
    subprocess.call("rm /home/pi/sensors/thermal/thermal_img.pgm", shell=True)

if __name__ == "__main__":
    convert(0)
