import librosa
import numpy as np
import os

import soundfile
from keras.models import Sequential
from keras.layers import LSTM, Dense

# Define data paths (modify these to your directory structure)
train_folder = r"C:\Users\User\Desktop\Project\DataSet\Training"
test_folder = r"C:\Users\User\Desktop\Project\DataSet\Test"

# Create mapping between chords and integers (consider using a dictionary or set for efficiency)
train_chord_folders = os.listdir(train_folder)
chord_to_int = {chord: i for i, chord in enumerate(train_chord_folders)}
int_to_chord = {i: chord for chord, i in chord_to_int.items()}

# Initialize empty lists for audio clip data
X_train = []
y_train = []

# Function to preprocess audio clips
def preprocess_audio_clip(audio_file_path):
    try:
        y, sr = librosa.load(audio_file_path)  # Try librosa.load first
    except (OSError, soundfile.LibsndfileError):  # Handle potential file format errors
        print(f"Error loading file: {audio_file_path}. Skipping...")
        return None  # Return None to indicate an error

    mfcc = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=40)
    # Padding or truncating to make sure all clips have the same length
   

    mfcc = librosa.util.pad_center(mfcc, pad_width=40, axis=1)
    mfcc_norm = (mfcc - np.mean(mfcc)) / np.std(mfcc)
    return mfcc_norm

# Process audio clips from training folder
for chord_folder in train_chord_folders:
    for clip_file in os.listdir(os.path.join(train_folder, chord_folder)):
        audio_file_path = os.path.join(train_folder, chord_folder, clip_file)
        preprocessed_clip_data = preprocess_audio_clip(audio_file_path)
        if preprocessed_clip_data is not None:  # Only append if processing succeeded
            X_train.append(preprocessed_clip_data)
            y_train.append(chord_to_int[chord_folder])

# Convert lists to NumPy arrays for efficient processing
X_train = np.array(X_train)
y_train = np.array(y_train)

# Define the model architecture (consider experimenting with hyperparameters)
model = Sequential()
model.add(LSTM(128, input_shape=(X_train.shape[1], X_train.shape[2])))
model.add(Dense(len(chord_to_int), activation='softmax'))

# Compile the model
model.compile(loss='sparse_categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

# Train the model (adjust epochs as needed)
model.fit(X_train, y_train, epochs=100)

# Save the trained model (consider using model.save_weights() for just weights)
model.save('chord_recognition_model.h5')

# Load and preprocess test audio clips (assuming 'test_chord_folders' is defined)
X_test = []
for chord_folder in os.listdir(test_folder):
    for clip_file in os.listdir(os.path.join(test_folder, chord_folder)):
        audio_file_path = os.path.join(test_folder, chord_folder, clip_file)
        preprocessed_clip_data = preprocess_audio_clip(audio_file_path)
        if preprocessed_clip_data is not None:
            X_test.append(preprocessed_clip_data)

# Convert test data to a NumPy array
X_test = np.array(X_test)

# Make predictions on test data
predictions = model.predict(X_test)

# Convert predictions to chord labels
predicted_chords = []
for prediction in predictions:
    predicted_chord_index = np.argmax(prediction)
    predicted_chord = int_to_chord[predicted_chord_index]
    predicted_chords.append(predicted_chord)

# Consider adding code to display or use the predictions here
