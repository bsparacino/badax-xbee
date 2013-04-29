# Imports
import RPi.GPIO as GPIO
from RaspberryPi import RaspberryPi
from time import sleep
from time import clock
 
class motion:

    def __init__(self):  
        # set up the STUFF
        GPIO.setmode(GPIO.BOARD)
        self.MOTIONPIN = RaspberryPi.SPI_MOSI
        self.PWR   = RaspberryPi.GPIO6#######
        GPIO.setup(self.PWR, GPIO.OUT)########
        GPIO.setup(self.MOTIONPIN, GPIO.IN)

    def start(self):
        motion = 0
        if True:
            try:
                while True:
                    clock()

                    motion = clock()

                    if not GPIO.input(self.MOTIONPIN):
                        
                        print "MOTION"
                        GPIO.output(self.PWR, True)
                        while not GPIO.input(self.MOTIONPIN):
                            sleep(5)
                               
        		    
                    if (clock() - motion) > 1:
                        print 'TIMEOUT'
                        GPIO.output(self.PWR, False)
                        #sleep(5)
                        while GPIO.input(self.MOTIONPIN):
                            sleep(2)
                            
                    sleep(0.5)
                    print clock() - motion
            except KeyboardInterrupt:
                GPIO.cleanup()