import numpy as np
from keras.models import Sequential
from keras.layers import LSTM, Dense
from keras.preprocessing.sequence import pad_sequences
import os
import tensorflow as tf
#import tensorflow.compat.v1.losses
# Define the paths to the prediction and test folders
prediction_folder = "C:\\Users\\User\\Desktop\\Projectii\\DataSet\\Training"
test_folder = "C:\\Users\\User\\Desktop\\Projectii\\DataSet\\Test"

# קבל את קבצי החיזוי
prediction_files = os.listdir(prediction_folder)

# Get the test files
test_files = os.listdir(test_folder)

# Define the chords
chords = ['Am', 'Bb', 'Bdim', 'C', 'Dm', 'Em' ,'F' ,'G']
# המר את האקורדים לייצוג מספר
chord_to_int = {chord: i for i, chord in enumerate(chords)}#הופך את האקורד לייצוג מספרי(זה בעיקר בשביל הנוחות)
int_to_chord = {i: chord for chord, i in chord_to_int.items()}
am_chord_folder = os.path.join(prediction_folder, 'Am')
am_chord_files = os.listdir(am_chord_folder)
num_am_files = len(am_chord_files)#מביא לי כמה קבצים יש לי מתקיה מסוימת
print("Number of 'Am' chord files:", num_am_files)

# צור רצפי קלט ופלט לאימון
sequence_length = 8 # קובע כמה אקורדים המודל ישקול כקלט כדי לחזות את האקורד הבא. לדוגמה, אם תגדיר את "sequence_length" ל-4, המודל ייקח 4 אקורדים כקלט וינסה לחזות את האקורד ה-5.
input_sequences = []
output_sequences = []


for chord_file in prediction_files:#עובר על כל התקיות של הנסוי
    print(os.access('C:\\Users\\User\\Desktop\\Projectii\\DataSet\\Training\\Am', os.R_OK))
    print(prediction_folder)
    print(chord_file)

    try:
        with open(os.path.join(prediction_folder, chord_file), 'r') as file:
              print("Rebekah here")
              chord_sequence = file.read().splitlines()
            # Process chord_sequence as needed
    except PermissionError as e:
         print(f"Permission error: {e}")
    except FileNotFoundError as e:
        print(f"File not found error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

    chord_sequence = []  # Initialize chord_sequence as an empty list before the code block

    # Your existing code
    if len(chord_sequence) > sequence_length:
        for i in range(len(chord_sequence) - sequence_length):
            input_seq = [chord_to_int[chord] for chord in chord_sequence[i:i + sequence_length]]
            output_seq = chord_to_int[chord_sequence[i + sequence_length]]
            input_sequences.append(input_seq)
            output_sequences.append(output_seq)


    # The rest of your code
    X_train = np.array(input_sequences)
    y_train = np.array(output_sequences)

    # Continue with the model creation, compilation, and training

# המר רצפים למערכים numpy
X_train = np.array(input_sequences)
y_train = np.array(output_sequences)

# Create the model
model = Sequential()
model.add(LSTM(128, input_shape=(sequence_length, 1)))
model.add(Dense(len(chords), activation='softmax'))

# Compile the model






# Compile the model with the correct 'loss' keyword argument
model.compile(loss='sparse_categorical_crossentropy', optimizer='adam')

# Train the model
print("Shape of X_train:", X_train.shape)
print("Shape of y_train:", y_train.shape)
print("Content of X_train:", X_train)
print("Content of y_train:", y_train)
model.fit(np.expand_dims(X_train, axis=-1), y_train, epochs=100)
print("I'm here3")

# Load test data and make predictions
for chord_file in test_files:
    with open(os.path.join(test_folder, chord_file), 'r') as file:
        chord_sequence = file.read().splitlines()
        if len(chord_sequence) >= sequence_length:
            # Prepare test input sequence
            test_input_seq = [chord_to_int[chord] for chord in chord_sequence[:sequence_length]]
            test_input_seq = np.expand_dims(test_input_seq, axis=0)

            # Generate prediction for the next chord
            test_prediction = model.predict(test_input_seq)
            predicted_chord_index = np.argmax(test_prediction)
            predicted_chord = int_to_chord[predicted_chord_index]


            print("File:", chord_file)
            print("Predicted Chord:", predicted_chord)
            print("")
