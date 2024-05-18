#קוד זה עובד ומזהה קובץ אחד ששולחים לו
import librosa
import numpy as np
from keras.models import load_model

from Chord_Model import int_to_chord

# טעינת המודל שנשמר
model = load_model('chord_recognition_model.keras.h5')

# פונקציה לזיהוי אקורד בקליפ אודיו
def identify_chord(audio_file_path):
    # קדימות העיבוד של הקליפ השמע
    y, sr = librosa.load(audio_file_path)
    mfcc = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=64)
    # Padding לאורך קבוע של 64
    pad_width = 64 - mfcc.shape[1]
    if pad_width > 0:
        mfcc = np.pad(mfcc, ((0, 0), (0, pad_width)), mode='constant')
    else:
        mfcc = mfcc[:, :64]  # חיתוך אם יש יותר מ-64 מאפיינים
    mfcc_norm = (mfcc - np.mean(mfcc)) / np.std(mfcc)

    # חיזוי האקורד באמצעות המודל
    prediction = model.predict(np.expand_dims(mfcc_norm, axis=0))

    # המרת החיזוי לשם האקורד
    predicted_chord_index = np.argmax(prediction)
    predicted_chord = int_to_chord[predicted_chord_index]

    return predicted_chord

# השימוש בפונקציה לזיהוי האקורד בקליפ אודיו
audio_file_path = 'output_40.wav'  # ציינו את נתיב הקובץ של האודיו
identified_chord = identify_chord(audio_file_path)
print(f"The identified chord is: {identified_chord}")
