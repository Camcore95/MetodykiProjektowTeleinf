import sys
import numpy as np

def createBufferIn(self, data):
Buffer = np.unpackbits(data).flatten()
CountIn = 1024 #Na przykład 1024, wielkość ramki bez nagłówków
OffsetIn = 0
for OffsetIn in range (0, len(Buffer): #Pętla opróżniająca cały buffer, dodać wyjątek na samą końcówkę
            DataIn = np.frombuffer(Buffer, dtype='S1', count=CountIn,offset=OffsetIn) 
                        if len(DataIn) % 2 != 0:
                                     raise Exception('Data is uneven!')
                                                ReturnVal = []
                                                return ReturnVal
#frame=headers+datain
#funkcja wysyłająca
            OffsetIn = OffsetIn + CountIn

