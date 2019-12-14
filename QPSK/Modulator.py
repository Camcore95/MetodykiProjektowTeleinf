import numpy as np


def createSignalI(bit, carrierFreq, fi, time):
    return checkValueOfBit(bit) * np.cos(2 * np.pi * carrierFreq * time + fi)


def createSignalQ(bit, carrierFreq, fi, time):
    return -1j * checkValueOfBit(bit) * np.sin(2 * np.pi * carrierFreq * time + fi)


def checkValueOfBit(bit):
    resultBit = bit
    if bit == 0:
        resultBit = -1
    return resultBit


class Modulator:

    def __init__(self, carrierFreq, symbolLength, fi, numOfPeriods):
        self.carrierFreq = carrierFreq
        self.symbolLength = symbolLength
        self.fi = fi
        self.numOfPeriods = numOfPeriods

    def modulate(self, bitsToModulate):
        time = np.linspace(0, self.numOfPeriods/self.carrierFreq, self.symbolLength)
        result = []
        for i in range(0, len(bitsToModulate), 2):
            signalI = createSignalI(bitsToModulate[i], self.carrierFreq, self.fi, time)
            signalQ = createSignalQ(bitsToModulate[i+1], self.carrierFreq, self.fi, time)
            result.extend(signalI + signalQ)
        return result
