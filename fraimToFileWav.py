import os
import speech_recognition as sr
import re
from pydub import AudioSegment
from pocketsphinx import LiveSpeech

# Load the audio file
audio_path = 'final.wav'

# Perform speech recognition on the audio
transcript = ""
for phrase in LiveSpeech(audio_file=audio_path):
    transcript += str(phrase)

# Split the transcript into individual words
words = re.findall(r'\b\w+\b', transcript)

# Calculate duration for each word
audio = AudioSegment.from_wav(audio_path)
audio_duration = len(audio)
word_duration = audio_duration / len(words)

# Divide the audio into segments based on the words
output_dir = 'word_segments'
os.makedirs(output_dir, exist_ok=True)

for idx, word in enumerate(words):
    word_start = idx * word_duration
    word_end = (idx + 1) * word_duration
    word_segment = audio[word_start:word_end]
    word_segment.export(os.path.join(output_dir, f'{word}.wav'), format="wav")

print(f"Finished dividing audio into {len(words)} word segments")
