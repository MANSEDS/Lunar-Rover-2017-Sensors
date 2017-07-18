import subprocess32 as subprocess

from convert import convert
import time

def run():
    subprocess.Popen("mjpg_streamer -i \"input_file.so -f /home/pi/sensors/thermal/stream -r\" -o \"output_http.so -p 8100\"", shell=True)

    i = 0

    while True:
        try:
            subprocess.Popen("./capture.out", shell=True).communicate(timeout=1)
        except subprocess.TimeoutExpired:
            continue
        convert(i % 2)
        i += 1
        # Thermal sensor can only be captured from ~8 times a second.
        # Take a safe value such as 5 per second to ensure the sensor
        # does not "burnout" and not respond for a time.
        time.sleep(0.2)

if __name__ == "__main__":
    run()
