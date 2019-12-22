import sys
import numpy as np
testData = np.array([[1,2,3],[4,5,6]],dtype=np.uint8)
def createBufferIn(data):
    buffer = np.unpackbits(data).flatten()
    print(buffer)
    countIn = 8 #Na przykład 8, wielkość ramki bez nagłówków
    offsetIn = 0
    for offsetIn in range (0, len(buffer)-1, countIn): #Pętla opróżniająca cały buffer
            dataIn = np.frombuffer(buffer, dtype='uint8', count=countIn,offset=offsetIn)
            if len(dataIn) % 2 != 0:
                raise Exception('Data is uneven!')
                returnVal = []
                return returnVal
#frame=headers+datain
#funkcja wysyłająca, zamiast tego teraz wyświetlanie
            print("Zawartosc ramki to:",dataIn)
            offsetIn = offsetIn + countIn

createBufferIn(testData)

