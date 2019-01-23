from Adafruit_CharLCD import Adafruit_CharLCD
from time import sleep
import RPi.GPIO as GPIO
import serial
import time
DataSer = serial.Serial('/dev/ttyUSB0',115200)
DataSer.close()
GPIO.setmode(GPIO.BCM)
sensor=26
realay=18
GPIO.setup(sensor,GPIO.IN)
GPIO.setup(realay,GPIO.OUT)
lcd=Adafruit_CharLCD(rs=22,en=11,d4=23,d5=10,d6=9,d7=25,cols=16,lines=2)
while True:
	lcd.clear()
	DataSer.open()
	Data=DataSer.readline()
	if Data[0]=='!':
		if GPIO.input(sensor):
			GPIO.output(realay, True)
			if Data[5]=='H':
				lcd.message(Data[1:3]+'%\nIn USE')
			elif Data[5]=='L':
				lcd.message(Data[1:3]+'%\nEMPTY')
			sleep(3)
			GPIO.output(realay, False)
	DataSer.close()
	sleep(1)
