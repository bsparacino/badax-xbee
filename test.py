#!/usr/bin/env python

# Imports
import RPi.GPIO as GPIO
from time import sleep

class RaspberryPi:
  GPIO0 = 11
  GPIO1 = 12
  GPIO2 = 13
  GPIO3 = 15
  GPIO4 = 16
  GPIO5 = 18
  GPIO6 = 22
  GPIO7 = 7

  SPI_MOSI = 19
  SPI_MISO = 21
  SPI_SCLK = 23
  SPI_CE0  = 24
  SPI_CE1  = 26

  SDA = 3
  SCL = 5

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

class LCD:
  # Code for this class taken from:
  # https://github.com/lrvick/raspi-hd44780
  # https://github.com/adafruit/Adafruit-Raspberry-Pi-Python-Code
  # Modified in here to better suit our requirements.

  # commands
  LCD_CLEARDISPLAY          = 0x01
  LCD_RETURNHOME            = 0x02
  LCD_ENTRYMODESET          = 0x04
  LCD_DISPLAYCONTROL        = 0x08
  LCD_CURSORSHIFT           = 0x10
  LCD_FUNCTIONSET           = 0x20
  LCD_SETCGRAMADDR          = 0x40
  LCD_SETDDRAMADDR          = 0x80

  # flags for display entry mode
  LCD_ENTRYRIGHT            = 0x00
  LCD_ENTRYLEFT             = 0x02
  LCD_ENTRYSHIFTINCREMENT   = 0x01
  LCD_ENTRYSHIFTDECREMENT   = 0x00

  # flags for display on/off control
  LCD_DISPLAYON             = 0x04
  LCD_DISPLAYOFF            = 0x00
  LCD_CURSORON              = 0x02
  LCD_CURSOROFF             = 0x00
  LCD_BLINKON               = 0x01
  LCD_BLINKOFF              = 0x00

  # flags for display/cursor shift
  LCD_DISPLAYMOVE           = 0x08
  LCD_CURSORMOVE            = 0x00

  # flags for display/cursor shift
  LCD_DISPLAYMOVE           = 0x08
  LCD_CURSORMOVE            = 0x00
  LCD_MOVERIGHT             = 0x04
  LCD_MOVELEFT              = 0x00

  # flags for function set
  LCD_8BITMODE              = 0x10
  LCD_4BITMODE              = 0x00
  LCD_2LINE                 = 0x08
  LCD_1LINE                 = 0x00
  LCD_5x10DOTS              = 0x04
  LCD_5x8DOTS               = 0x00

  def __init__(self):
    self.rs    = RaspberryPi.GPIO7
    self.e     = RaspberryPi.SPI_MOSI
    self.db    = [RaspberryPi.SPI_MISO,
                  RaspberryPi.SPI_SCLK,
                  RaspberryPi.SPI_CE0,
                  RaspberryPi.SPI_CE1]

    GPIO.setup(self.rs, GPIO.OUT)
    GPIO.setup(self.e,  GPIO.OUT)
    for pin in self.db:
      GPIO.setup(pin, GPIO.OUT)

    self.cmd(0x33) # initialization
    self.cmd(0x32) # initialization
    self.cmd(0x28) # 2 line 5x7 matrix
    self.cmd(0x0E) # turn cursor on
    self.cmd(0x06) # shift cursor right

    self.displaycontrol  = self.LCD_DISPLAYON | self.LCD_CURSOROFF 
    self.displaycontrol |= self.LCD_BLINKOFF

    self.displayfunction = self.LCD_4BITMODE | self.LCD_1LINE | self.LCD_5x8DOTS
    self.displayfunction |= self.LCD_2LINE

    """ Initialize to default text direction (for romance languages) """
    self.displaymode =  self.LCD_ENTRYLEFT | self.LCD_ENTRYSHIFTDECREMENT
    self.cmd(self.LCD_ENTRYMODESET | self.displaymode)
    
    self.clear()

  def clear(self):
    """ Clear the LCD """
    print 'Clearing LCD'
    self.cmd(self.LCD_CLEARDISPLAY)
    sleep(0.003)

  def cmd(self, bits, char_mode=False):
    """ Send a command to the LCD """

    sleep(0.001)
    bits = bin(bits)[2:].zfill(8)

    GPIO.output(self.rs, char_mode)

    for pin in self.db:
      GPIO.output(pin, False)

    for i in range(4):
      if bits[i] == "1":
        GPIO.output(self.db[::-1][i], True)

    GPIO.output(self.e, True)
    GPIO.output(self.e, False)

    for pin in self.db:
      GPIO.output(pin, False)

    for i in range(4,8):
      if bits[i] == "1":
        GPIO.output(self.db[::-1][i-4], True)

    GPIO.output(self.e, True)
    GPIO.output(self.e, False)

  def message(self, text):
    """ Send string to LCD. """
    print 'Printing: ', text

    for char in text:
      if char == '\n':
        self.cmd(0xC0) # New Line Command
      else:
        self.cmd(ord(char), True)

class Buzzer:

  def __init__(self):
    self.pins = [RaspberryPi.SDA,
                 RaspberryPi.SCL]

    for pin in self.pins:
      GPIO.setup(pin, GPIO.OUT)

if __name__ == '__main__':
  try:
    GPIO.setmode(GPIO.BOARD)
    keypad = Keypad()
    while True:
      pass
		
  except KeyboardInterrupt:
    GPIO.cleanup()
