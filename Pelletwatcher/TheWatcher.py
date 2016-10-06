import requests
import datetime
import os
import sys
import time
import threading
import json
import random

'''
This code can be tested without the Raspberry Pi by using the included testGPIO module instead of RPi module.
The functions listenForStart, listenForStop, startDetected and stopDetected are not doing anything useful.

The program listens for activity on pin 16 by running in an eternal loop.
If it finds that it has gone from 1 to 0 it is a start and a timer is started.
If it finds that it has gone from 0 to 1 it is a stop and the timer is stopped and the result sent to logger. 

Pin 18 is handled in such a way that if it is 0 a value is increased by 7 grams per second.
When data is sent due to Pin 16, the total amount is divided by the amount of time that has 
passed since it first started counting until it was sent. and a total average amount of kilos per day is calculated.

The raspberry Pi connections:

Pin 34 (IO 12)
    |   |----Mitsubishi Control Box--|----------------------|
    |   |                                                   |
    |--------3K Ohm-----------|                             |
                              |                             |
Pin 36 (IO 16)              Pin 2 PWR(5V)                 GROUND
   |                          |                             |
   |                          |                             |
   -----|--3K Ohm-------------                              |
        |---------------------------CONTROL BOX-------------|

When the motor is turned on it connects ground to Pin 16 and it will detect a 0.
When the motor is turned off, the GND circuit is broken and Pin 16 will detect 1.

The program sends data to Loggly.com using identifier received when creating account: 54aa2a22-9d21-4ea7-8518-186e0add55f0
porten4.loggly.com (login and password: "Porten4")

It can also send email, use Email function for this.

It has been measured beforehand that the external screw delivers 410 grams of pellets per minute = 7 grams per second.

'''

from email.mime.text import MIMEText

import smtplib

#import RPi.GPIO as GPIO #Use for production
import testGPIO as GPIO #Use for debugging GPIO

class Reporter():
    
	MitsubishiChannel = 12
	MoellerChannel = 16
	MoellerChannelStartTime = datetime.datetime.now()
	MoellerChannelStopTime = datetime.datetime.now()
	MitsubishiChannelStartTime = datetime.datetime.now()
	MitsubishiChannelStopTime = datetime.datetime.now()
	
	MitsubishiReset = datetime.datetime.now()
	MitsubishiKilos = 0
	
	Today = 0
	
	def __init__(self, master=None):
		pass
					
	def go(self):

		GPIO.setwarnings(False)
		GPIO.setmode(GPIO.BCM)
		GPIO.setup(self.MoellerChannel, GPIO.IN)
		GPIO.setup(self.MitsubishiChannel, GPIO.IN)
		GPIO.cleanup()

		GPIO.setwarnings(True)
		GPIO.setmode(GPIO.BCM)
		GPIO.setup( self.MoellerChannel, GPIO.IN )
		GPIO.setup( self.MitsubishiChannel, GPIO.IN )
		
		print("Watching channels 12 (Mitsubishi EO 04, Externskruv) and 16 (Moeller, Motor M2)")
		lastReadMoellerValue = GPIO.input(self.MoellerChannel)
		lastReadMitsubishiValue = GPIO.input(self.MitsubishiChannel)
		while True:
			try:
				currentMoellerValue = GPIO.input(self.MoellerChannel)
				currentMitsubishiValue = GPIO.input(self.MitsubishiChannel)
				#print("Moeller: " + str(currentMoellerValue) + ", Mitsubishi: " + str(currentMitsubishiValue))
				
				if currentMoellerValue != lastReadMoellerValue and currentMoellerValue == 1:
					stopToStartMoeller = self.MoellerChannelStartTime - self.MoellerChannelStopTime
					logStringMoellerStopToStart = str(divmod(stopToStartMoeller.seconds, 60)[0]) + ':' + str(divmod(stopToStartMoeller.seconds, 60)[1])
					
					logStringMitsubishiConsumption = str(round((self.MitsubishiKilos / (datetime.datetime.now() - self.MitsubishiReset).seconds) * 3600 * 24, 2))
					self.MitsubishiReset = datetime.datetime.now()
					self.MitsubishiKilos = 0
					
					self.MoellerChannelStopTime = datetime.datetime.now()
					runTimeMoeller = self.MoellerChannelStopTime - self.MoellerChannelStartTime
					logStringMoellerRunTime = str(divmod(runTimeMoeller.seconds, 60)[0]) + ':' + str(divmod(runTimeMoeller.seconds, 60)[1])
					
					payload = json.dumps({ 'Moeller-run-time' : logStringMoellerRunTime, 'Moeller-last-off-time' : logStringMoellerStopToStart, 'Mitsubishi-daily-consumption-rate-kilos' : logStringMitsubishiConsumption })
					#print(payload)
					requests.post('http://logs-01.loggly.com/inputs/54aa2a22-9d21-4ea7-8518-186e0add55f0/tag/Pellets/', data=payload)
					
					#print(self.Today)
					#print(datetime.datetime.now().day)
					if datetime.datetime.now().day != self.Today: # Once a day we also send an email, just for show.
						#pass
						self.Today = datetime.datetime.now().day
						self.sendEmail(payload) #enable and enter credentials in sendMail function to use this.
					
				elif currentMoellerValue != lastReadMoellerValue and currentMoellerValue == 0:
					self.MoellerChannelStartTime = datetime.datetime.now()

				if currentMitsubishiValue == 0:
					self.MitsubishiKilos += 0.007 #per second!!!, depends on time.sleep() below.

				lastReadMoellerValue = currentMoellerValue
				lastReadMitsubishiValue = currentMitsubishiValue
				time.sleep(1)
			except Exception as detail:
				payload = json.dumps({ 'Exception' : str(detail) })
				#print(payload)
				requests.post('http://logs-01.loggly.com/inputs/54aa2a22-9d21-4ea7-8518-186e0add55f0/tag/ERROR/', data=payload)
				#exit(0)
				os.system('sudo shutdown -r now')


	def end():
		GPIO.cleanup()

	def sendEmail(self,payload):
	
		me = 'Pelletspannan'
		you = 'brfporten4@gmail.com'
		msg = MIMEText(payload)
		msg['Subject'] = 'PELLETSRAPPORT'
		msg['From'] = me
		msg['To'] = you
		
		try:
			s = smtplib.SMTP('smtp.gmail.com:587')
			s.starttls()
			s.login('pannapellets@gmail.com', 'P0rten44')
			s.sendmail(me, [you], msg.as_string())
			s.quit()
		except Exception as detail:
			print(str(detail))
		
rep = Reporter()
<<<<<<< HEAD
rep.go()
=======
rep.go()
>>>>>>> 8f928c6... Added Easy512, made Mitsubishi code send val, not str
