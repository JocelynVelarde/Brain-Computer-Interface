from sqlite3 import Timestamp
import sys; 
#pip install pyserial
import serial
import time 

ser = serial.Serial('COM3' , 9600)
time.sleep(2)

thresh = 0.5

#pip install pylsl
from pylsl import StreamInlet, resolve_stream

print("buscando un controlador de EEG...")
streams = resolve_stream('type' , 'EEG')

inlet = StreamInlet(streams[0])

while True: 
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
