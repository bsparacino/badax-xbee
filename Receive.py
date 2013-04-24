#!/usr/bin/python
import MySQLdb
import MySQLdb.cursors
import time
import threading
import thread
from Buzzer import Buzzer
from twilio.rest import TwilioRestClient
import smtplib
from email.mime.text import MIMEText
import string

class Receive():	

	def trip_sensor(self,sensorId):
		self.cancelTimer = 0
		self.timeout = 10

		con = MySQLdb.connect(host="localhost", user="root", passwd="badax", db="badax", cursorclass=MySQLdb.cursors.DictCursor)
		cur = con.cursor()
		cur.execute("SELECT sensor_types.title AS type,sensors.title AS title,sensors.status FROM sensors,sensor_types WHERE sensors.serial='"+sensorId+"' AND sensors.type=sensor_types.id")

		sensor = cur.fetchone()
		if(sensor and sensor['status']):
			print 'tripped sensor: '+sensor['title']
			print sensor['type'] 
			if(sensor['type'] == 'Door'):
				print 'sensor type: Door'

				t = threading.Thread(target=self.start_timer, args=(self.timeout,))
				t.start()
				#self.start_timer(5)
				print 'yay'

				#time.sleep(5)
				# correct code entered, cancel the timer
				#self.cancelTimer = 1

			elif(sensor['type'] == 'Window'):
				print 'sensor type: Window'
				# sound alarm
				print 'BEEP'

			elif(sensor['type'] == 'Room'):
				print 'sensor type: Room'
				# sound alarm
				print 'BEEP'
		else:
			print 'sensor not found'

		cur.close ()
		con.close ()

	def start_timer(self,timeout):
		self.cancelTimer = 0

		while timeout > 0:
			# correct code entered
			if self.cancelTimer:
				break
			# sleep
			else:
				print(timeout)
				timeout -=1
				time.sleep(1)

		# send alerts
		if(self.cancelTimer == 0):
			self.alert()

	def stop_timer(self):
		self.cancelTimer = 1

	def alert(self):
		print 'sending alerts'

		buzzer = Buzzer()
		buzzer.beep(659, 125)

		#client = TwilioRestClient("ACc4cb12c713e1483cb661100848c562b8", "c829b7d4169070c10e5121f0a55180af")
		#message = client.sms.messages.create(to="+15856940209", from_="+15855981936", body="BADAX Test")

		SUBJECT = "BADAX Alerts"
		TO = "bsparacino@gmail.com"
		FROM = "BADAX@gmail.com"
		text = "testing alerts 123"
		BODY = string.join((
		        "From: %s" % FROM,
		        "To: %s" % TO,
		        "Subject: %s" % SUBJECT ,
		        "",
		        text
		        ), "\r\n")
		mailServer = smtplib.SMTP('smtp.gmail.com')
		mailServer.starttls()
		mailServer.login('badaxalerts@gmail.com', 'sourfarm39')
		mailServer.sendmail(FROM, [TO], BODY)
		mailServer.quit()

		
		
