from flask import send_file

from flask import Flask, request, jsonify,send_file
from flask_cors import CORS
import os


import text_in_5_seconds
#import trytext
import write_chords_to_excel
#from text_in_5_seconds import wavs_to_text
import new_wav_to_text
# import start_4
import exl_to_pdf
import main
import start_1
import start_3
import Ziui


app = Flask(__name__)
CORS(app)
CORS(app, resources={r"/audio_file": {"origins": "http://localhost:3000"}})


@app.route('/audio_file', methods=['POST'])
def audio_file():
    # Check if the post request has the file part
    if 'audioFile' not in request.files:
        return jsonify({'error': 'No file part'}), 400

    file = request.files['audioFile']

    # If the user does not select a file, the browser submits an empty file without a filename
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    # Save the file
    file_path = os.path.join("C:/Users/User/Desktop/Project", "song.mp3")
    file.save(file_path)
#####כאן מבצעים את כל הפונקציות

    audio_file = 'song.mp3'
    print("1")

    # ממיר את הקובץ ל WAV ולטקסט בקובץ text_song
    start_1.startAudio(audio_file)
    print("7")
    # מספר שניות בשיר
    seconds_in_song = start_3.get_song_length(audio_file) * 60
    print("2")

    # מספר האקורדים בשיר
    bpm = start_3.get_bpm(audio_file)
    print("3")

    # מספר אקורדים בשניה
    num_chords_in_second = bpm / seconds_in_song
    print("4")

    # מספר האקורדים ב 5 שניות
    num_chord_in_5 = num_chords_in_second * 5
    print("5")

    print("6")

    # יוצר קבצים קטנים של wav כמספר הפעימות בשיר שאח"כ כל קובץ נשלח לזיהוי
    # start_4.split_wav_file("final.wav", bpm)

    # זיהוי חלקיקי השיר
    arr_chords = Ziui.identify_chords_in_folder("C:/Users/User/Desktop/Project/files_wav")
    print("8")

    # לכתוב את האקורדים לאקסל]

    write_chords_to_excel.write_chords_to_excel(arr_chords, "chords.xlsx", int(num_chord_in_5))

    # כותב את המילים לקובץ טקסט
    text_in_5_seconds.wavs_to_text()
    print("9")

    # כותב את המילים לקובץ אקסל(לפני זה היה בקובץ trytext)
    new_wav_to_text.text_to_excel("new_text_song.txt", "chords.xlsx")
    print("1000000")

    # הפונקציה ממירה את הקובץ אקסל לPDF

    exl_to_pdf.excel_to_pdf("chords.xlsx", "output.pdf", "dejavu-fonts-ttf-2.37/ttf")
    # למחוק את כל הקבצים

    # פונקציה זו מקבלת טקסט וכותבת את המילים בקובץ אקסל בסדר טוב




    print("finish main")
    pdf_file_path = "output.pdf"
    return send_file(pdf_file_path, as_attachment=True)

if __name__ == '__main__':
    print("ghjk")
    app.run(port=5000)
