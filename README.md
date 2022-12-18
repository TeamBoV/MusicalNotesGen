# Summary

This Python script generates a series of .wav audio files for the notes from A to G. It does this by using the 'create_wave_file' function, which takes four arguments: a frequency (in Hz) for the note, a duration (in seconds) for the note, a volume (a value between 0 and 1) for the note, and a filename for the resulting .wav file. The 'create_wave_file' function uses these arguments to generate a sine wave with the specified frequency and duration, and then writes the waveform to a .wav file with the given filename.

Once the .wav files have been created, the script uses the 'ffmpeg' command-line utility to adjust the volume of each file by a fixed amount (-12 dB). Finally, the script removes the original .wav files, leaving only the modified ones.

# Usage

    python musicalnotesgen.py


The audio files will be saved in the same directory as the script file. You can use a media player to play the audio files and listen to the notes.

# Dependencies

    ffmpeg

# How to install ffmpeg

# Windows
There are several ways to install FFmpeg on Windows:

Download a pre-built static binary from the FFmpeg website

    (https://ffmpeg.org/download.html#build-windows).

Extract the downloaded archive and add the bin folder to your system's PATH environment variable.
Use a package manager such as Chocolatey (https://chocolatey.org/) to install FFmpeg. Open a command prompt and run the following command:

    choco install ffmpeg

This will install the latest version of FFmpeg and add it to your system's PATH.

Use a third-party software installer such as the Zeranoe FFmpeg builds (https://ffmpeg.zeranoe.com/builds/). Download and run the installer, and follow the prompts to install FFmpeg.

# Mac
There are several ways to install FFmpeg on Mac:

Use a package manager such as Homebrew (https://brew.sh/) to install FFmpeg. Open a terminal and run the following command:

    brew install ffmpeg

This will install the latest version of FFmpeg and add it to your system's PATH.
Download a pre-built static binary from the FFmpeg website (https://ffmpeg.org/download.html#build-mac). Extract the downloaded archive and add the bin folder to your system's PATH environment variable.

# Linux
There are several ways to install FFmpeg on Linux:

Use a package manager such as apt (Debian/Ubuntu), yum (CentOS/Red Hat), or dnf (Fedora) to install FFmpeg. For example, on Debian/Ubuntu, you can use the following commands:

    sudo apt update
    sudo apt install ffmpeg

This will install the latest version of FFmpeg available through the package manager.

Download the source code from the FFmpeg website (https://ffmpeg.org/download.html#source) and build FFmpeg from source. This can be a more involved process, but it allows you to customize your build and potentially get the latest version of FFmpeg.
