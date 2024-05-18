import librosa

# Load the audio file
#audio_path = 'final.wav'
#y, sr = librosa.load(audio_path)

# Estimate the tempo (beats per minute) of the audio
#tempo, beat_frames = librosa.beat.beat_track(y, sr)

# Print the estimated tempo
#print(f"Estimated tempo: {tempo} BPM")

# Print the beat frames
#print(f"Beat frames: {beat_frames}")
#ספריה המוצאת מקצב
#import librosa
#import numpy as np

#audio_file = "final.wav"
#audio, sr = librosa.load(audio_file)

#tempo, beats = librosa.beat.beat_track(y=audio, sr=sr)

#chunk_size = int(len(audio) / len(beats))
#chunks = np.array_split(audio, len(beats))
#for i, chunk in enumerate(chunks):
  #  print(f"Chunk {i+1}: {chunk}")
#ספריה שמוצאת את האקןרד


from music21 import converter, chord
#audio_chunk = "final.wav"
def extract_chords(audio_chunk):
    # Load the audio chunk using music21
    stream = converter.parse(audio_chunk)

    # Extract the chords from the stream
    chords = []
    for element in stream.flat:
        if isinstance(element, chord.Chord):
            chords.append(element.pitchedCommonName)

    return chords

# Load audio chunk
audio_chunk = "final.wav"

# Extract chords from the audio chunk
chords = extract_chords(audio_chunk)

# Print the extracted chords
print(f"The extracted chords are: {chords}")