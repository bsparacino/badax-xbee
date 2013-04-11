# Imports
import time
import RPi.GPIO as GPIO
from RaspberryPi import RaspberryPi


class Buzzer:

    def __init__(self):
        self.pins = [RaspberryPi.SDA, RaspberryPi.SCL]

        for pin in self.pins:
            GPIO.setup(pin, GPIO.OUT)
        #self.boop()
        self.mario()
        #self.beepLoop()

    def beep(self):
        PIN = RaspberryPi.SDA
        BUZZER_REPETITIONS = 20
        BUZZER_DELAY = 0.001
        PAUSE_TIME = 0.05

        #GPIO.setmode(GPIO.BCM)
        #GPIO.setup(pin, GPIO.OUT)

        while False:
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

    def beep3(self, hz, ms):

        print 'beep ' + str(hz) + 'hz ' + str(ms) + 'ms'
        DELAY_OFFSET = 11
        us = (500000 / hz) - DELAY_OFFSET
        rep = (ms * 500) / (us + DELAY_OFFSET)

        sleep_time = us/1000000.0

        for i in range(0, rep):
            GPIO.output(RaspberryPi.SDA, True)
            GPIO.output(RaspberryPi.SCL, False)
            time.sleep(sleep_time)
            GPIO.output(RaspberryPi.SDA, False)
            GPIO.output(RaspberryPi.SCL, True)
            time.sleep(sleep_time)

    def beepLoop(self):
        for i in range(0, 100000):
            print i
            self.beep3(2000, 100)
            time.sleep(.10)

    def boop(self):
        print 'boop'
        for _ in xrange(5):
            for value in [True, False]:
                GPIO.output(RaspberryPi.SDA, value)
                time.sleep(0.001)
        time.sleep(0.05) 

    def mario(self):

        C   = 1911
        C1  =  1804
        D   = 1703
        Eb  =  1607
        E   = 1517
        F   = 1432
        F1  = 1352
        G   = 1276
        Ab  = 1204
        A   = 1136
        Bb   = 1073
        B    = 1012
        c    =   955
        c1   =   902
        d     =  851
        eb    =  803
        e     =  758
        f     =  716
        f1    =  676
        g     =  638
        ab    =  602
        a     =  568
        bb    =  536
        b     =  506

        print 'MARIO :D'        

        melod = [e, e, e, c, e, g, G, c, G, E, A, B, Bb, A, G, e, g, a, f, g, e, c, d, B, c]
        ritmo = [6, 12, 12, 6, 12, 24, 24, 18, 18, 18, 12, 12, 6, 12, 8, 8, 8, 12, 6, 12, 12, 6, 6, 6, 12]

        #melod = [G, E, D, C, D, E, G, E, D, C, D, E, D, E,G, E, G, A, E, A, G, E, D, C]
        #ritmo = [8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 4, 4, 4, 4, 8, 8, 8, 8, 8, 8, 8, 8, 8, 16]

        #melod = [G, A, G, E, G, A, G, E, c, c, A, B, B, G, A, G, A, c, B, A, G, A, G, E]
        #ritmo = [12, 4, 8, 16, 12, 4, 8, 16, 12, 4, 16, 12, 4, 16, 12, 4, 8, 8, 8, 8, 12, 4, 8, 16]

        #melod = [Bb, G, G, Bb, G, G, Bb, G, G, Bb, G, G, Bb, G, C, G, Bb, G, G, Bb, G, G, Bb, G, G, Bb, G, G, Bb, G, F, D, F, D, G, F, D, C, Bb, G, Bb, C, C1, C, Bb, F, D, Bb, G, F, D, C, Bb, D, C, Bb, G]
        #ritmo = [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4]

        for i in range(0, len(melod)):
            tom = melod[i]
            tempo = ritmo[i]

            print str(tom) + ' - ' + str(tempo)
     
            vel = 20000
            tempo_value = tempo * vel

            sleep_time = tom/2048000.0

            tempo_gasto = 0;
            while (tempo_gasto < tempo_value):
                tempo_gasto += tom

                GPIO.output(RaspberryPi.SDA, True)
                #GPIO.output(RaspberryPi.SCL, False)
                time.sleep(sleep_time)
                GPIO.output(RaspberryPi.SDA, False)
                #GPIO.output(RaspberryPi.SCL, True)
                time.sleep(sleep_time)

            time.sleep(0.01)
        time.sleep(1)


        
        