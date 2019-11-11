from pydub import AudioSegment

sound1 = AudioSegment.from_wav("output.wav")
sound2 = AudioSegment.from_wav("output1.wav")

combined_sounds = sound1 + sound2
combined_sounds.export("path.wav", format="wav")