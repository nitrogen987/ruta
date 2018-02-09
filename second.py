import soundfile as sf
import numpy as np
import scipy.io.wavfile as wf
import sounddevice as sd
import matplotlib.pyplot as plt

rate, data = wf.read('/home/saturn/Downloads/1212.wav') #read data in numpy array 
sd.play(data, rate)  #play our numpy array  to make sure that the array is not corrupted

data2, samplerate = sf.read('/home/saturn/Downloads/1212.wav')  #read data second  way 


signal = data * 1.0 / 32768

N = 8192

win = np.hamming(N)
x = signal[0:N] * win
sp = np.fft.rfft(x)
mag = np.abs(sp)
ref = np.sum(win) / 2
s_dbfs = 20 * np.log10(mag / ref)
freq = np.arange((N / 2) + 1) / (float(N) / rate)
plt.plot(freq, s_dbfs)

plt.grid(True)
plt.xlabel('Frequency [Hz]')       #build graph our numpy array
plt.ylabel('Amplitude [dB]')       #build graph our numpy array
plt.show()
#sd.play(data2 , samplerate)   #play second way  if you want

np.savetxt('second.csv', data, delimiter=',')       #save to csv
