import time

import pyaudio
from pysinewave import SineWave
import pyaudio as p

p = pyaudio.PyAudio()

def s():
    sinewave = SineWave(pitch=0, pitch_per_second=10)
    sinewave.play()
    sinewave.set_volume(0)

    for i in range(12):

        sinewave.set_pitch(i)

        time.sleep(0.1)


if __name__ == "__main__":
    s()