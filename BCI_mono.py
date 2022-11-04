from sqlite3 import Timestamp
#pip install os-sys
#pip install --upgrade os_sys 
import sys; 
#pip install pyserial
import serial
import time 

ser = serial.Serial('COM5' , 9600)
time.sleep(2)

#investigar lo de esta variable
thresh = 0.5

#pip install pylsl
from pylsl import StreamInlet, resolve_stream

#resolver un stream EEG desde el lab network 
print("buscando un controlador de EEG...")
streams = resolve_stream('type' , 'markers')
#manejar marcadores, los estimulos

#crear un nuevo inlet para resolver el stream
inlet = StreamInlet(streams[0])

while True: 
    #obtener un nuevo sample
    sample, Timestamp = inlet.pull_sample()
    state = sample[0]
    print(state)

    if state >= thresh: 
        print("close")
        ser.write(b'R')

    elif state < thresh:
        print("open")
        ser.write(b'L')
    
    else: 
        print("Algo salio mal...")
