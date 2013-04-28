# Imports
import RPi.GPIO as GPIO
from RaspberryPi import RaspberryPi
from time import sleep

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
    self.PWR   = RaspberryPi.GPIO6
    self.rs    = RaspberryPi.GPIO7
    self.e     = RaspberryPi.SPI_MOSI
    self.db    = [RaspberryPi.SPI_MISO,
                  RaspberryPi.SPI_SCLK,
                  RaspberryPi.SPI_CE0,
                  RaspberryPi.SPI_CE1]

    GPIO.setup(self.rs, GPIO.OUT)
    GPIO.setup(self.e,  GPIO.OUT)
    GPIO.setup(self.PWR, GPIO.OUT)
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
    self.begin(15,2)
    
  def begin(self, cols, lines):

      if (lines > 1):
              self.numlines = lines
              self.displayfunction |= self.LCD_2LINE
              self.currline = 0    

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
#----------------------------------------------------------------------------------------
  def home(self):

        self.cmd(self.LCD_RETURNHOME) # set cursor position to zero
        sleep(0.003) # this command takes a long time!
        
  def setCursor(self, col, row):

        self.row_offsets = [ 0x00, 0x40, 0x14, 0x54 ]

        if ( row > self.numlines ): 
                row = self.numlines - 1 # we count rows starting w/0

        self.cmd(self.LCD_SETDDRAMADDR | (col + self.row_offsets[row]))
        
  def displayOff(self): 
      """ Turn the display off """
      GPIO.output(self.PWR, False)
  
  def displayOn(self):
      """ Turn the display on  """
      GPIO.output(self.PWR, True)
      
  def noDisplay(self): 
      """ Turn the display off (quickly) """

      self.displaycontrol &= ~self.LCD_DISPLAYON
      self.cmd(self.LCD_DISPLAYCONTROL | self.displaycontrol)
  
  def display(self):
      """ Turn the display on (quickly) """

      self.displaycontrol |= self.LCD_DISPLAYON
      self.cmd(self.LCD_DISPLAYCONTROL | self.displaycontrol)
  
  def scrollDisplayLeft(self):
      """ These commands scroll the display without changing the RAM """

      self.cmd(self.LCD_CURSORSHIFT | self.LCD_DISPLAYMOVE | self.LCD_MOVELEFT)


  def scrollDisplayRight(self):
      """ These commands scroll the display without changing the RAM """

      self.cmd(self.LCD_CURSORSHIFT | self.LCD_DISPLAYMOVE | self.LCD_MOVERIGHT);   
      
  def noCursor(self):
      """ Turns the underline cursor on/off """

      self.displaycontrol &= ~self.LCD_CURSOROFF
      self.cmd(self.LCD_DISPLAYCONTROL | self.displaycontrol) 
  def Cursor(self):
      """ Turns the underline cursor on/off """

      self.displaycontrol |= self.LCD_CURSORON
      self.cmd(self.LCD_DISPLAYCONTROL | self.displaycontrol)
  
  def noBlink(self):
      """ Turn on and off the blinking cursor """

      self.displaycontrol &= ~self.LCD_BLINKON
      self.cmd(self.LCD_DISPLAYCONTROL | self.displaycontrol)


  def Blink(self):
      """ Turn on and off the blinking cursor """

      self.displaycontrol |= self.LCD_BLINKON
      self.cmd(self.LCD_DISPLAYCONTROL | self.displaycontrol)            
#----------------------------------------------------------------------------------------      
  def message(self, text):
    """ Send string to LCD. """
    print 'Printing: ', text

    for char in text:
      if char == '\n':
        self.cmd(0xC0) # New Line Command
      else:
        self.cmd(ord(char), True)
        
if __name__ == '__main__':
  try:
    GPIO.setmode(GPIO.BOARD)
    LCD = LCD()
    
    LCD.noCursor()
    LCD.message('CATS \nARE CUTE')
    sleep(1)
    LCD.Cursor()
    LCD.message(' =)')
    sleep(2)
    for k in range (10):
        LCD.scrollDisplayRight()
        sleep(.1)
    for k in range (10):
        LCD.scrollDisplayLeft()
        sleep(.1)
    sleep(2)    
    LCD.home()
    for j in range (2):
        for i in range (16):
            LCD.setCursor(i,j)
            sleep(.1)
    LCD.clear()
    LCD.setCursor(0,0)    
    LCD.message('Something here:')
    LCD.setCursor(0,1) 
    LCD.Blink()
    sleep(5)
    LCD.noBlink()

    while True:
      print 'off'
      LCD.displayOff()
      sleep(3)
      print'on'
      LCD.displayOn()
      sleep(3)
      pass
		
  except KeyboardInterrupt:
    GPIO.cleanup()