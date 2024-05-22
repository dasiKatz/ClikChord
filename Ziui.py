#קוד זה צריך לזהות את כל התקיה של הקבצים ושלא יתאמן כל פעם שאני אשלח לזיהוי שיעשה לפי הקובץ ששמר את נתוני האימון
import librosa
import numpy as np
import os
import keras
from keras.models import load_model
from natsort import natsorted
from keras.initializers import Orthogonal
from tensorflow.keras.initializers import Orthogonal


import tensorflow as tf
#from tensorflow.keras.models import load_model

# הגדרת הנתיב לקובץ המודל שלך
filepath = 'chord_recognition_model.keras.h5'
#mode = keras.saving.load_model(filepath, custom_objects=None, compile=True, safe_mode=True)
#from tensorflow.keras.initializers import Orthogonal
#from tensorflow.keras.models import load_model

# הגדרת הנתיב לקובץ המודל שלך
#filepath = 'chord_recognition_model.h5'

# טעינת המודל
model = load_model(filepath, custom_objects={'Orthogonal': Orthogonal})

# טעינת המודל
#model = load_model(filepath, custom_objects={'Orthogonal': Orthogonal,'time_major': True})

# טעינת המודל שאימנת
#m#del = load_model(r"C:\Users\User\Desktop\Project\chord_recognition_model.h5")
#filepath = r"C:\Users\User\Desktop\Project\chord_recognition_model.h5"

#model = tf.keras.models.load_model(filepath, custom_objects={'Orthogonal': Orthogonal}, compile=True)

print("after loading model")
# קביעת נתיב לתיקיית הבדיקה
test_folder = r'C:\Users\User\Desktop\Project\DataSet\Test'


# פונקציה לפריסת הקליפ לאורך קבוע
def pad_mfcc(mfcc):
    pad_width = 64 - mfcc.shape[1]
    if pad_width > 0:
        mfcc = np.pad(mfcc, ((0, 0), (0, pad_width)), mode='constant')
    else:
        mfcc = mfcc[:, :64]  # חיתוך אם יש יותר מ-64 מאפיינים
    return mfcc


# פונקציה לזיהוי אקורדים בקליפי אודיו
def identify_chord(audio_file_path):
    # קדימות העיבוד של קליפ האודיו
    y, sr = librosa.load(audio_file_path)
    mfcc = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=64)
    mfcc = pad_mfcc(mfcc)
    mfcc_norm = (mfcc - np.mean(mfcc)) / np.std(mfcc)

    # חיזוי האקורד באמצעות המודל
    prediction = model.predict(np.expand_dims(mfcc_norm, axis=0))

    # המרת החיזוי לשם האקורד
    predicted_chord_index = np.argmax(prediction)
    predicted_chord = int_to_chord[predicted_chord_index]

    return predicted_chord


# הגדרת המיפויים במערך הפעם מחוץ לפונקציה
train_folder = r'C:\Users\User\Desktop\Project\DataSet\Training'
train_chord_folders = os.listdir(train_folder)
chord_to_int = {chord: i for i, chord in enumerate(train_chord_folders)}
int_to_chord = {i: chord for chord, i in chord_to_int.items()}

# ניסוי זיהוי אקורד באמצעות פונקציה




def identify_chords_in_folder(folder_path):
    chordArr = []
    with os.scandir(folder_path) as entries:
        for entry in natsorted(entries, key=lambda entry: entry.name):
            if entry.is_file() and entry.name.endswith('.wav'):

                audio_file_path = os.path.join(folder_path, entry.name)
                # נעמי
                print(audio_file_path)
                #
                predicted_chord = identify_chord(audio_file_path)
                print(f"File: {entry.name}, Predicted Chord: {predicted_chord}")
                chordArr.append(predicted_chord)
    return chordArr

#identify_chords_in_folder("files_wav")
# התקייה שבה נרצה לבצע את זיהוי האקורדים
#folder_path = r'C:\Users\User\Desktop\Project\files_wav'
#identify_chords_in_folder(folder_path)










