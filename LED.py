# Imports
import RPi.GPIO as GPIO
from RaspberryPi import RaspberryPi
from time import sleep
 
# set up the STUFF
GPIO.setmode(GPIO.BOARD)
LED = RaspberryPi.SCL
GPIO.setup(LED,GPIO.OUT)


if True:
    try:
        while True:

            GPIO.output(LED, True)
            sleep(.17)
            GPIO.output(LED, False)
            sleep(.17)
            
            GPIO.output(LED, True)
            sleep(.17)
            GPIO.output(LED, False)
            sleep(.17)
            
            GPIO.output(LED, True)
            sleep(.17)
            GPIO.output(LED, False)
            sleep(.17)
            
            GPIO.output(LED, True)
            sleep(.17)
            GPIO.output(LED, False)
            sleep(2)
                
            
    except KeyboardInterrupt:
        GPIO.output(LED, False)
        GPIO.cleanup()