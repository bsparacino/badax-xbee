#!/usr/bin/env python

# Imports
import RPi.GPIO as GPIO
from buttons import Buttons
from LCD import LCD
#from Buzzer import Buzzer
from Database import Database

if __name__ == '__main__':
  try:
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)
    #buzzer = Buzzer()
    database = Database()
    buttons = Buttons(database)
    
    while True:
      pass
		
  except KeyboardInterrupt:
    GPIO.cleanup()
    database.cleanup()
