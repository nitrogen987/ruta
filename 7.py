from pylab import*
from scipy.io import wavfile
import matplotlib.pyplot as plt
import numpy
from scipy.io.wavfile import read
import numpy as np
import matplotlib.ticker as ticker
import contextlib, datetime, math, os, time, wave, glob
import wave
import pandas as pd


sampFreq, snd = wavfile.read('/home/saturn/1212.wav')

wav = wave.open('/home/saturn/1212.wav', mode="r")
(nchannels, sampwidth, framerate, nframes, comptype, compname) = wav.getparams()

snd = snd / (2.**15)
if len(snd.shape) > 1:
    s1 = snd[:,0]
else:
    s1 = snd
timeArray = arange(0, nframes, 1)
timeArray = timeArray / sampFreq
timeArray = timeArray * 1000  #scale to milliseconds

plt.plot(timeArray, s1, color='k')
ylabel('Amplitude')
xlabel('Time (ms)')
plt.show()          #if you want show graph
n = len(s1) 
p = fft(s1)
nUniquePts = int(ceil((n+1)/2.0))
p = p[0:nUniquePts]
p = abs(p)
p = p/float(n)

c = 10*log10(p)
timeArray1 = arange(0, len(c), 1)
timeArray1 = timeArray1/ sampFreq
timeArray1 = timeArray1 * 1000
plt.plot(timeArray1, c, color='k')
ylabel('DB')
xlabel('Time (ms)')
fr = np.savetxt('frequency.csv', s1, delimiter=',',  fmt='%f')
db = np.savetxt('db.csv', c, delimiter=',',  fmt='%f')


