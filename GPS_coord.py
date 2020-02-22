import threading
import serial
import os
import time
import re

def read_GPS_Coord():
    os.system('sudo chmod 777 /dev/serial0')
    time.sleep(3)

    ser = serial.Serial('/dev/serial0', 115200, bytesize=serial.EIGHTBITS, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE, timeout=1)

    ser.write(b'AT+CGNSPWR=1\n')
    time.sleep(5)
    ser.write(b'AT+CGPSINF=0\n')

    rcv=ser.read(100).strip()
    split=rcv.decode('ascii').split(',')

    coor = split[1:3]
    return(coor)

    ser.write(b'AT+CGNSPWR=0\n')
    ser.close()
    