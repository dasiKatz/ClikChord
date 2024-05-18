from googleTranslate.cloud import speech as speech


def wav_to_text(file_path):
    client = speech.SpeechClient()
    transcript = ""

    with open(file_path, "rb") as audio_file:
        content = audio_file.read()

    audio = speech.RecognitionAudio(content=content)
    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=16000,
        language_code="en-US",
    )

    response = client.recognize(config=config, audio=audio)

    for result in response.results:
        transcript += result.alternatives[0].transcript + " "

    return transcript

# Provide the path to your WAV file
transcript = wav_to_text("final.wav")
print("Transcript: {}".format(transcript))