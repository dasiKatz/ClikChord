#import librosa
#import madmom
#from numpy import zeros
import librosa
# Load the audio file
#audio_file = 'final.wav'
#y, sr = librosa.load(audio_file)

# Extract chords from the audio
#chords = madmom.audio.chords.DeepChromaChordRecognitionProcessor()(y)

# Segment the song based on chord changes
#segments = []
#current_chord = chords[0]
#start_time = 0

#for i in range(1, len(chords)):
   # if chords[i] != current_chord:
    #    end_time = librosa.frames_to_time(i, sr=sr)
   #     segments.append((start_time, end_time, current_chord))
  #      start_time = end_time
 #       current_chord = chords[i]

# Export each segment as a separate audio file
#for idx, (start, end, chord) in enumerate(segments):
 #   segment = y[int(start * sr):int(end * sr)]
#    librosa.output.write_wav(f'segment_{idx}_{chord}.wav', segment, sr)

#קוד שני
#import madmom
import numpy as np

# Load the audio file
#audio_file = 'final.wav'
#y, sr = madmom.io.audio.load_audio_file(audio_file, sample_rate=44100)

# Perform chord recognition using the Tonnetz-based Algorithm
#processor = madmom.features.chords.TonnetzChordRecognitionProcessor()
#annotations = processor(y)

# Define frame length and hop size (adjust as needed)
#frame_len = 2048
#hop_size = 512

# Cut the audio into frames according to detected chords
#frames = []
#for onset, duration, chord in annotations:
 #   start_frame = int(onset * sr / hop_size)
  #  end_frame = int((onset + duration) * sr / hop_size)
   # frame = y[start_frame * hop_size:start_frame * hop_size + frame_len]
    #frames.append(frame)

# Process the frames (e.g., save to files, further analysis)

# Print the number of frames
#print(f"Number of frames: {len(frames)}")

# Further processing or saving frames to files can be done here
# For example, you can save each frame as a separate audio file

#קוד משוהם
def spectral_flux_onset_detection(y, sr):
    # Compute spectral flux
    onset_env = librosa.onset.onset_strength(y=y, sr=sr, hop_length=512)
    # Compute onset times
    onset_frames = librosa.onset.onset_detect(onset_envelope=onset_env, sr=sr)
    onset_times = librosa.frames_to_time(onset_frames, sr=sr)
    return onset_times


audio_file = "final.wav"
y, sr = librosa.load(audio_file, sr=None)

# Get predicted onsets
predicted_onsets = spectral_flux_onset_detection(y, sr)

# Print predicted onsets
print("Predicted onsets:")
for onset in predicted_onsets:
    print("{:.2f} seconds".format(onset))

