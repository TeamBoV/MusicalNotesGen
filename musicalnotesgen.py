import wave
import struct
import math
import subprocess
import os

def create_wave_file(frequency, duration, volume, filename):
    # Set the parameters for the wave file
    sample_rate = 44100
    num_samples = int(duration * sample_rate)
    rest_samples = num_samples % sample_rate
    waveform = []

    # Generate the waveform for the note
    for i in range(num_samples):
        sample = volume * math.sin(2 * math.pi * frequency * i / sample_rate)
        waveform.append(sample)

    # Add a rest at the end of the note
    for i in range(rest_samples):
        waveform.append(0)

    # Convert the waveform to a string of bytes
    waveform_bytes = b''.join([struct.pack('f', s) for s in waveform])

    # Create the wave file
    with wave.open(filename, 'w') as f:
        f.setnchannels(1)
        f.setsampwidth(4)
        f.setframerate(sample_rate)
        f.writeframes(waveform_bytes)

# Create the notes from A to G
notes = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']
frequencies = [440, 466.16, 493.88, 523.25, 554.37, 587.33, 622.25, 659.25, 698.46, 739.99, 783.99, 830.61]

for i in range(len(notes)):
    create_wave_file(frequencies[i], 1.0, 0.1, f'{notes[i]}_original.wav')

    # Use sox to adjust the gain of the .wav file
    subprocess.run(['sox', f'{notes[i]}_original.wav', f'{notes[i]}.wav', 'gain', '-12'])

    # Delete the original .wav file
    os.remove(f'{notes[i]}_original.wav')

print('Done!')
