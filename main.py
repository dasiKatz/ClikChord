import Ziui
import start_3
import text_in_5_seconds
import trytext
import write_chords_to_excel
import start_1
from text_in_5_seconds import wavs_to_text

# import start_4

audio_file = 'song.mp3'
print("1")
#מספר שניות בשיר
seconds_in_song = start_3.get_song_length(audio_file) * 60
print("2")

#מספר האקורדים בשיר
bpm = start_3.get_bpm(audio_file)
print("3")

#מספר אקורדים בשניה
num_chords_in_second = bpm/seconds_in_song
print("4")

#מספר האקורדים ב 5 שניות
num_chord_in_5 = num_chords_in_second*5
print("5")

print("6")

#ממיר את הקובץ ל WAV ולטקסט בקובץ text_song
start_1.startAudio(audio_file)
print("7")
#יוצר קבצים קטנים של wav כמספר הפעימות בשיר שאח"כ כל קובץ נשלח לזיהוי
# start_4.split_wav_file("final.wav", bpm)

#זיהוי חלקיקי השיר
arr_chords = Ziui.identify_chords_in_folder("C:/Users/User/Desktop/Project/files_wav")
print("8")

#לכתוב את האקורדים לאקסל]

write_chords_to_excel.write_chords_to_excel(arr_chords, "chords.xlsx", int(num_chord_in_5))

#כותב את המילים לקובץ טקסט
text_in_5_seconds.wavs_to_text()
print("9")

#כותב את המילים לקובץ אקסל
trytext.text_to_excel("new_text_song.txt","chords.xlsx")
print("1000000")
#למחוק את כל הקבצים

