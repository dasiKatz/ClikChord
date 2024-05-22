
import librosa
import librosa
from mutagen.mp3 import MP3

def get_song_length(file_path):
    audio = MP3(file_path)
    length_in_seconds = audio.info.length
    length_in_minutes = length_in_seconds / 60
    return length_in_minutes
def get_bpm(audio_file):
    # Load the audio file
    y, sr = librosa.load(audio_file)

    # Calculate the tempo (BPM)
    tempo, _ = librosa.beat.beat_track(y=y, sr=sr)
    length=get_song_length(audio_file)
    return tempo*length

# Example usage
#audio_file = 'AvartiBachoshech.mp3'
#bpm = get_bpm(audio_file)
#print("BPM:", bpm)

#rhythm = start_2.miktzav('AvartiBachoshech.mp3')# לקבל את הערת מהפונקציה Miktzav3_4
#beat_seconds = get_beat_seconds(audio_file, rhythm)
#print(beat_seconds)