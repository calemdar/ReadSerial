import serial
from datetime import datetime
import os
import platform


#####################################################
PORT = '' # write port here, i.e. COM3
#####################################################

PLATFORM = platform.system()
DIR_PATH = os.path.dirname(os.path.realpath(__file__))
FILE_PATH = f"{DIR_PATH}/output.txt"

if PORT:
	try:
		ser = serial.Serial(PORT, 9600, timeout=1)
	except:
		pass
else:
	ser = None
	if PLATFORM == 'Windows':
		for i in range(3, 10):
			try:
				ser = serial.Serial(f'COM{i}', 9600, timeout=1)
				break
			except:
				pass

	elif PLATFORM == 'Darwin':
		for i in range(0, 1000):
			try:
				port = f'/dev/tty.usbmodem14{i}'
				ser = serial.Serial(port, 9600, timeout=1)
				break
			except:
				pass

if not ser:
	print('No serial connection found!')
	exit()

print('Starting to listen to the serial port')
while (True):
	x = ser.readline().decode('utf-8').replace('\n', '')
	if x:
		txt_file = open(FILE_PATH, "a+")
		if '#' in x:
			timestamp = datetime.now().strftime('%d/%m/%y  %H:%M:%S')
			txt_file.write(f"{x}\n{timestamp}\n")
		else:
			txt_file.write(f"{x}\n")
		txt_file.close()
ser.close()
