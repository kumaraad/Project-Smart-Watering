import RPi.GPIO as GPIO
import smtplib #SMTP library used to send the email notification
import time # Time library to use the sleep function

user = "d92841fe7d8320" # smtp username 
password = "56c5ae3c85f36f" # smtp password
host = "smtp.mailtrap.io" #smtp host
port = 465 # smtp port

sender = "from@smtp.mailtrap.io" # smtp sender email address
receiver = "kumaraad@deakin.edu.au" # smtp receiver email address

message_nomoisture = """
Subject: Moisture Sensor Notification

No moisture detected!  :'(
"""



message_moisture = """
Subject: Moisture Sensor Notification

Sufficient Moisture :)
"""

def sendEmail(smtp_text):
	try:
		Object = smtplib.SMTP(host, port)
		Object.login(user, password)
		Object.sendmail(sender, receiver, smtp_text)         
		print "Sent via email"
	except smtplib.SMTPException:
		print "Unsuccessful sending email"


def callback(input):  
	if GPIO.input(input):
		print "LED off"
		sendEmail(message_nomoisture)
	else:
		print "LED on"
        sendEmail(message_moisture)

GPIO.setmode(GPIO.BCM)

#GPIO pin for output from sensor
input = 17
#GPIO pin for input
GPIO.setup(input, GPIO.IN)

GPIO.add_event_detect(input, GPIO.BOTH, bouncetime=300)

GPIO.add_event_callback(input, callback)

#Script running
while True:
	time.sleep(0.5)
