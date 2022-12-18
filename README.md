# Summary

This Python script generates a series of .wav audio files for the notes from A to G. It does this by using the 'create_wave_file' function, which takes four arguments: a frequency (in Hz) for the note, a duration (in seconds) for the note, a volume (a value between 0 and 1) for the note, and a filename for the resulting .wav file. The 'create_wave_file' function uses these arguments to generate a sine wave with the specified frequency and duration, and then writes the waveform to a .wav file with the given filename.

Once the .wav files have been created, the script uses the 'ffmpeg' command-line utility to adjust the volume of each file by a fixed amount (-12 dB). Finally, the script removes the original .wav files, leaving only the modified ones.

# Usage

    python musicalnotesgen.py


The audio files will be saved in the same directory as the script file. You can use a media player to play the audio files and listen to the notes.

# Dependencies

    ffmpeg
