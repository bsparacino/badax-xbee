# Imports
import RPi.GPIO as GPIO
from RaspberryPi import RaspberryPi
from time import sleep
from time import clock
from Buzzer import Buzzer
 
# set up the STUFF
GPIO.setmode(GPIO.BOARD)
MOTIONPIN = RaspberryPi.SPI_MOSI
PWR   = RaspberryPi.GPIO6#######
GPIO.setup(PWR, GPIO.OUT)########
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
                GPIO.output(PWR, True)
                while not GPIO.input(MOTIONPIN):
                    sleep(2)
                       
		    
            if (clock() - motion) > .5:
                print 'TIMEOUT'
                GPIO.output(PWR, False)
                sleep(5)
                while GPIO.input(MOTIONPIN):
                    sleep(2)
                    
            sleep(0.005)
            print clock() - motion
    except KeyboardInterrupt:
        GPIO.cleanup()