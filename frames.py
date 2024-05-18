import librosa#חילוק השיר לפריימים

# Load the audio file
audio_path = 'final.wav'
y, sr = librosa.load(audio_path)

# Estimate the tempo (beats per minute) of the audio
tempo, beat_frames = librosa.beat.beat_track(y=y, sr=sr)

# Print the estimated tempo
print(f"Estimated tempo: {tempo} BPM")

# Print the beat frames
print(f"Beat frames: {beat_frames}")
#beat_times = librosa.frames_to_time(beat_frames, sr=sr)#פונקציה המביאה לי את מיקומי הזמן של הפעימות