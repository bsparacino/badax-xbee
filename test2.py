#!/usr/bin/env python

# Imports
import RPi.GPIO as GPIO
from Buzzer import Buzzer

if __name__ == '__main__':
  try:
    GPIO.setmode(GPIO.BOARD)
    buzzer = Buzzer()
    
    while True:
      pass
		
  except KeyboardInterrupt:
    GPIO.cleanup()
