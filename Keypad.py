# Imports
import RPi.GPIO as GPIO
from RaspberryPi import RaspberryPi
from LCD import LCD
from time import sleep

class Keypad:
  
  def __init__(self):  
    self.pins = [RaspberryPi.GPIO0,
                 RaspberryPi.GPIO1,
                 RaspberryPi.GPIO2,
                 RaspberryPi.GPIO3,
                 RaspberryPi.GPIO4,
                 RaspberryPi.GPIO5,
                 RaspberryPi.GPIO6]
    self.active = 0
    pin0 = {RaspberryPi.GPIO1: '2',
            RaspberryPi.GPIO6: '5',
            RaspberryPi.GPIO5: '8',
            RaspberryPi.GPIO3: '0'}
    pin2 = {RaspberryPi.GPIO1: '1',
            RaspberryPi.GPIO6: '4',
            RaspberryPi.GPIO5: '7',
            RaspberryPi.GPIO3: '*'}
    pin4 = {RaspberryPi.GPIO1: '3',
            RaspberryPi.GPIO6: '6',
            RaspberryPi.GPIO5: '9',
            RaspberryPi.GPIO3: '#'}
    self.lookup = {RaspberryPi.GPIO0: pin0,
                   RaspberryPi.GPIO2: pin2,
                   RaspberryPi.GPIO4: pin4}
    self.message = ''
      
    for i in range(3):
      GPIO.setup(self.pins[::2][i], GPIO.OUT)
      GPIO.setup(self.pins[1::2][i], GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(self.pins[6], GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

    self.lcd = LCD()

    self.setup_callbacks()
    self.loop()

  def setup_callbacks(self):
    for i in range(3):
      GPIO.add_event_detect(self.pins[1::2][i], GPIO.RISING,
                            callback=self.callback, bouncetime=200)
    GPIO.add_event_detect(self.pins[6], GPIO.RISING,
                          callback=self.callback, bouncetime=200)

  def callback(self, channel):
    if (GPIO.input(channel)):
      print 'PRESS: ', self.lookup[self.active][channel]
      self.message += self.lookup[self.active][channel]
      self.lcd.clear()
      self.lcd.message(self.message)

  def loop(self):
    while True:
      for i in range(3):
        self.active = self.pins[::2][i]
        GPIO.output(self.active, True)
        sleep(0.01)
        GPIO.output(self.active, False)

