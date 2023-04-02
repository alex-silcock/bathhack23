import threading
import wave
import pyaudio
# import simpleaudio as sa

class Loops:
    def __init__(self):
        self.FILENAMES = {
            'bass': 'bathhack23/bass.wav',
            'back-beat': 'bathhack23/back-beat.wav',
            'echo-synth': 'bathhack23/echo-synth.wav',
            'high-hat': 'bathhack23/high-hat.wav',
            'paddington-bass': 'bathhack23/paddington-bass.wav',
            'synth-chord': 'bathhack23/synth-chord.wav'
        }

        self.wf1 = wave.open(self.FILENAMES['bass'], 'rb')
        self.p1 = pyaudio.PyAudio()
        self.stream1 = self.p1.open(format=self.p1.get_format_from_width(self.wf1.getsampwidth()),
                        channels=self.wf1.getnchannels(),
                        rate=self.wf1.getframerate(),
                        output=True)

        self.wf2 = wave.open(self.FILENAMES['back-beat'], 'rb')
        self.p2 = pyaudio.PyAudio()
        self.stream2 = self.p2.open(format=self.p2.get_format_from_width(self.wf2.getsampwidth()),
                                    channels=self.wf2.getnchannels(),
                                    rate=self.wf2.getframerate(),
                                    output=True)

        self.wf3 = wave.open(self.FILENAMES['echo-synth'], 'rb')
        self.p3 = pyaudio.PyAudio()
        self.stream3 = self.p1.open(format=self.p3.get_format_from_width(self.wf3.getsampwidth()),
                                    channels=self.wf3.getnchannels(),
                                    rate=self.wf3.getframerate(),
                                    output=True)

        self.wf4 = wave.open(self.FILENAMES['high-hat'], 'rb')
        self.p4 = pyaudio.PyAudio()
        self.stream4 = self.p4.open(format=self.p4.get_format_from_width(self.wf4.getsampwidth()),
                                    channels=self.wf4.getnchannels(),
                                    rate=self.wf4.getframerate(),
                                    output=True)

        self.wf5 = wave.open(self.FILENAMES['paddington-bass'], 'rb')
        self.p5 = pyaudio.PyAudio()
        self.stream5 = self.p5.open(format=self.p5.get_format_from_width(self.wf5.getsampwidth()),
                                    channels=self.wf5.getnchannels(),
                                    rate=self.wf5.getframerate(),
                                    output=True)

        self.wf6 = wave.open(self.FILENAMES['synth-chord'], 'rb')
        self.p6 = pyaudio.PyAudio()
        self.stream6 = self.p6.open(format=self.p6.get_format_from_width(self.wf6.getsampwidth()),
                                    channels=self.wf6.getnchannels(),
                                    rate=self.wf6.getframerate(),
                                    output=True)

    def play_bass(self):
        # Read and play the audio in chunks
        chunk_size = 1024
        data = self.wf1.readframes(chunk_size)

        while len(data) > 0:
            self.stream1.write(data)
            data = self.wf1.readframes(chunk_size)
        # Clean up
        self.stream1.stop_stream()
        self.stream1.close()
        self.p1.terminate()

    def play_back_beat(self):
        # Read and play the audio in chunks
        chunk_size = 1024
        data = self.wf2.readframes(chunk_size)

        while len(data) > 0:
            self.stream2.write(data)
            data = self.wf2.readframes(chunk_size)
        # Clean up
        self.stream2.stop_stream()
        self.stream2.close()
        self.p2.terminate()

    def play_echo_synth(self):
        # Read and play the audio in chunks
        chunk_size = 1024
        data = self.wf3.readframes(chunk_size)

        while len(data) > 0:
            self.stream3.write(data)
            data = self.wf3.readframes(chunk_size)
        # Clean up
        self.stream3.stop_stream()
        self.stream3.close()
        self.p3.terminate()

    def play_high_hat(self):
        # Read and play the audio in chunks
        chunk_size = 1024
        data = self.wf4.readframes(chunk_size)

        while len(data) > 0:
            self.stream4.write(data)
            data = self.wf4.readframes(chunk_size)
        # Clean up
        self.stream4.stop_stream()
        self.stream4.close()
        self.p4.terminate()

    def play_paddington_bass(self):
        # Read and play the audio in chunks
        chunk_size = 1024
        data = self.wf5.readframes(chunk_size)

        while len(data) > 0:
            self.stream5.write(data)
            data = self.wf5.readframes(chunk_size)
        # Clean up
        self.stream5.stop_stream()
        self.stream5.close()
        self.p5.terminate()

    def play_synth_chord(self):
        # Read and play the audio in chunks
        chunk_size = 1024
        data = self.wf6.readframes(chunk_size)

        while len(data) > 0:
            self.stream6.write(data)
            data = self.wf6.readframes(chunk_size)
        # Clean up
        self.stream6.stop_stream()
        self.stream6.close()
        self.p6.terminate()


class PlayWav:
    def __init__(self):
        self.FILENAMES = {
            'bass': 'bathhack23/bass.wav',
            'back-beat': 'bathhack23/back-beat.wav',
            'echo-synth': 'bathhack23/echo-synth.wav',
            'high-hat': 'bathhack23/high-hat.wav',
            'paddington-bass': 'bathhack23/paddington-bass.wav',
            'synth-chord': 'bathhack23/synth-chord.wav'
        }
        self.threads = []

    def play_wav(self, filename):
        wave_obj = sa.WaveObject.from_wave_file(self.FILENAMES[filename])
        play_obj = wave_obj.play()
        play_obj.wait_done()
        self.run()

    def run(self, filename):
        thread = threading.Thread(target=self.play_wav, args=('bass',))
        thread.start()

if __name__ == '__main__':
    # pw = PlayWav()
    # pw.play_wav('bass')
    l = Loops()

    thread1 = threading.Thread(target=l.play_bass)
    thread2 = threading.Thread(target=l.play_back_beat)
    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()
