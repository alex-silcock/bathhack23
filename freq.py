import time, math
from pysinewave import SineWave

def pitch_to_freq(pitch):
    return 440 * 2 ^ ((pitch-9)/12)

def freq_to_pitch(freq):
    return 12 * math.log2(freq/440) + 9

# CHORDS = {
#     0   : [-10, -6, -4],
#     0.1 : [-7, -4, -2],
#     0.2 : [-5, -2, 1],
#     0.3 : [-3, 1, 3],
#     0.4 : [-1, 3, 5],
#     0.5 : [0, 4, 7],
#     0.6 : [2, 5, 9],
#     0.7 : [3, 7, 10],
#     0.8 : [5, 9, 12],
#     0.9 : [7, 11, 14],
#     1   : [9, 13, 16]
# }

CHORDS = {
    0   : [-6, -2, 1],
    0.1 : [-5, -1, 2],
    0.2 : [-4, 0, 3],
    0.3 : [-2, 2, 5],
    0.4 : [-1, 3, 6],
    0.5 : [0, 4, 7],
    0.6 : [0.5, 5, 8],
    0.7 : [2, 6, 9],
    0.8 : [4, 8, 11],
    0.9 : [5, 9, 12],
    1   : [6, 10, 13]
}

class Waves:
    def __init__(self):
        self.wave1 = SineWave(pitch=0)
        self.wave2 = SineWave(pitch=4)
        self.wave3 = SineWave(pitch=7)
        self.waves = [self.wave1, self.wave2, self.wave3]

    def update_chord(self, x_pos):
        pitches = CHORDS[x_pos]
        for i in range(3):
            self.waves[i].set_pitch(pitches[i])

        self.run()

    def run(self):
        for wave in self.waves:
            wave.play()
        time.sleep(1.5) # Comment out when done

    def stop(self):
        for wave in self.waves:
            wave.stop()


if __name__ == "__main__":
    w = Waves()
    w.run()
