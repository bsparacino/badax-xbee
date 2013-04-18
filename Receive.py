#!/usr/bin/python
import MySQLdb
import MySQLdb.cursors
import time
import threading
import thread

class Receive():

	def __init__(self):

		self.cancelTimer = 0

		sensorId = '123aavvbb'
		sensorId = 'abc123'

		con = MySQLdb.connect(host="localhost", user="root", passwd="badax", db="badax", cursorclass=MySQLdb.cursors.DictCursor)
		cur = con.cursor()
		cur.execute("SELECT sensor_types.title AS type,sensors.title AS title,sensors.status FROM sensors,sensor_types WHERE sensors.serial='"+sensorId+"' AND sensors.type=sensor_types.id")

		sensor = cur.fetchone()
		if(sensor['status']):
			print 'tripped sensor: '+sensor['title']

			if(sensor['type'] == 'door'):
				print 'sensor type: Door'

				t = threading.Thread(target=self.start_timer, args=(5,))
				t.start()
				#self.start_timer(5)
				print 'yay'

				time.sleep(2)
				print 'boo'
				#self.cancelTimer = 1


				# wait 60 seconds for successful login, then sound alarm
				#timer = 10
				#while timer > 0:
				#	timer -= 1
				#	print timer
				#	time.sleep(1)

				#print 'BEEP'

			elif(sensor['type'] == 'window'):
				print 'sensor type: Window'
				# sound alarm
				print 'BEEP'

			elif(sensor['type'] == 'room'):
				print 'sensor type: Room'
				# sound alarm
				print 'BEEP'


		cur.close ()
		con.close ()

	

	def start_timer(self,timeout):
		self.cancelTimer = 0
		print "starting timer"

		while timeout > 0:
			if self.cancelTimer:
				break
			else:
				print(timeout)
				timeout -=1
				time.sleep(1)

		if(self.cancelTimer == 0):
			print "BEEEEEP"