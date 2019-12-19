import sys
import numpy as np

def createBufferIn(self, data):
Buffer = np.unpackbits(data).flatten()
#Jutro dodac pętle działającą aż do opróżnienia bufforu 
DataIn = np.frombuffer(Buffer, dtype='S1', count=1024) #Na przykład 1024, wielkość ramki bez nagłówków
if len(DataIn) % 2 != 0:
            raise Exception('Data is uneven!')
            ReturnVal = []
            return ReturnVal
#frame=headers+datain
