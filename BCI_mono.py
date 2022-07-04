from sqlite3 import Timestamp
import sys; 
#pip install pyserial
import serial
import time 

ser = serial.Serial('COM3' , 9600)
time.sleep(2)

#investigar lo de esta variable
thresh = 0.5

#pip install pylsl
from pylsl import StreamInlet, resolve_stream

#resolver un stream EEG desde el lab network 
print("buscando un controlador de EEG...")
streams = resolve_stream('type' , 'EEG')

#crear un nuevo inlet para resolver el stream
inlet = StreamInlet(streams[0])

while True: 
    #obtener un nuevo sample
    sample, Timestamp = inlet.pull_sample()
    state = sample[0]
    print(state)

    if state >= thresh: 
        print("close")
        ser.write(b'H')

    elif state < thresh:
        print("open")
        ser.write(b'L')
    
    else: 
        print("Algo salio mal...")
