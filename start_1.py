from pydub import AudioSegment
import speech_recognition as sr
import os


def split_wav_minute(file_path, segment_length=60000):
    # Load the audio file
    audio = AudioSegment.from_wav(file_path)

    # Calculate the number of segments
    total_length = len(audio)
    num_segments = total_length // segment_length

    # Split and export segments
    base_name = os.path.splitext(os.path.basename(file_path))[0]
    output_dir = os.path.join(os.path.dirname(file_path), base_name + "_segments_minutes")
    os.makedirs(output_dir, exist_ok=True)

    for i in range(num_segments):
        start_time = i * segment_length
        end_time = start_time + segment_length
        segment = audio[start_time:end_time]

        segment_name = f"{base_name}_part_{i + 1}.wav"
        segment_path = os.path.join(output_dir, segment_name)
        segment.export(segment_path, format="wav")
        print(f"Exported {segment_path}")

    # Handle the last segment if the total length is not exactly divisible by segment_length
    if total_length % segment_length != 0:
        start_time = num_segments * segment_length
        segment = audio[start_time:]

        segment_name = f"{base_name}_part_{num_segments + 1}.wav"
        segment_path = os.path.join(output_dir, segment_name)
        segment.export(segment_path, format="wav")
        print(f"Exported {segment_path}")


def startAudio(audio_def):
    try:
        # Convert MP3 to WAV
        song = AudioSegment.from_mp3(audio_def)
        wav_file = "final.wav"
        song.export(wav_file, format="wav")
        print(f"Converted {audio_def} to {wav_file}")

        # Split the song into 1-minute segments
        split_wav_minute(wav_file)

        # Convert audio segments to text
        dir_segment_minutes = "final_segments_minutes"
        text = ""
        for segment_file in os.listdir(dir_segment_minutes):
            segment_path = os.path.join(dir_segment_minutes, segment_file)
            if segment_path.endswith('.wav'):
                recognizer = sr.Recognizer()
                with sr.AudioFile(segment_path) as source:
                    audio = recognizer.record(source)
                try:
                    segment_text = recognizer.recognize_google(audio, language="he-IL")
                    text += segment_text + "\n"
                    print(f"Recognized text for {segment_file}: {segment_text}")
                except sr.UnknownValueError:
                    print(f"Google Speech Recognition could not understand audio in {segment_file}")
                except sr.RequestError as e:
                    print(f"Could not request results from Google Speech Recognition service for {segment_file}; {e}")

        # Save the recognized text to a file
        text_file_path = "C:/Users/User/Desktop/Project/text_song.txt"
        with open(text_file_path, "w", encoding='utf-8') as f:
            f.write(text)
        print(f"Text written to {text_file_path}")

    except Exception as e:
        print(f"An error occurred: {e}")


startAudio('song.mp3')






