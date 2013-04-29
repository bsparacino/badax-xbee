#!/usr/bin/env python

# Imports
import RPi.GPIO as GPIO
from buttons import Buttons
from LCD import LCD
from Rec import Rec
from SensorProcess import SensorProcess
import threading
import thread
#from Buzzer import Buzzer

from Database import Database

if __name__ == '__main__':
  try:
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)
    #buzzer = Buzzer()

    sp = SensorProcess()
    database = Database()

    buttons = Buttons(database, sp)
    buttons_thread = threading.Thread(target=buttons.start,)
    buttons_thread.start()

    #receive = Rec(database, sp);
    #receive_thread = threading.Thread(target=receive.start,)
    #receive_thread.start()



    #self.receive.trip_sensor('0013A2004092D86A')
    
    while True:
      pass
		
  except KeyboardInterrupt:
    GPIO.cleanup()
    database.cleanup()
