#!/usr/bin/python
import MySQLdb
import MySQLdb.cursors
import time
import threading
import thread
from Buzzer import Buzzer
from Database import Database
from twilio.rest import TwilioRestClient
import smtplib
from email.mime.text import MIMEText
import string
import sys

class SensorProcess():

	def __init__(self):
		self.database = database = Database()
		self.timeout = 15
		self.timeout_thread = threading.Thread(target=self.start_timer_process, args=(self.timeout,))
		self.soundingAlarm = 0

	def trip_sensor(self,sensorId):
		self.cancelTimer = 0

		status = self.database.system_status()
		print 'system status '+status

		if(status=='1'):
			sensor = self.database.get_sensor(sensorId)			

			if(sensor and sensor['status']):

				message = "Sensor Tripped: "+sensor['title']
				self.database.log(message)

				print sensor

				print 'tripped sensor: '+sensor['title']
				print sensor['type'] 
				if(sensor['type'] == 'Door'):

					self.start_timer()

					print 'sensor type: Door'

					#t = threading.Thread(target=self.start_timer, args=(self.timeout,))
					#t.start()
					#self.start_timer(5)
					print 'yay'

					#time.sleep(5)
					# correct code entered, cancel the timer
					#self.cancelTimer = 1

				elif(sensor['type'] == 'Window'):
					print 'sensor type: Window'
					# sound alarm
					print 'BEEP'
					self.alert()

				elif(sensor['type'] == 'Room'):
					print 'sensor type: Room'
					# sound alarm
					print 'BEEP'
					self.alert()
			else:
				print 'sensor not found'

	def start_timer(self):
		print 'trying to start timer'		

		if(self.timeout_thread.isAlive()==False):
			try:
				print 'START TIMER'
				self.timeout_thread = threading.Thread(target=self.start_timer_process, args=(self.timeout,))
				self.timeout_thread.start()
			except:
				print 'Trouble with t1 synchronizer'

						
		
	def start_timer_process(self,timeout):
		self.cancelTimer = 0
		
		timeout = timeout*10
		while timeout > 0:

			if(timeout % 4 == 0):
				buzzer = Buzzer()
				buzzer.beep(800, 25)

			# correct code entered
			if self.cancelTimer:
				break
			# sleep
			else:
				print(timeout)
				timeout -=1

				# need a small time otherwise it takes too long to stop the timer
				time.sleep(0.1)

		# send alerts
		if(self.cancelTimer == 0):
			self.alert()

	def stop_timer(self):
		print 'STOP TIMER'
		self.cancelTimer = 1

	def alert(self):
		print 'sending alerts'

		#buzzer = Buzzer()
		#buzzer.beep(659, 125)

		self.alarmSound_thread = threading.Thread(target=self.sound_alarm)
		self.alarmSound_thread.start()

		users = self.database.get_users()		

		client = TwilioRestClient("ACc4cb12c713e1483cb661100848c562b8", "c829b7d4169070c10e5121f0a55180af")

		for user in users:
			
			if(user['alert'] == 0):
				continue;

			message = client.sms.messages.create(to=user['phone'], from_="+15855981936", body="BADAX Test")

			SUBJECT = "BADAX Alerts"
			TO = user['email']
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

	def sound_alarm(self):
		self.soundingAlarm = 1
		buzzer = Buzzer()
		while(self.soundingAlarm):
			buzzer.beep(800, 100)
			time.sleep(0.1)

		
		
