import librosa
def miktzav(audio_path):
    # Load audio file

    y, sr = librosa.load(audio_path)
    # Calculate tempo (beats per minute)
    tempo, _ = librosa.beat.beat_track(y=y, sr=sr)

    # Estimate time signature based on tempo
    if tempo >= 90:  # Check if tempo is higher than a threshold to distinguish between 4/4 and 2/2
        time_signature = '4/4'
    else:
        time_signature = '3/4'

    print(f"Tempo: {tempo} BPM")
    print(f"Estimated Time Signature: {time_signature}")
miktzav('files_wav')