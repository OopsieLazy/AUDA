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

# Open Audio, and Start Streaming At Set Vars #
input_audio = pyaudio.PyAudio()
stream = input_audio.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, output=True, frames_per_buffer=CHUNK)

plt.ion()
# Creates Figure and Two Axes #
fig, (ax, ax2) = plt.subplots(2, figsize=(15, 8)) # Figsize controls size of both

x = np.arange(0, 2* CHUNK, 2)
x_fft = np.linspace(0, RATE, CHUNK)

line, = ax.plot(x, np.random.rand(CHUNK), '-', lw=2)
line_fft, = ax.plot(x_fft, np.random.rand(CHUNK), '-', lw=2)

ax.set_ylim(0, 255)
ax.set_xlim(0, 2 * CHUNK)

plt.setp(ax, xticks=[0, CHUNK, 2 * CHUNK], yticks=[0, 128, 255])

ax2.set_xlim(20, RATE / 2)

plt.show(block=False)

while True:
    data = stream.read(CHUNK)  # Getting byte --> Needs to be converted
    data_int = np.array(struct.unpack(str(CHUNK) + 'h', data))
    line.set_ydata(data_int)
    fig.canvas.draw()
    fig.canvas.flush_events()
