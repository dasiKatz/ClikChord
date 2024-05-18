from pydub import AudioSegment
import speech_recognition as sr
import os
import re


# הפונקציה מחלקת הקובץ לקטעים של 5 שניות
def split_wav(file_path, segment_length=5000):
    audio = AudioSegment.from_wav(file_path)

    total_length = len(audio)
    num_segments = total_length // segment_length

    base_name = os.path.splitext(os.path.basename(file_path))[0]
    output_dir = os.path.join(os.path.dirname(file_path), base_name + "_segments")
    os.makedirs(output_dir, exist_ok=True)

    for i in range(num_segments):
        start_time = i * segment_length
        end_time = start_time + segment_length
        segment = audio[start_time:end_time]

        segment_name = f"{base_name}_part_{i + 1}.wav"
        segment_path = os.path.join(output_dir, segment_name)
        segment.export(segment_path, format="wav")
        print(f"Exported {segment_path}")

    if total_length % segment_length != 0:
        start_time = num_segments * segment_length
        segment = audio[start_time:]

        segment_name = f"{base_name}_part_{num_segments + 1}.wav"
        segment_path = os.path.join(output_dir, segment_name)
        segment.export(segment_path, format="wav")
        print(f"Exported {segment_path}")

#ממיר כל 5 שניות לטקסט וכותב לקובץ - כל 5 שניות בשורה
def wavs_to_text():
    dir_segments = "final_segments"  # Path to the directory with the segmented WAV files
    new_text = "C:/Users/User/Desktop/Project/new_text_song.txt"
    str_text = ""

    # מיון הקבצים בתיקייה לפי סדר מספרי
    files = os.listdir(dir_segments)
    files = sorted(files, key=lambda x: int(re.search(r'\d+', x).group()))

    for segment in files:
        segment_path = os.path.join(dir_segments, segment)
        if segment_path.endswith('.wav'):
            r = sr.Recognizer()
            with sr.AudioFile(segment_path) as source:
                audio = r.record(source)
                try:
                    s = r.recognize_google(audio, language="he-IL")
                    str_text += s + "\n"
                except sr.UnknownValueError:
                    print(f"Google Speech Recognition could not understand audio in {segment}")
                    str_text += "\n"
                except sr.RequestError as e:
                    print(f"Could not request results from Google Speech Recognition service for {segment}; {e}")

    with open(new_text, "w", encoding='utf-8') as f:
        f.write(str_text)
    print(f"Text written to {new_text}")


# קריאה לפונקציות
split_wav("final.wav")
wavs_to_text()
