import sounddevice as sd
import numpy as np

count = 0
volumes = []
once = True
average = 0
plt_count = 0

def print_sound(indata, outdata, frames, times, status):
    global count, once, volumes, average, plt_count

    plt_count += 1

    volume_norm = np.linalg.norm(indata)*10


    if(count < 1000):
        if volume_norm > 0:
            volumes.append(volume_norm)
            count += 1
    else:
        if once:
            for i in volumes:
                average += i

            average = average / len(volumes)

            print('calibration done!')
            print(average)
            once = False

    if average > 0:
        if volume_norm > average:
            print('said')

with sd.Stream(callback=print_sound):
    sd.sleep(1000000)

