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
        time.sleep(0.1)

if __name__ == "__main__":
    run()
