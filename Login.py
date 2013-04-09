#!/usr/bin/python
import MySQLdb
import MySQLdb.cursors

class Login:

	def __init__(self):  
		self.con = MySQLdb.connect(host="localhost", user="root", passwd="badax", db="badax", cursorclass=MySQLdb.cursors.DictCursor)

	def check_login(self, pin):
		
		cur = self.con.cursor()
		cur.execute("SELECT first_name, last_name FROM users WHERE pin='"+pin+"'")

		u = ''
		if cur.rowcount:
			user = cur.fetchone()
			print user['first_name']+' '+user['last_name']
			u = 'Login Successful:\n'+user['first_name']+' '+user['last_name']
		else:
			u = 'Invalid Code'

		cur.close()
		return u

	def cleanup(self):
		self.con.close()