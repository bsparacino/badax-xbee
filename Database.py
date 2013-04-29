#!/usr/bin/python
import MySQLdb
import MySQLdb.cursors
import sys

class Database:

	def __init__(self):  
		self.con = MySQLdb.connect(host="localhost", user="root", passwd="badax", db="badax", cursorclass=MySQLdb.cursors.DictCursor)

	def check_login(self, pin):
		
		cur = self.con.cursor()
		cur.execute("SELECT first_name, last_name FROM users WHERE pin='"+pin+"'")

		u = ''
		if cur.rowcount:
			user = cur.fetchone()
			return user
		else:
			u = 'Invalid Code'

		cur.close()
		return u

	def system_status(self):
		self.con = MySQLdb.connect(host="localhost", user="root", passwd="badax", db="badax", cursorclass=MySQLdb.cursors.DictCursor)
		cur = self.con.cursor()
		cur.execute("SELECT field, value FROM system WHERE field='status'")
		row = cur.fetchone()
		print row
		return row['value']

	def system_arm(self):
		cur = self.con.cursor()
		cur.execute("UPDATE system SET value='1' WHERE field='status'")
		self.con.commit()

	def system_disarm(self):
		cur = self.con.cursor()
		cur.execute("UPDATE system SET value='0' WHERE field='status'")
		self.con.commit()

	def get_users(self):
		cur = self.con.cursor()
		cur.execute("SELECT first_name, last_name, email, phone, alert FROM users")
		users = cur.fetchall()
		return users

	def get_sensor(self, sensorId):
		cur = self.con.cursor()
		cur.execute("SELECT sensor_types.title AS type,sensors.title AS title,sensors.status FROM sensors,sensor_types WHERE sensors.serial='"+sensorId+"' AND sensors.type=sensor_types.id AND sensors.status='1' ")
		sensor = cur.fetchone()
		return sensor

	def log(self, message):
		cur = self.con.cursor()
		cur.execute("INSERT INTO logs (message) VALUES ('"+message+"')")
		self.con.commit()

		print message

	def cleanup(self):
		self.con.close()