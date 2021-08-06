# Soundboard
# Setup
Install the packages in `requirements.txt` with something like pip. 

The file `config/settings.py` hold the folder the audio files are read from, and the default sound device. If the 
default sound device is `None`, the engine will prompt the user to select one.

Run `main.py` with python 3 to start the program.

# Usage
Place all mp3 files you want to be in the soundboard into the folder specified in the settings file, default `audio`.
When the program is running, use `numpad 1-9` to play a sound. Hold `numpad .` and type a number on the numpad to input
numbers larger than 9.

Files are ordered in standard system order, as displayed on the program window. 

Disclaimer: Likely only works on Windows 10+.