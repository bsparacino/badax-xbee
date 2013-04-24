#!/usr/bin/env python

# Imports
import RPi.GPIO as GPIO
from buttons import Buttons
from LCD import LCD
from Rec import Rec
from SensorProcess import SensorProcess
#from Buzzer import Buzzer

from Database import Database

if __name__ == '__main__':
  try:
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)
    #buzzer = Buzzer()

    sp = SensorProcess()
    database = Database()
    receive = Rec(database, sp);    
    buttons = Buttons(database, receive, sp)

    #self.receive.trip_sensor('0013A2004092D86A')
    
    while True:
      pass
		
  except KeyboardInterrupt:
    GPIO.cleanup()
    database.cleanup()
