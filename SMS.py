from twilio.rest import TwilioRestClient
from Database import Database
import smtplib
from email.mime.text import MIMEText
import string

database = Database()
users = database.get_users()

client = TwilioRestClient("ACc4cb12c713e1483cb661100848c562b8", "c829b7d4169070c10e5121f0a55180af")

for user in users:
	
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