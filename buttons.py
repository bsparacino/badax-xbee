#!/usr/bin/env python
import time
import RPi.GPIO as GPIO
from RaspberryPi import RaspberryPi
from Buzzer import Buzzer
from LCD import LCD
from Database import Database
from Rec import Rec
import threading
import thread
 
GPIO.setmode(GPIO.BOARD)
DEBUG = 0

class Buttons:

    def __init__(self, database, sensorProcess):

        self.database = database
        self.buzzer = Buzzer()
        self.sp = sensorProcess
        self.password = ''
        self.typePassword = 0

        #buttons_thread = threading.Thread(target=self.start,)
        #buttons_thread.start()
        #self.start()
     
    # read SPI data from MCP3008 chip, 8 possible adc's (0 thru 7)
    def readadc(self, adcnum, clockpin, mosipin, misopin, cspin):
            if ((adcnum > 7) or (adcnum < 0)):
                    return -1
            GPIO.output(cspin, True)
     
            GPIO.output(clockpin, False)  # start clock low
            GPIO.output(cspin, False)     # bring CS low
     
            commandout = adcnum
            commandout |= 0x18  # start bit + single-ended bit
            commandout <<= 3    # we only need to send 5 bits here
            for i in range(5):
                    if (commandout & 0x80):
                            GPIO.output(mosipin, True)
                    else:
                            GPIO.output(mosipin, False)
                    commandout <<= 1
                    GPIO.output(clockpin, True)
                    GPIO.output(clockpin, False)
     
            adcout = 0
            # read in one empty bit, one null bit and 10 ADC bits
            for i in range(12):
                    GPIO.output(clockpin, True)
                    GPIO.output(clockpin, False)
                    adcout <<= 1
                    if (GPIO.input(misopin)):
                            adcout |= 0x1
     
            GPIO.output(cspin, True)
            
            adcout >>= 1       # first bit is 'null' so drop it
            return adcout
     
    def start(self):

        # change these as desired - they're the pins connected from the
        # SPI port on the ADC to the Cobbler
        SPICLK = RaspberryPi.GPIO0
        SPIMISO = RaspberryPi.GPIO1
        SPIMOSI = RaspberryPi.GPIO2
        SPICS = RaspberryPi.GPIO3
         
        # set up the SPI interface pins
        GPIO.setup(SPIMOSI, GPIO.OUT)
        GPIO.setup(SPIMISO, GPIO.IN)
        GPIO.setup(SPICLK, GPIO.OUT)
        GPIO.setup(SPICS, GPIO.OUT)
         
        # 10k trim pot connected to adc #0
        potentiometer_adc = 0;
         
        last_read = 0       # this keeps track of the last potentiometer value
        tolerance = 5       # to keep from being jittery we'll only change
                            # volume when the pot has moved more than 5 'counts'

        buzzer = Buzzer()
        lcd = LCD() 
        lcd.Blink()
        printed = False
        try:
            while True:
                # we'll assume that the pot didn't move
                trim_pot_changed = False
         
                # read the analog pin
                trim_pot = self.readadc(potentiometer_adc, SPICLK, SPIMOSI, SPIMISO, SPICS)
                # how much has it changed since the last read?
                pot_adjust = abs(trim_pot - last_read)
         
                if DEBUG:
                        print "trim_pot:", trim_pot
                        print "pot_adjust:", pot_adjust
                        print "last_read", last_read
         
                if ( pot_adjust > tolerance ):
                       trim_pot_changed = True
         
                if DEBUG:
                        print "trim_pot_changed", trim_pot_changed
         
                if ( trim_pot_changed ):
                        value = trim_pot / 10.24           # convert 10bit adc0 (0-1024) trim pot read into 0-100 volume level
                        value = round(value)          # round out decimal value
                        value = int(value)            # cast volume as integer
                number = '';
                printedNumber = ''
                released = False
                if ( value != 60):
                    if (value >= 75 and value < 80):
                        number ='1'
                    elif (value >= 69 and value < 74):
                        number ='2'
                    elif (value >= 64 and value <= 70):
                        number ='3'
                    elif (value >= 0 and value <= 12):
                        number ='4'
                    elif (value >= 32 and value <= 37):
                        number ='5'
                    elif (value >= 38 and value <= 44):
                        number ='6'
                    elif (value >= 21 and value <= 26):
                        number ='7'
                    elif (value >= 83 and value <= 90):
                        number ='8'
                    elif (value >= 45 and value <= 51):
                        number ='9'
                    elif (value >= 54 and value <= 59):
                        number ='*'
                    elif (value >= 94 and value <= 100):
                        number ='0'
                    elif (value >= 50 and value <= 53):
                        number ='#'
                    else:
                        print "Dunno: ", value   
                
                if (value == 60):
                     released = True
                     printed = False

                if(number != printedNumber and not printed):
                    printedNumber = number
                    print number, value
                    lcd.message(number)
                    buzzer.beep(659, 125)
                    printed = True
                    time.sleep(0.1)

                    if(number == '*'):
                        self.typePassword = 1
                        self.password = ''
                    elif(number == '#' and self.typePassword == 1):
                        lcd.noBlink()
                        self.typePassword = 0
                        user = self.database.check_login(self.password)
                        print user

                        if(user != 'Invalid Code'):
                            self.sp.stop_timer()

                        time.sleep(0.5)
                        lcd.clear()
                        lcd.message(user)
                        self.message = ''
                        time.sleep(5)
                        lcd.clear()
                        lcd.Blink()
                    if(self.password == '1111'):
                        print 'play mario'
                        mario_thread = threading.Thread(target=self.play_song(),)
                        print 'die mario'
                        mario_thread.start()
                    elif(self.typePassword == 1):
                        if(number != '*'):
                            self.password += number

                time.sleep(0.01)
        except KeyboardInterrupt:
              GPIO.cleanup()
              print "\nKill"

    def play_song(self):
        print 'boo'
        self.buzzer.mario()
