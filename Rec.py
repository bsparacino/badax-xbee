#! /usr/bin/python

from xbee import ZigBee
from Buzzer import Buzzer
import RPi.GPIO as GPIO
from RaspberryPi import RaspberryPi
import time
import serial
import struct
import threading
import thread

class Rec():

    def __init__(self, database, sensorProcess):
        GPIO.setmode(GPIO.BOARD)

        self.database = database;
        self.sp = sensorProcess

    def start(self):
        #------------------------------------------------------------------------------- 
        # Open serial port
        ser = serial.Serial('/dev/ttyAMA0', 9600)
        self.buzzer = Buzzer()

        # Create API object
        xbee = ZigBee(ser,callback = self.print_data ,escaped=True)

        # Continuously read and print packets
        print "Starting"
        #print '\n *****************************'
        #print xbee.api_commands
        #print '\n *****************************'
        #print xbee.api_responses
        #print '\n *****************************'

        MY = self.HexToByte('7Az3')
        ADR = self.HexToByte('0013A2004092D842')

        #0013A2004092D842 sensor1
        #0013A2004092D86A sensor2        

        once = 1
        while True:
            try: 
                
                #xbee.tx(dest_addr=pan,dest_addr_long=Destination, data='Hello World')
                #xbee.remote_at(dest_addr=MY,dest_addr_long=ADR, command='MY',parameter=None)
                #time.sleep(5) \x
                #xbee.send("remote_at",frame_id='A', command='MY')
                
                #
                #xbee.tx(dest_addr='\xbf\x0c',dest_addr_long='\x00\x13\xa2\x00\x40\x92\xd8\x6a', data='Hello World')
                    if once == 1:
                        print 'Discovering Nodes'
                        #xbee.at(frame_id='A', command='MY')
                        #xbee.at(frame_id='A', command='ID')
                        xbee.at(frame_id='D', command='ND')
                    
                    #xbee.remote_at(dest_addr='\xbf\x0c',command='IR',parameter='\xff')
                    #xbee.remote_at(dest_addr='\xbf\x0c',command='V+',parameter='\xff')
                    #xbee.remote_at(dest_addr='\xbf\x0c',command='MY',parameter=None)
                    
                        once = 0
                        time.sleep(5)
                        print 'Sending RAT'
                        #xbee.tx(dest_addr=MY2,dest_addr_long=ADR2, data='Hello World')
                        xbee.remote_at(dest_addr=MY,dest_addr_long=ADR,command='IS')
                        #time.sleep(1)
                        xbee.remote_at(dest_addr=MY,dest_addr_long=ADR,command='IR',parameter='\xFF')
                        #time.sleep(1)
                        xbee.remote_at(dest_addr=MY,dest_addr_long=ADR,command='IR',parameter='\x00')
                        print 'Done'
                    time.sleep(3)
            except KeyboardInterrupt:
                break

        xbee.halt()        
        ser.close()

    #------------------------------------------------------------------------------- 
    def ByteToHex(self, byteStr): 
        """ 
        Convert a byte string to it's hex string representation e.g. for 
        output. """ 
        
        # Uses list comprehension which is a fractionally faster 
        #implementation than # the alternative, more readable, implementation 
        #below    
        #    hex = [] 
        #    for aChar in byteStr: 
        #        hex.append( "%02X " % ord( aChar ) ) 
        # 
        #    return ''.join( hex ).strip()         

        return ''.join( [ "%02X" % ord( x ) for x in byteStr ] ).strip() 

    #-------------------------------------------------------------------------------
    def HexToByte(self, hexStr):
        """
        Convert a string hex byte values into a byte string. The Hex Byte values may
        or may not be space separated.
        """
        # The list comprehension implementation is fractionally slower in this case    
        #
        #    hexStr = ''.join( hexStr.split(" ") )
        #    return ''.join( ["%c" % chr( int ( hexStr[i:i+2],16 ) ) \
        #                                   for i in range(0, len( hexStr ), 2) ] )
     
        bytes = []

        hexStr = ''.join( hexStr.split(" ") )

        for i in range(0, len(hexStr), 2):
            bytes.append( chr( int (hexStr[i:i+2], 16 ) ) )

        return ''.join( bytes )

    #------------------------------------------------------------------------------- 

    def print_data(self, data):
        #print response  
        print '\n *****************************'
        print 'Response recieved:\n',data,'\nEnd Response\n'
        
        if 'frame_id' in data:
            if (data['frame_id'] == "D"):
                print 'NODE DISCOVERY'
        
        if 'status' in data:
            status = self.ByteToHex( data['status'])
            print '\nStatus: ', status
        
        if 'frame_id' in data:
            frame_id = data['frame_id']
            print 'Frame id: ',frame_id ,'/', self.ByteToHex( data['frame_id'])
            
        if 'source_addr_long' in data:
            source_addr_long = self.ByteToHex( data['source_addr_long'])
            print 'Source Adr:'+source_addr_long

        if 'rf_data' in data:
            rf_data = data['rf_data']
            print 'rf data'+rf_data

        if 'samples' in data:
            if 'adc-7' in data['samples'][0]:
                samples = data['samples'][0]['adc-7']
                print 'Testig', self.ByteToHex( str(data['samples'][0]['adc-7']))
                print 'Voltage:',samples, '/', ((1200 * samples) + 512) / 1024 , 'mV'
                print  int('0x'+str(samples),16)

            if 'dio-1' in data['samples'][0]:
                samples = data['samples'][0]['dio-1']
                print 'Sensor:',samples            
                if(samples == True):
                    #buzzer.storm2()
                    #self.buzzer.beep(800, 25)
                    self.sp.start_timer()

                elif(samples == False):                    
                    self.buzzer.beep(659, 125)
                    #self.sp.stop_timer()

                
        if 'parameter' in data:
            if 'status' in data['parameter']:
                status = self.ByteToHex( data['parameter']['status'])
                print 'Status: ', status
            
            if 'source_addr' in data['parameter']:
                source_addr = self.ByteToHex( data['parameter']['source_addr'])
                print 'source_addr: ', source_addr
            
            if 'parent_address' in data['parameter']:
                parent_address = self.ByteToHex( data['parameter']['parent_address'])
                print 'parent_address: ', parent_address
            
            if 'profile_id' in data['parameter']:
                profile_id = self.ByteToHex( data['parameter']['profile_id'])
                print 'profile_id: ', profile_id
            
            if 'source_addr_long' in data['parameter']:
                source_addr_long = self.ByteToHex( data['parameter']['source_addr_long'])
                print 'source_addr_long: ', source_addr_long
            
            if 'device_type' in data['parameter']:
                device_type = self.ByteToHex( data['parameter']['device_type'])
                print 'device_type: ', device_type
            
            if 'node_identifier' in data['parameter']:
                node_identifier = data['parameter']['node_identifier']
                print 'node_identifier: ', node_identifier
            
            if 'manufacturer' in data['parameter']:
                manufacturer = self.ByteToHex( data['parameter']['manufacturer'])
                print 'manufacturer: ', manufacturer

        print '\n *****************************'