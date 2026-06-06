# Audio Visualizer Analyzer
import pyaudio
import os
import struct
import numpy as np
import matplotlib.pyplot as plt
import time
from scipy.fft import fft
from tkinter import TclError

# Constants #
CHUNK = 1024 * 2
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100

# Creates Figure and Two Axes #
fig, (ax, ax2) = plt.subplots(2, figsize=(15, 8)) # Figsize controls size of both

# Open Audio, and Start Streaming At Set Vars #
input_audio = pyaudio.PyAudio()
stream = input_audio.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, output=True, frames_per_buffer=CHUNK)

plt.show(block=True)
