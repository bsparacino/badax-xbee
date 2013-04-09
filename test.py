#!/usr/bin/env python

# Imports
import RPi.GPIO as GPIO
from Keypad import Keypad
from LCD import LCD
from Buzzer import Buzzer
from Login import Login

if __name__ == '__main__':
  try:
    GPIO.setmode(GPIO.BOARD)
    login = Login()
    keypad = Keypad(login)
    while True:
      pass
		
  except KeyboardInterrupt:
    GPIO.cleanup()
    login.cleanup()
