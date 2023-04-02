import math
import time

from pysinewave import SineWave


def pitch_to_freq(pitch):
    return 440 * 2 ^ ((pitch - 9) / 12)


def freq_to_pitch(freq):
    return 12 * math.log2(freq / 440) + 9


CHORDS = {
    0   : [-10, -6, -4],
    0.1 : [-7, -4, -2],
    0.2 : [-5, -2, 1],
    0.3 : [-3, 1, 3],
    0.4 : [-1, 3, 5],
    0.5 : [0, 4, 7],
    0.6 : [2, 5, 9],
    0.7 : [3, 7, 10],
    0.8 : [5, 9, 12],
    0.9 : [7, 11, 14],
    1   : [9, 13, 16]
}

# CHORDS = {
#     0: [-6, -2, 1],
#     0.1: [-5, -1, 2],
#     0.2: [-4, 0, 3],
#     0.3: [-2, 2, 5],
#     0.4: [-1, 3, 6],
#     0.5: [0, 4, 7],
#     0.6: [1, 5, 8, 12, 15],
#     0.7: [2, 6, 9, 14, 18],
#     0.8: [4, 8, 11, 16, 22],
#     0.9: [5, 9, 12, 18, 24],
#     1: [6, 10, 13, 20, 27]
# }


class Waves:
    def __init__(self, initial_pitches):
        self.initial_pitches = initial_pitches
        self.waves = []
        for pitch in self.initial_pitches:
            self.waves.append(SineWave(pitch=pitch))

    def get_chords(self, x_pos):
        difference = x_pos - 0.5

        new_chord = []
        for c in self.initial_pitches:
            new_chord.append(c + (difference*10))
        print(new_chord)
        return new_chord

    def update_chord(self, x_pos):
        pitches = CHORDS[x_pos]

        if len(pitches) > len(self.waves):
            for i in range(len(pitches)-len(self.waves)):
                self.waves.append(SineWave(pitch=pitches[len(pitches)-len(self.waves)]))

        if len(pitches) < len(self.waves):
            self.waves = self.waves[1:len(pitches)-1]

        for i in range(len(self.waves)):
            self.waves[i].set_pitch(pitches[i])

        self.run()

    def run(self):
        for wave in self.waves:
            wave.play()
        time.sleep(1)  # Comment out when done

    def stop(self):
        for wave in self.waves:
            wave.stop()


if __name__ == "__main__":
    w = Waves([0, 4, 7])
    w.run()
    w.update_chord(0.6)
    w.update_chord(0.7)
    w.update_chord(0.8)
    w.update_chord(0.9)
    # w.update_chord(1)
    # w.update_chord(1)
    # w.update_chord(1)
