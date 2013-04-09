#!/usr/bin/env python

# Imports
import RPi.GPIO as GPIO
from Keypad import Keypad
from LCD import LCD
from Buzzer import Buzzer

if __name__ == '__main__':
  try:
    GPIO.setmode(GPIO.BOARD)
    keypad = Keypad()
    while True:
      pass
		
  except KeyboardInterrupt:
    GPIO.cleanup()
