import os
from google.cloud import speech_v1p1beta1 as speech

def transcribe_audio(audio_file):
    client = speech.SpeechClient()

    with open(audio_file, "rb") as audio_file:
        content = audio_file.read()

    audio = speech.RecognitionAudio(content=content)
    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=16000,
        language_code="he-IL",
    )

    response = client.recognize(config=config, audio=audio)

    for result in response.results:
        print("Transcript: {}".format(result.alternatives[0].transcript))

# Example usage
audio_file = "final.wav"
transcribe_audio(audio_file)
