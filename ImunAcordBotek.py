# Import necessary libraries
import librosa
import numpy as np
import os
from keras.models import Sequential
from keras.layers import LSTM, Dense

# Define the path to your train and test folders
train_folder = r"C:\Users\User\Desktop\Project\DataSet\Training"
test_folder = r"C:\Users\User\Desktop\Project\DataSet\Test"

# מכניס את התקיות כמערך
train_chord_folders = os.listdir(train_folder)
test_chord_folders = os.listdir(test_folder)
print(train_chord_folders)
print(test_chord_folders)

# Create a mapping between chords and numeric values
chord_to_int = {chord: i for i, chord in enumerate(train_chord_folders)}
int_to_chord = {i: chord for chord, i in chord_to_int.items()}
print(chord_to_int,"line 19")
print(int_to_chord,"line 20")
# Initialize lists to store audio clip data
X_train = []
y_train = []

# Load audio clips from the train folder
#def preprocess_audio_clip(param):
    #audio_data, sr = librosa.load(param)

    # Preprocess the audio data (e.g., extract features, convert to spectrogram)
    # This is where you perform your actual audio data preprocessing

    # Return the preprocessed data
    #return preprocessed_data
def preprocess_audio_clip(audio_file_path):#למה הפונקציה הזו צריכה לקבל נתיב של קובץ שמע?מה זה קשור לאימון

    # טוענת את קובץ השמע
    y, sr = librosa.load(audio_file_path)

    #  MFCC-מחלץ את תכונות ה
    mfcc = librosa.feature.mfcc(y=y, sr=sr)

    # Normalize MFCC מנרמל את הערכים
    mfcc_norm = (mfcc - np.mean(mfcc)) / np.std(mfcc)

    return mfcc_norm
audio_file_path="AvartiBachoshech.mp3"
# Example of using the preprocess_audio_clip function
url="C:\\Users\\User\\Desktop\\Project\\DataSet\\Training\\"
for chord_folder in train_chord_folders:
    for clip_file in os.listdir(os.path.join(train_folder, chord_folder)):
        # Load and preprocess audio clip data (you will need to implement this part)
        # Append preprocessed data to X_train

        #preprocessed_clip_data = preprocess_audio_clip("C:\\Users\\User\\Desktop\\Projectii\\DataSet\\Training\\Am\\Am_acousticguitar_Mari_1.wav")
        preprocessed_clip_data = preprocess_audio_clip(url+chord_folder+'\\'+clip_file)

        X_train.append(preprocessed_clip_data)
        # Append target chord index to y_train
        y_train.append(chord_to_int[chord_folder])
len=0
for arr in X_train:
    if arr.__len__()>len:
        len=arr.__len__()
print(len)
for arr in X_train:
    padded_data = np.pad(arr, ((len-arr.__len__(), 0), (0, 0)), mode='constant', constant_values=0)
    arr=padded_data

# Convert the lists to numpy arrays
X_train = np.array(X_train)
y_train = np.array(y_train)
#הדפסות לבדיקות
print(np.array(X_train))
print(X_train.shape)
print(X_train)
print(y_train)

# Define the model architecture
model = Sequential()
model.add(LSTM(128, input_shape=(X_train.shape[1], X_train.shape[2])))
model.add(Dense(len(chord_to_int), activation='softmax'))

# Assemble the model
model.compile(loss='sparse_categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

# Train the model
model.fit(X_train, y_train, epochs=100)#לפי מה אני קובעת חו את המספר

# Load and preprocess audio clips from the test folder
# Make predictions similar to your existing code

# This code provides an outline to adapt your existing model for chord prediction using audio clips. You will need to implement the audio data loading, preprocessing, and model input shape according to your specific requirements.
# Load and preprocess audio clips from the test folder
X_test = []
for chord_folder in test_chord_folders:
    for clip_file in os.listdir(os.path.join(test_folder, chord_folder)):
        # Load and preprocess audio clip data for testing
        # Append preprocessed data to X_test

        X_test.append(preprocessed_clip_data)

# Convert the list to a numpy array
X_test = np.array(X_test)

# Make predictions for the test data
predictions = model.predict(X_test)

# Convert predictions to chord labels
predicted_chords = [int_to_chord[np.argmax(prediction)] for prediction in predictions]

print("Predicted chords for test data:", predicted_chords)
print(predicted_chords.__len__())





