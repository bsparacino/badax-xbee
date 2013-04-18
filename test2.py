#!/usr/bin/env python

# Imports
import RPi.GPIO as GPIO
from Buzzer import Buzzer
from Receive import Receive

if __name__ == '__main__':
  try:
    GPIO.setmode(GPIO.BOARD)
    #buzzer = Buzzer()
    #buzzer.beep(659, 125)
    #buzzer.mario()
    receive = Receive()
    
    while True:
      pass
		
  except KeyboardInterrupt:
    GPIO.cleanup()
