import pyaudio
import wave
import threading

class SoundPlayer:
    def __init__(self, filename):
        self.filename = filename
        self.wf = wave.open(filename, 'rb')
        self.p = pyaudio.PyAudio()
        self.stream = self.p.open(format=self.p.get_format_from_width(self.wf.getsampwidth()),
                channels=self.wf.getnchannels(),
                rate=self.wf.getframerate(),
                output=True)

    def play(self):
        data = self.wf.readframes(1024)
        while data != b'':
            self.stream.write(data)
            data = self.wf.readframes(1024)
        self.stream.close()
        self.p.terminate()

def play_sounds(sound1, sound2):
    thread1 = threading.Thread(target=sound1.play)
    thread2 = threading.Thread(target=sound2.play)
    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()

sound1 = SoundPlayer("high-hat.wav")
sound2 = SoundPlayer("bass.wav")

play_sounds(sound1, sound2)