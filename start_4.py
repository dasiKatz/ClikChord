import os
import wave
import numpy as np
import start_2
import start_3


def split_wav_file(input_wav_file, split_times):
    output_folder = "files_wav"
    os.makedirs(output_folder, exist_ok=True)  # Create the output folder if it doesn't exist
    #print(len(split_times))

    with wave.open(input_wav_file, 'rb') as wav_file:
        params = wav_file.getparams()
        frames = wav_file.readframes(params.nframes)
        audio = np.frombuffer(frames, dtype=np.int16)
        frame_rate = wav_file.getframerate()

        for i in range(len(split_times) - 1):
            start_time = int(split_times[i] * frame_rate)
            end_time = int(int(split_times[i + 1] * frame_rate))
            split_audio = audio[start_time:end_time]

            output_file = os.path.join(output_folder, f'output_{i}.wav')
            with wave.open(output_file, 'wb') as output_wav:
                output_wav.setparams(params)
                output_wav.writeframes(split_audio.tobytes())


# Example usage
split_times =start_3.get_beat_seconds('AvartiBachoshech.mp3',start_2.miktzav('final.wav')) # start3 לייבא את הפונקציה
split_wav_file('final.wav', split_times)

