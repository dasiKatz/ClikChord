import speech_recognition as sr
from pydub import AudioSegment

Text = input("Enter the Text file: ")
r = sr.Recognizer()
Wav = "output_40.wav"
hellow = sr.AudioFile(Wav)
with hellow as source:
    audio = r.record(source)
    # בחירת שפה
    s = r.recognize_google(audio, language="he-IL")
print("Text: " + s)
f = open(Text, "w")
f.write(s)
f.close()