import librosa
import numpy as np
import os
from keras.models import Sequential
from keras.layers import LSTM, Dense

# הגדרת נתיבים
train_folder = r'C:\Users\User\Desktop\Project\DataSet\Training'
test_folder = r'C:\Users\User\Desktop\Project\DataSet\Test'

# יצירת מיפוי בין אקורדים למספרים שלמים
train_chord_folders = os.listdir(train_folder)
chord_to_int = {chord: i for i, chord in enumerate(train_chord_folders)}
int_to_chord = {i: chord for chord, i in chord_to_int.items()}

# אתחול רשימות עבור נתוני קליפ אודיו
X_train = []
y_train = []

# פונקציה לקדם עיבוד קליפי אודיו
def preprocess_audio_clip(audio_file_path):
    y, sr = librosa.load(audio_file_path)
    mfcc = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=64)
    # Padding לאורך קבוע של 40
    pad_width = 64 - mfcc.shape[1]
    if pad_width > 0:
        mfcc = np.pad(mfcc, ((0, 0), (0, pad_width)), mode='constant')
    else:
        mfcc = mfcc[:, :64]  # חיתוך אם יש יותר מ-40 מאפיינים
    mfcc_norm = (mfcc - np.mean(mfcc)) / np.std(mfcc)
    return mfcc_norm

# עיבוד קליפי אודיו מתיקת הקלסר
for chord_folder in train_chord_folders:
    for clip_file in os.listdir(os.path.join(train_folder, chord_folder)):
        audio_file_path = os.path.join(train_folder, chord_folder, clip_file)
        preprocessed_clip_data = preprocess_audio_clip(audio_file_path)
        X_train.append(preprocessed_clip_data)
        y_train.append(chord_to_int[chord_folder])

# המרת רשימות למערכים של NumPy
X_train = np.array(X_train, dtype=np.float32)
y_train = np.array(y_train)

# הגדרת המודל
model = Sequential()
model.add(LSTM(128, input_shape=(X_train.shape[1], X_train.shape[2])))
model.add(Dense(len(chord_to_int), activation='softmax'))

# הרכבת המודל
model.compile(loss='sparse_categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

# אימון המודל
model.fit(X_train, y_train, epochs=100)

# שמירת המודל
model.save('chord_recognition_model.h5')

# טעינת וקדם עיבוד קליפי אודיו מתיקת הבדיקה
X_test = []
test_chord_folders = test_folder


test_home = r'C:\Users\User\Desktop\Project\DataSet\Test'
directory_list = os.listdir(test_home)

for directory in directory_list:
    print(directory)
    full_directory_path = os.path.join(test_home, directory)
    print(full_directory_path)
    for filename in os.listdir(full_directory_path):
        if filename.endswith('.wav'):  # Check if the file is an audio file
            print(filename)
            audio_file_path = os.path.join(full_directory_path, filename)
            preprocessed_clip_data = preprocess_audio_clip(audio_file_path)
            X_test.append(preprocessed_clip_data)

# def get_directory_names(directory_path):
#     return [name for name in os.listdir(directory_path) if os.path.isdir(os.path.join(directory_path, name))]
#
# test_home = r'C:\Users\User\Desktop\Project\DataSet\Test'
# directory_list = get_directory_names(test_home)
# print(directory_list)
#
# for directory in directory_list:
#     print(directory)
#     full_directory_path = os.path.join(test_home, directory)
#     print(full_directory_path)
#     for filename in os.listdir(full_directory_path):
#         print(filename)
#         audio_file_path = os.path.join(full_directory_path, filename)
#         preprocessed_clip_data = preprocess_audio_clip(audio_file_path)
#         X_test.append(preprocessed_clip_data)
# for chord_folder in test_chord_folders:
#     print(test_folder)
#     print(chord_folder)
#     for clip_file in os.listdir(os.path.join(test_folder, chord_folder)):
#         print(clip_file+"שורה 66")
#         audio_file_path = os.path.join(test_folder, chord_folder, clip_file)
#         preprocessed_clip_data = preprocess_audio_clip(audio_file_path)
#         X_test.append(preprocessed_clip_data)
#     print("אני פה")

# המרת הרשימה למערך NumPy
X_test = np.array(X_test)
print(X_test)
print("אני פה 11111")


# ביצוע תחזיות עבור נתוני הבדיקה
predictions = model.predict(X_test)
print("line 77")
print(predictions)

#print(predictions+"שורה 77")
# המרת תחזיות לתיוגי אקורדים
predicted_chords = []
for prediction in predictions:
    predicted_chord_index = np.argmax(prediction)
    predicted_chord = int_to_chord[predicted_chord_index]
    predicted_chords.append(predicted_chord)


# הדפסת 5 התחזיות הראשונות
for i in range(8):
    print(f"קליפ {i + 1}: אקורד חיזוי - {predicted_chords[i]}")