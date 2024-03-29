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

	def __init__(self, led):
		self.database = database = Database()
		self.timeout = 60
		self.timeout_thread = threading.Thread(target=self.start_timer_process, args=(self.timeout,))
		self.soundingAlarm = 0
		self.buzzer = Buzzer()
		self.led = led
		self.led_status_thread = threading.Thread(target=self.led.status_light)
		self.led_status_thread.start()
		self.sensor = None

	def trip_sensor(self,sensorId):
		self.cancelTimer = 0

		status = self.database.system_status()
		print 'system status '+status

		if(status=='1'):

			sensor = self.database.get_sensor(sensorId)
			self.sensor = sensor	

			if(sensor and sensor['status']):

				if(self.soundingAlarm == 0):
					self.buzzer.beep(659, 125)

				message = "Sensor Tripped: "+sensor['title']
				self.database.log(message)

				print 'tripped sensor: '+sensor['title']
				print sensor['type'] 
				if(sensor['type'] == 'Door'):
					self.start_timer()
					print 'sensor type: Door'

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
		else:
			self.buzzer.beep(800, 20)
			time.sleep(0.1)
			self.buzzer.beep(800, 20)

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
				self.buzzer.beep(800, 25)

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

		if(self.soundingAlarm == 0):

			self.alarmSound_thread = threading.Thread(target=self.sound_alarm)
			self.alarmSound_thread.start()

			users = self.database.get_users()		

			client = TwilioRestClient("ACc4cb12c713e1483cb661100848c562b8", "c829b7d4169070c10e5121f0a55180af")

			for user in users:
				
				if(user['alert'] == 0):
					continue;

				message = self.sensor['title']+' Sensor Tripped'
				client.sms.messages.create(to=user['phone'], from_="+15855981936", body=message)

				SUBJECT = "BADAX Alerts"
				TO = user['email']
				FROM = "BADAX@gmail.com"
				BODY = string.join((
				        "From: %s" % FROM,
				        "To: %s" % TO,
				        "Subject: %s" % SUBJECT ,
				        "",
				        message
				        ), "\r\n")
				mailServer = smtplib.SMTP('smtp.gmail.com')
				mailServer.starttls()
				mailServer.login('badaxalerts@gmail.com', 'sourfarm39')
				mailServer.sendmail(FROM, [TO], BODY)
				mailServer.quit()

	def sound_alarm(self):
		self.led.show_status_light = 0
		if(self.soundingAlarm == 0):
			self.soundingAlarm = 1
			while(self.soundingAlarm):
				self.buzzer.beep(800, 100)
				time.sleep(0.1)
