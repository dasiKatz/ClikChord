#מציאת קצב-מספר פעימות BPM
import librosa

audio_path = 'final.wav'
audio_data, sample_rate = librosa.load(audio_path)
tempo, beat_frames = librosa.beat.beat_track(y=audio_data, sr=sample_rate)
print("BPM:", tempo)


#המרת קובץ WAV לMIDI
#import librosa
#import numpy as np
#import mido

#wav_file = 'final.wav'
#midi_file = 'mid.mid'

#def wav_to_midi(wav_file, midi_file):
    # Load the WAV file
 #   audio_data, _ = librosa.load(wav_file)

    # Extract the pitch and beat information from the audio
  #  pitches, beat_frames = librosa.piptrack(y=audio_data, sr=44100)

    # Convert the pitch information to MIDI notes
   # midi_notes = np.argmax(pitches, axis=0)

    # Determine the minimum size between midi_notes and beat_frames
    #min_size = min(len(midi_notes), beat_frames.shape[0])

    # Create a MIDI file
  #  midi = mido.MidiFile()
   # track = mido.MidiTrack()
   # midi.tracks.append(track)

    # Add note events to the MIDI track
  #  for i in range(min_size):
   #     note = midi_notes[i]
    #    if note > 0:
     #       note_on = mido.Message('note_on', note=int(np.clip(note, 0, 127)), velocity=64, time=int(beat_frames[i][0]))
      #      note_off = mido.Message('note_off', note=int(np.clip(note, 0, 127)), velocity=64, time=0)
       #     track.append(note_on)
        #    track.append(note_off)

    # Save the MIDI file
   # midi.save(midi_file)

# Convert the WAV file to MIDI
#wav_to_midi(wav_file, midi_file)