# Imports
import RPi.GPIO as GPIO
from RaspberryPi import RaspberryPi

class Buzzer:

  def __init__(self):
    self.pins = [RaspberryPi.SDA,
                 RaspberryPi.SCL]

    for pin in self.pins:
      GPIO.setup(pin, GPIO.OUT)
