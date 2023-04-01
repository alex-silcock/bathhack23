import wave
from pydub import AudioSegment

# Load the two audio files
audio_file1 = AudioSegment.from_wav("chord1.wav")
audio_file2 = AudioSegment.from_wav("chord2.wav")

# Define the duration of the crossfade in milliseconds
crossfade_duration = 5000  # 5 seconds

# Get the last few seconds of audio from the first file
last_seconds = audio_file1[-crossfade_duration:]

# Create a new AudioSegment that is the crossfade between the two files
crossfade = last_seconds.append(audio_file2, crossfade=crossfade_duration)

# Export the crossfade to a new .wav file
crossfade.export("crossfade.wav", format="wav")

# Play the crossfade using the wave module
with wave.open("crossfade.wav", "rb") as wf:
    params = wf.getparams()
    frames = wf.readframes(wf.getnframes())
    wave_out = wave.open("default", "wb")
    wave_out.setparams(params)
    wave_out.writeframes(frames)
    wave_out.close()
