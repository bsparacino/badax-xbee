# Imports
import RPi.GPIO as GPIO
from RaspberryPi import RaspberryPi
from time import sleep
from time import clock
from Buzzer import Buzzer
 
# set up the STUFF
GPIO.setmode(GPIO.BOARD)
MOTIONPIN = RaspberryPi.GPIO6
GPIO.setup(MOTIONPIN, GPIO.IN)
buzzer = Buzzer()

motion = 0
if True:
    try:
        while True:
            clock()
            if not GPIO.input(MOTIONPIN):
                motion = clock()
                print "MOTION"
                buzzer.beep(659, 125)
                while not GPIO.input(MOTIONPIN):
                    sleep(5)
                       
		    
            if (clock() - motion) > 1:
                print 'TIMEOUT'
                while GPIO.input(MOTIONPIN):
                    sleep(.5)
                    
            sleep(0.005)
            print clock() - motion
    except KeyboardInterrupt:
        GPIO.cleanup()