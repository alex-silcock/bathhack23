import wave
import pyaudio

FILENAMES = {
    'bass': 'bass.wav',
    'back-beat': 'back-beat.wav',
    'echo-synth': 'echo-synth.wav',
    'high-hat': 'high-hat.wav',
    'paddington-bass': 'paddington-bass.wav',
    'synth-chord': 'synth-chord.wav'
}


def play_sound(sound_type):
    # Open the .wav file
    wf = wave.open(FILENAMES[sound_type], 'rb')
    # Initialize PyAudio
    p = pyaudio.PyAudio()
    # Open a stream to play the audio
    stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                    channels=wf.getnchannels(),
                    rate=wf.getframerate(),
                    output=True)
    stream.volume = 0
    # Read and play the audio in chunks
    chunk_size = 1024
    data = wf.readframes(chunk_size)
    
    while len(data) > 0:
        stream.write(data)
        data = wf.readframes(chunk_size)

    # Clean up
    stream.stop_stream()
    stream.close()
    p.terminate()


if __name__ == "__main__":
    play_sound('synth-chord')
    play_sound('echo-synth')


