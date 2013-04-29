# Imports
import time
import RPi.GPIO as GPIO
from RaspberryPi import RaspberryPi
from LED import LED

class Buzzer:

    def __init__(self):
        self.pins = [RaspberryPi.SDA, RaspberryPi.GPIO7]
        self.led = LED()

        for pin in self.pins:
            GPIO.setup(pin, GPIO.OUT)
        #self.boop()
        #self.mario()
        #time.sleep(5)
        #self.storm()
        #self.beep(659, 125)

    def beep(self, hz, ms):

        #print 'beep ' + str(hz) + 'hz ' + str(ms) + 'ms'
        DELAY_OFFSET = 11
        us = (500000 / hz) - DELAY_OFFSET
        rep = (ms * 500) / (us + DELAY_OFFSET)

        sleep_time = us/1000000.0

        for i in range(0, rep):
            GPIO.output(RaspberryPi.SDA, True)
            GPIO.output(RaspberryPi.GPIO7, False)
            time.sleep(sleep_time)
            GPIO.output(RaspberryPi.SDA, False)
            GPIO.output(RaspberryPi.GPIO7, True)            
            time.sleep(sleep_time)
            
        self.led.beep()            

        #time.sleep(0.05)

    def beepBoopLoop(self):
        for i in range(0, 100000):
            print i
            self.beep(2000, 1000)
            time.sleep(0.10)

    def boop(self):
        print 'boop'
        for _ in xrange(5):
            for value in [True, False]:
                GPIO.output(RaspberryPi.SDA, value)
                time.sleep(0.001)
        time.sleep(0.05) 

    def sleep2(self, ms):
        sleep_time = ms/1000.0
        time.sleep(sleep_time)

    def mario(self):
        self.beep(659, 125)
        self.beep(659, 125)
        self.sleep2(125)
        self.beep(659, 125)
        self.sleep2(167)
        self.beep(523, 125)
        self.beep(659, 125)
        self.sleep2(125)
        self.beep(784, 125)
        self.sleep2(375)
        self.beep(392, 125)
        self.sleep2(375)
        self.beep(523, 125)
        self.sleep2(250)
        self.beep(392, 125)
        self.sleep2(250)
        self.beep(330, 125)
        self.sleep2(250)
        self.beep(440, 125)
        self.sleep2(125)
        self.beep(494, 125)
        self.sleep2(125)
        self.beep(466, 125)
        self.sleep2(42)
        self.beep(440, 125)
        self.sleep2(125)
        self.beep(392, 125)
        self.sleep2(125)
        self.beep(659, 125)
        self.sleep2(125)
        self.beep(784, 125)
        self.sleep2(125)
        self.beep(880, 125)
        self.sleep2(125)
        self.beep(698, 125)
        self.beep(784, 125)
        self.sleep2(125)
        self.beep(659, 125)
        self.sleep2(125)
        self.beep(523, 125)
        self.sleep2(125)
        self.beep(587, 125)
        self.beep(494, 125)
        self.sleep2(125)
        self.beep(523, 125)
        self.sleep2(250)
        self.beep(392, 125)
        self.sleep2(250)
        self.beep(330, 125)
        self.sleep2(250)
        self.beep(440, 125)
        self.sleep2(125)
        self.beep(494, 125)
        self.sleep2(125)
        self.beep(466, 125)
        self.sleep2(42)
        self.beep(440, 125)
        self.sleep2(125)
        self.beep(392, 125)
        self.sleep2(125)
        self.beep(659, 125)
        self.sleep2(125)
        self.beep(784, 125)
        self.sleep2(125)
        self.beep(880, 125)
        self.sleep2(125)
        self.beep(698, 125)
        self.beep(784, 125)
        self.sleep2(125)
        self.beep(659, 125)
        self.sleep2(125)
        self.beep(523, 125)
        self.sleep2(125)
        self.beep(587, 125)
        self.beep(494, 125)
        self.sleep2(375)
        self.beep(784, 125)
        self.beep(740, 125)
        self.beep(698, 125)
        self.sleep2(42)
        self.beep(622, 125)
        self.sleep2(125)
        self.beep(659, 125)
        self.sleep2(167)
        self.beep(415, 125)
        self.beep(440, 125)
        self.beep(523, 125)
        self.sleep2(125)
        self.beep(440, 125)
        self.beep(523, 125)
        self.beep(587, 125)
        self.sleep2(250)
        self.beep(784, 125)
        self.beep(740, 125)
        self.beep(698, 125)
        self.sleep2(42)
        self.beep(622, 125)
        self.sleep2(125)
        self.beep(659, 125)
        self.sleep2(167)
        self.beep(698, 125)
        self.sleep2(125)
        self.beep(698, 125)
        self.beep(698, 125)
        self.sleep2(625)
        self.beep(784, 125)
        self.beep(740, 125)
        self.beep(698, 125)
        self.sleep2(42)
        self.beep(622, 125)
        self.sleep2(125)
        self.beep(659, 125)
        self.sleep2(167)
        self.beep(415, 125)
        self.beep(440, 125)
        self.beep(523, 125)
        self.sleep2(125)
        self.beep(440, 125)
        self.beep(523, 125)
        self.beep(587, 125)
        self.sleep2(250)
        self.beep(622, 125)
        self.sleep2(250)
        self.beep(587, 125)
        self.sleep2(250)
        self.beep(523, 125)
        self.sleep2(1125)
        self.beep(784, 125)
        self.beep(740, 125)
        self.beep(698, 125)
        self.sleep2(42)
        self.beep(622, 125)
        self.sleep2(125)
        self.beep(659, 125)
        self.sleep2(167)
        self.beep(415, 125)
        self.beep(440, 125)
        self.beep(523, 125)
        self.sleep2(125)
        self.beep(440, 125)
        self.beep(523, 125)
        self.beep(587, 125)
        self.sleep2(250)
        self.beep(784, 125)
        self.beep(740, 125)
        self.beep(698, 125)
        self.sleep2(42)
        self.beep(622, 125)
        self.sleep2(125)
        self.beep(659, 125)
        self.sleep2(167)
        self.beep(698, 125)
        self.sleep2(125)
        self.beep(698, 125)
        self.beep(698, 125)
        self.sleep2(625)
        self.beep(784, 125)
        self.beep(740, 125)
        self.beep(698, 125)
        self.sleep2(42)
        self.beep(622, 125)
        self.sleep2(125)
        self.beep(659, 125)
        self.sleep2(167)
        self.beep(415, 125)
        self.beep(440, 125)
        self.beep(523, 125)
        self.sleep2(125)
        self.beep(440, 125)
        self.beep(523, 125)
        self.beep(587, 125)
        self.sleep2(250)
        self.beep(622, 125)
        self.sleep2(250)
        self.beep(587, 125)
        self.sleep2(250)
        self.beep(523, 125)
        self.sleep2(625)
    def storm(self):
         NOTE_B0  =31
         NOTE_C1  =33
         NOTE_CS1 =35
         NOTE_D1  =37
         NOTE_DS1 =39
         NOTE_E1  =41
         NOTE_F1  =44
         NOTE_FS1 =46
         NOTE_G1  =49
         NOTE_GS1 =52
         NOTE_A1  =55
         NOTE_AS1 =58
         NOTE_B1  =62
         NOTE_C2  =65
         NOTE_CS2 =69
         NOTE_D2  =73
         NOTE_DS2 =78
         NOTE_E2  =82
         NOTE_F2  =87
         NOTE_FS2 =93
         NOTE_G2  =98
         NOTE_GS2 =104
         NOTE_A2  =110
         NOTE_AS2 =117
         NOTE_B2  =123
         NOTE_C3  =131
         NOTE_CS3 =139
         NOTE_D3  =147
         NOTE_DS3 =156
         NOTE_E3  =165
         NOTE_F3  =175
         NOTE_FS3 =185
         NOTE_G3  =196
         NOTE_GS3 =208
         NOTE_A3  =220
         NOTE_AS3 =233
         NOTE_B3  =247
         NOTE_C4  =262
         NOTE_CS4 =277
         NOTE_D4  =294
         NOTE_DS4 =311
         NOTE_E4  =330
         NOTE_F4  =349
         NOTE_FS4 =370
         NOTE_G4  =392
         NOTE_GS4 =415
         NOTE_A4  =440
         NOTE_AS4 =466
         NOTE_B4  =494
         NOTE_C5  =523
         NOTE_CS5 =554
         NOTE_D5  =587
         NOTE_DS5 =622
         NOTE_E5  =659
         NOTE_F5  =698
         NOTE_FS5 =740
         NOTE_G5  =784
         NOTE_GS5 =831
         NOTE_A5  =880
         NOTE_AS5 =932
         NOTE_B5  =988
         NOTE_C6  =1047
         NOTE_CS6 =1109
         NOTE_D6  =1175
         NOTE_DS6 =1245
         NOTE_E6  =1319
         NOTE_F6  =1397
         NOTE_FS6 =1480
         NOTE_G6  =1568
         NOTE_GS6 =1661
         NOTE_A6  =1760
         NOTE_AS6 =1865
         NOTE_B6  =1976
         NOTE_C7  =2093
         NOTE_CS7 =2217
         NOTE_D7  =2349
         NOTE_DS7 =2489
         NOTE_E7  =2637
         NOTE_F7  =2794
         NOTE_FS7 =2960
         NOTE_G7  =3136
         NOTE_GS7 =3322
         NOTE_A7  =3520
         NOTE_AS7 =3729
         NOTE_B7  =3951
         NOTE_C8  =4186
         NOTE_CS8 =4435
         NOTE_D8  =4699
         NOTE_DS8 =4978
         
         self.beep( NOTE_D5, 100) 
         self.sleep2(80)
         self.beep( NOTE_F5, 100) 
         self.sleep2(80)
         self.beep( NOTE_D6, 200) 
         self.sleep2(250)
  
         self.beep( NOTE_D5, 100) 
         self.sleep2(80)
         self.beep( NOTE_F5, 100) 
         self.sleep2(80)
         self.beep( NOTE_D6, 200)
         self.sleep2(250)
  
         self.beep( NOTE_E6, 200) 
         self.sleep2(200)
         self.beep( NOTE_F6, 100) 
         self.sleep2(100)
         self.beep( NOTE_E6, 100) 
         self.sleep2(80)
         self.beep( NOTE_F6, 100) 
         self.sleep2(80)
         self.beep( NOTE_E6, 100) 
         self.sleep2(80)
         self.beep( NOTE_C6, 100) 
         self.sleep2(80)
         self.beep( NOTE_A5, 100) 
         self.sleep2(300)
  
         self.beep( NOTE_A5, 200) 
         self.sleep2(100)
         self.beep( NOTE_D5, 200) 
         self.sleep2(100)
         self.beep( NOTE_F5, 100) 
         self.sleep2(100)
         self.beep( NOTE_G5, 100) 
         self.sleep2(100)
         self.beep( NOTE_A5, 100) 
         self.sleep2(500)
  
         self.beep( NOTE_A5, 200) 
         self.sleep2(100)
         self.beep( NOTE_D5, 200) 
         self.sleep2(100)
         self.beep( NOTE_F5, 100) 
         self.sleep2(100)
         self.beep( NOTE_G5, 100) 
         self.sleep2(100)
         self.beep( NOTE_E5, 100) 
         self.sleep2(500)
  
  
  
         self.beep( NOTE_D5, 100) 
         self.sleep2(80)
         self.beep( NOTE_F5, 100) 
         self.sleep2(80)
         self.beep( NOTE_D6, 200) 
         self.sleep2(250)
  
         self.beep( NOTE_D5, 100) 
         self.sleep2(80)
         self.beep( NOTE_F5, 100) 
         self.sleep2(80)
         self.beep( NOTE_D6, 200)
         self.sleep2(250)
  
         self.beep( NOTE_E6, 200) 
         self.sleep2(200)
         self.beep( NOTE_F6, 100) 
         self.sleep2(100)
         self.beep( NOTE_E6, 100) 
         self.sleep2(80)
         self.beep( NOTE_F6, 100) 
         self.sleep2(80)
         self.beep( NOTE_E6, 100) 
         self.sleep2(80)
         self.beep( NOTE_C6, 100) 
         self.sleep2(80)
         self.beep( NOTE_A5, 100) 
         self.sleep2(300)
  
         self.beep( NOTE_A5, 200) 
         self.sleep2(100)
         self.beep( NOTE_D5, 200) 
         self.sleep2(100)
         self.beep( NOTE_F5, 100) 
         self.sleep2(100)
         self.beep( NOTE_G5, 100) 
         self.sleep2(100)
         self.beep( NOTE_A5, 300)
         self.sleep2(100)
         self.beep( NOTE_A5, 200)
         self.sleep2(100)
         self.beep( NOTE_D5, 300)
         self.sleep2(2000)
    def storm2(self):
         NOTE_B0  =31
         NOTE_C1  =33
         NOTE_CS1 =35
         NOTE_D1  =37
         NOTE_DS1 =39
         NOTE_E1  =41
         NOTE_F1  =44
         NOTE_FS1 =46
         NOTE_G1  =49
         NOTE_GS1 =52
         NOTE_A1  =55
         NOTE_AS1 =58
         NOTE_B1  =62
         NOTE_C2  =65
         NOTE_CS2 =69
         NOTE_D2  =73
         NOTE_DS2 =78
         NOTE_E2  =82
         NOTE_F2  =87
         NOTE_FS2 =93
         NOTE_G2  =98
         NOTE_GS2 =104
         NOTE_A2  =110
         NOTE_AS2 =117
         NOTE_B2  =123
         NOTE_C3  =131
         NOTE_CS3 =139
         NOTE_D3  =147
         NOTE_DS3 =156
         NOTE_E3  =165
         NOTE_F3  =175
         NOTE_FS3 =185
         NOTE_G3  =196
         NOTE_GS3 =208
         NOTE_A3  =220
         NOTE_AS3 =233
         NOTE_B3  =247
         NOTE_C4  =262
         NOTE_CS4 =277
         NOTE_D4  =294
         NOTE_DS4 =311
         NOTE_E4  =330
         NOTE_F4  =349
         NOTE_FS4 =370
         NOTE_G4  =392
         NOTE_GS4 =415
         NOTE_A4  =440
         NOTE_AS4 =466
         NOTE_B4  =494
         NOTE_C5  =523
         NOTE_CS5 =554
         NOTE_D5  =587
         NOTE_DS5 =622
         NOTE_E5  =659
         NOTE_F5  =698
         NOTE_FS5 =740
         NOTE_G5  =784
         NOTE_GS5 =831
         NOTE_A5  =880
         NOTE_AS5 =932
         NOTE_B5  =988
         NOTE_C6  =1047
         NOTE_CS6 =1109
         NOTE_D6  =1175
         NOTE_DS6 =1245
         NOTE_E6  =1319
         NOTE_F6  =1397
         NOTE_FS6 =1480
         NOTE_G6  =1568
         NOTE_GS6 =1661
         NOTE_A6  =1760
         NOTE_AS6 =1865
         NOTE_B6  =1976
         NOTE_C7  =2093
         NOTE_CS7 =2217
         NOTE_D7  =2349
         NOTE_DS7 =2489
         NOTE_E7  =2637
         NOTE_F7  =2794
         NOTE_FS7 =2960
         NOTE_G7  =3136
         NOTE_GS7 =3322
         NOTE_A7  =3520
         NOTE_AS7 =3729
         NOTE_B7  =3951
         NOTE_C8  =4186
         NOTE_CS8 =4435
         NOTE_D8  =4699
         NOTE_DS8 =4978
         
         self.beep( NOTE_D5, 100) 
         self.sleep2(80)
         self.beep( NOTE_F5, 100) 
         self.sleep2(80)
         self.beep( NOTE_D6, 200) 
         self.sleep2(250)
  
         self.beep( NOTE_D5, 100) 
         self.sleep2(80)
         self.beep( NOTE_F5, 100) 
         self.sleep2(80)
         self.beep( NOTE_D6, 200)
         self.sleep2(250)
  
         self.beep( NOTE_E6, 200) 
         self.sleep2(200)
         self.beep( NOTE_F6, 100) 
         self.sleep2(100)
         self.beep( NOTE_E6, 100) 
         self.sleep2(80)
         self.beep( NOTE_F6, 100) 
         self.sleep2(80)
         self.beep( NOTE_E6, 100) 
         self.sleep2(80)
         self.beep( NOTE_C6, 100) 
         self.sleep2(80)
         self.beep( NOTE_A5, 100) 
         self.sleep2(300)
         