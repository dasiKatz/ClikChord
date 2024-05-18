import tempfile
from pydub import AudioSegment
from pydub.playback import play

import miktzav3_4
from start_3 import get_beat_seconds
import os
import pygame


# Function to play a segment of the audio file between two beats
def play_segment(audio_file, start_beat, end_beat):
    audio = AudioSegment.from_file(audio_file)

    start_time = start_beat * 1000  # Convert beat seconds to milliseconds
    end_time = end_beat * 1000

    segment = audio[start_time:end_time]

    # Create a temporary WAV file in a custom temporary directory
    with tempfile.NamedTemporaryFile(suffix='.wav', dir='path_to_custom_temp_dir', delete=False) as temp_file:
        temp_file.close()  # Close the file to allow it to be opened by pydub
        segment.export(temp_file.name, format='wav')
        play(temp_file.name)

# Example usage
audio_file = 'Tfila.mp3'
rhythm = miktzav3_4.miktzav('Tfila.mp3')
beat_seconds = get_beat_seconds(audio_file, rhythm)
os.system('Tfila.mp3')
print("אני פה")
#play_segment(audio_file, beat_seconds[1], beat_seconds[2])

# Play the segment between the 2nd and 3rd beat
#os.system(play_segment(audio_file, beat_seconds[1], beat_seconds[2]))
