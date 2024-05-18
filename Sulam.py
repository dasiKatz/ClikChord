from music21 import converter, roman

# Load the MIDI file or musicxml file
song = converter.parse('LechuAroch.mp3')

# Get the key of the song
key = song.analyze('key')

# Print the identified key and its corresponding scale
print("Key:", key.tonic.name, key.mode)
print("Scale:", key.getScale().name)

# Alternatively, you can print the key using roman numeral notation
print("Roman Numeral:", roman.romanNumeralFromKey(key))