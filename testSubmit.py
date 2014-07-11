import time
import serial

serialport = serial.Serial("/dev/ttyACM1",9600)
serialport.open()
time.sleep(2)
serialport.write('3')
time.sleep(4)
