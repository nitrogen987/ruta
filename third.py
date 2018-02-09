from pylab import plot, show, subplot
from scipy import signal
from matplotlib import pyplot as plt
from numpy import log10, mean
from scipy.io.wavfile import read
import numpy as np
import matplotlib
import numpy
from scipy.io import wavfile
rate, y = read('/home/saturn/Downloads/timbale.wav') 

def plotsp(y, rate, s=2048):
    
    pxx, freqs, bins, _ = plt.specgram(y, NFFT=s, Fs=rate, noverlap = 0,
                                   cmap=plt.cm.binary, sides='onesided',
                                   window=numpy.hamming(s),
                                   scale_by_freq=None, scale  = 'dB', mode = 'magnitude')
    ax1 = plt.subplot(2, 1,  2)
    freqs = np.take(freqs, np.arange(0, freqs.size, 4))
    
    db = 20 * log10(mean(pxx, axis=1))
    db = np.take(db, np.arange(0, db.size, 4))
    
    plt.plot(freqs, db, 'g')    #db =  20 * log10(mean(1, axis=1))
    #print(db)
    np.savetxt('freq_db.csv', np.transpose([freqs, db]), delimiter=',',  fmt='%f')
    np.savetxt('freq.csv', freqs, delimiter=',',  fmt='%f')
    np.savetxt('db.csv', db, delimiter=',',  fmt='%f')
    plt.show()
    

#np.transpose([db, freqs])
    
plotsp(y, rate, s=2048)

