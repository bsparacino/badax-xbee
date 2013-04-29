# Imports
import RPi.GPIO as GPIO
from RaspberryPi import RaspberryPi
from time import sleep
import threading
import thread

class LED:

    def __init__(self):
        # set up the STUFF
        GPIO.setmode(GPIO.BOARD)
        self.LED = RaspberryPi.SCL
        GPIO.setup(self.LED,GPIO.OUT)
        GPIO.output(self.LED, False)

        self.show_status_light = 1

    def status_light(self):
        if True:
            try:

                self.status_light_thread = threading.Thread(target=self.status_light_process)
                self.status_light_thread.start()
                
            except KeyboardInterrupt:
                GPIO.output(LED, False)
                GPIO.cleanup()

    def status_light_process(self):
        while True:
            if(self.show_status_light == 1):
                GPIO.output(self.LED, True)
                sleep(.17)
                GPIO.output(self.LED, False)
                sleep(.17)
                GPIO.output(self.LED, True)
                sleep(.17)
                GPIO.output(self.LED, False)
                sleep(.17)
                GPIO.output(self.LED, True)
                sleep(.17)
                GPIO.output(self.LED, False)
                sleep(.17)
                GPIO.output(self.LED, True)
                sleep(.17)
                GPIO.output(self.LED, False)
            sleep(2)

    def beep(self):
        self.beep_proc_thread = threading.Thread(target=self.beep_process)
        self.beep_proc_thread.start()

    def beep_process(self):
        GPIO.output(self.LED, True)
        sleep(.17)
        GPIO.output(self.LED, False)
        sleep(.17)