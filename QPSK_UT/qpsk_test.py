import sys
import numpy as np
import matplotlib.pyplot as plt

from transmitter import Modulator
from ether import Ether
from receiver import Demodulator

from scipy.signal import hilbert

fc=2e3
fs=10e4


# creation of input data 
txData = np.random.randint(0, 69, 4, dtype=np.uint8)
qamModulator = Modulator(fc=fc, fs=fs)

# initialization of tx channel
constelationPoints = qamModulator.createConstelationQAM(txData)
modulatedData, upsampledSymmbols, timebase = qamModulator.modulateQAM(
    constelationPoints)


# plotting tx symbols 
i_symbol_val = [x[0] for x in upsampledSymmbols]
y_symbol_val = [x[1] for x in upsampledSymmbols]
fig0, axs0 = plt.subplots(2, 1, constrained_layout=True)
fig0.suptitle('Input data', fontsize=16)
axs0[0].plot(timebase, i_symbol_val, 'o', timebase, y_symbol_val, 'x')
axs0[0].set_title('Real and complex part of constelation symbols')
axs0[0].set_xlabel('time [s]')
axs0[0].set_ylabel('amplitude')
axs0[1].plot(timebase, modulatedData)
axs0[1].set_title('QAM modulated data ')
axs0[1].set_xlabel('time [s]')
axs0[1].set_ylabel('amplitude')
plt.show()

# adding noise to simulate transmission channel
ether = Ether()
noisyTimebase = ether.addJitter(timebase)
shiftedFrequency = ether.changeFrequency(noisyTimebase)
fig1, axs1 = plt.subplots()
axs1.plot(timebase, modulatedData, label='Clean Modulated data')
axs1.plot(noisyTimebase, modulatedData, label='Added AWGN')
axs1.plot(shiftedFrequency, modulatedData, label='Added Doplers shift')
axs1.set_title('Modeling enviroment')
axs1.set_xlabel('time [s]')
axs1.set_ylabel('amplitude')
plt.legend()
plt.show()


# demodulating data
demodulator = Demodulator(fc=fc,fs=fs)
idatDemod, qdatDemod = demodulator.demodulateQam(noisyTimebase,modulatedData)

fig2, axs2 = plt.subplots(3, 1, constrained_layout=True)
fig2.suptitle('Demodulator circuit', fontsize=16)
axs2[0].plot(noisyTimebase, modulatedData)
axs2[0].set_title('Noisy data')
axs2[0].set_xlabel('time [s]')
axs2[0].set_ylabel('amplitude')
# axs2[1].plot(xdemodVals, ydemodinterp)
# axs2[1].set_title('clock recovery (double the frequency)')
# axs2[1].set_xlabel('time [s]')
# axs2[1].set_ylabel('amplitude')
# # axs2[2].plot(xdemodVals[:len(xdemodVals)//2], ydemodinterp[:len(ydemodinterp)//2])
# axs2[1].plot(noisyTimebase, ydemodinterp[:len(ydemodinterp)//2])
# axs2[1].set_title('Recovered base clock frequency')
# axs2[1].set_xlabel('time [s]')
# axs2[1].set_ylabel('amplitude')
axs2[1].plot(noisyTimebase, idatDemod)
axs2[1].set_title('Downconverted signal ')
axs2[1].set_xlabel('time [s]')
axs2[1].set_ylabel('amplitude')
axs2[2].plot(noisyTimebase, qdatDemod)
axs2[2].set_title('Downconverted signal ')
axs2[2].set_xlabel('time [s]')
axs2[2].set_ylabel('amplitude')
plt.show()

# axs2[2].plot(noisyTimebase, modulatedData)




# plt.subplot(3, 1, 3)
# plt.plot(noisyTimebase, modulatedData)
# plt.plot(shiftedFrequency, modulatedData)
# plt.show()

# fig1, axs2 = plt.plot(timebase, modulatedData, noisyTimebase, modulatedData, 'x', shiftedFrequency, modulatedData,'o' )

# fig2 = plt.figure()
# # Demodulationby squaring signal:
# # https://dsp.stackexchange.com/questions/32133/phase-synchronization-in-bpsk

# x = np.linspace(0, 1e-05, len(modulatedData))
# xvals = np.linspace(0, 1e-05, 2*len(modulatedData))
# yinterp = np.interp(xvals, x, np.square(modulatedData))

# plt.plot(x, np.square(modulatedData))
# plt.plot(x, yinterp[:len(yinterp)//2])


# fig4 = plt.figure()
# fig4.suptitle
# plt.title('Simple plot')
# plt.plot(x, np.abs((yinterp[:len(yinterp)//2])))

# applying Hilbert transform to obtain phase shift



# analyticSignal = hilbert(np.abs(yinterp[:len(yinterp)//2]))
# plt.plot(x, np.square(modulatedData))
# plt.plot(x, analyticSignal)


# demolulation:

# fig5 = plt.figure()
# ydemod = yinterp[:len(yinterp)//2]* modulatedData
# plt.plot(ydemod)


# plt.show()

# Demodulation

# 


