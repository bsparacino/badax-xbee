# Imports
import time
import RPi.GPIO as GPIO
from RaspberryPi import RaspberryPi


class Buzzer:

    def __init__(self):
        self.pins = [RaspberryPi.SDA, RaspberryPi.SCL]

        for pin in self.pins:
            GPIO.setup(pin, GPIO.OUT)

        self.beep()

    def beep(self):
        PIN = RaspberryPi.SDA
        BUZZER_REPETITIONS = 200
        BUZZER_DELAY = 0.000001
        PAUSE_TIME = 0.05

        #GPIO.setmode(GPIO.BCM)
        #GPIO.setup(pin, GPIO.OUT)

        while True:
            for _ in xrange(BUZZER_REPETITIONS):
                for value in [True, False]:
                    GPIO.output(PIN, value)
                    time.sleep(BUZZER_DELAY)
            time.sleep(PAUSE_TIME)   

    def beep2(self):
        number = 0.000001
        timer = 500

        while timer != 0:
            GPIO.output(RaspberryPi.SDA, True)
            time.sleep(number)
            GPIO.output(RaspberryPi.SDA, False)
            time.sleep(number/100)
            timer = timer - 1
            print timer;

        timer = 200
        time.sleep(0.3)