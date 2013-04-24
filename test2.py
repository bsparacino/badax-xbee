#!/usr/bin/env python

# Imports
import RPi.GPIO as GPIO
from Buzzer import Buzzer
from Receive import Receive
import time

if __name__ == '__main__':
  try:
    GPIO.setmode(GPIO.BOARD)
    #buzzer = Buzzer()
    #buzzer.beep(659, 125)
    #buzzer.mario()
    receive = Receive()
    receive.trip_sensor('0013A2004092D86A')
    time.sleep(5)
    receive.stop_timer()
    
    while True:
      pass
		
  except KeyboardInterrupt:
    GPIO.cleanup()
