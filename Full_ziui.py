import os
import numpy as np
from Chord_Model import identify_chord

def identify_chords_in_folder(folder_path):
    chord_results = []  # רשימה ריקה לשמירת תוצאות הזיהוי

    # עבור כל קובץ בתיקיית הקליפים
    for filename in os.listdir(folder_path):
        if filename.endswith('.wav'):  # בדיקה אם הקובץ הוא קובץ אודיו בפורמט wav
            audio_file_path = os.path.join(folder_path, filename)
            identified_chord = identify_chord(audio_file_path)  # זיהוי האקורד בקובץ האודיו
            chord_results.append(identified_chord)  # הוספת התוצאה לרשימה

    return chord_results

# הגדרת התיקייה שבה נרצה לבצע את זיהוי האקורדים
folder_path = r'C:\Users\User\Desktop\Project\files_wav'

# קריאה לפונקציה לזיהוי האקורדים בתיקיית הקבצים והשמת התוצאות במערך
chord_results = identify_chords_in_folder(folder_path)

# הדפסת התוצאות
print("Chord results:")
for idx, chord in enumerate(chord_results, 1):
    print(f"File {idx}: {chord}")
