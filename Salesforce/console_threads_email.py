from simple_salesforce import Salesforce
import requests
from lxml import html
from tqdm import tqdm
import datetime
import os
import time
import threading

# Import smtplib for the actual sending function
import smtplib

# Import the email modules we'll need
from email.mime.text import MIMEText

class Downloader():
	startTime = datetime.datetime.now()
	stopTime = datetime.datetime.now()
	
	def __init__(self, master=None):
		with open('setup.txt') as setup:
			self.us = setup.readline().strip()
			self.pw = setup.readline().strip()
			self.st = setup.readline().strip()
			self.dp = setup.readline().strip()
			self.ea = setup.readline().strip()
			d = datetime.date(1,1,1)
			d = str(d.today())
			self.dp = self.dp + d + '\\'

			self.threads = 0

	def go(self):
		if not os.path.exists(self.dp):
			os.makedirs(self.dp)
		export_url = 'https://eu4.salesforce.com/ui/setup/export/DataExportPage/d?setupid=DataManagementExport'
		sf = Salesforce(username=self.us, password=self.pw, security_token=self.st)
		self.session = requests.session()
		self.session.cookies.set('sid',sf.session_id)
		self.result = self.session.get(export_url)
		tree = html.fromstring(self.result.content)
		links = tree.findall(".//a[@class='actionLink']")
		print('Download of ' + str(len(links)) + ' files will now start')
		print('Files will be downloaded to:  ' + self.dp)
		self.startTime = datetime.datetime.now()
		for link in links:
			try:
				while self.threads > 5:
					time.sleep(10)
				t = threading.Thread(target=self.downloaderThread, args=(link, self.result, self.session, self.dp))
				self.threads += 1
				t.daemon = True
				t.start()
			except Exception as e:
				print(type(e))     # the exception instance
				print(e.args)      # arguments stored in .args
				print(e)           # __str__ allows args to be printed directly
				#x, y = e.args
				#print('x =', x)
				#print('y =', y)
		print('All downloads started')
		while self.threads > 0:
			time.sleep(5)
			
		try:
			self.stopTime = datetime.datetime.now()
			runTime = self.stopTime - self.startTime
			logString = 'Runtime was ' + str(divmod(runTime.seconds, 60)[0]) + ' minutes and ' + str(divmod(runTime.seconds, 60)[1]) + ' seconds.'
			self.sendEmail(logString)
		except Exception as e:
			print(type(e))     # the exception instance
			print(e.args)      # arguments stored in .args
			print(e)           # __str__ allows args to be printed directly			

	def downloaderThread(self, link, result, session, dp):
		print('Download thread started')
		result = session.get('https://eu4.salesforce.com' + link.get('href'), stream=True)
		with open(dp + link.get('title'), "wb") as handle:
			print('Now downloading file: ' + link.get('title') + 'in 1 MB chunks')
			for data in tqdm(result.iter_content(chunk_size=1048576)):
				handle.write(data)
		self.threads -= 1
		
	def sendEmail(self, logString):
		me = 'mr.download@tele2.com'
		you = self.ea
		msg = MIMEText(logString)
		msg['Subject'] = 'Download of Salesforce Backup data to ' + self.dp + ' completed.'
		msg['From'] = me
		msg['To'] = you
		
		s = smtplib.SMTP('mailrelay.tele2.se')
		s.sendmail(me, [you], msg.as_string())
		s.quit()


app = Downloader()
app.go()
#time.sleep(3)
#app.stopTime = datetime.datetime.now()
#runTime = app.stopTime - app.startTime
#logString = str(divmod(runTime.seconds, 60)[0]) + ' minutes and ' + str(divmod(runTime.seconds, 60)[1]) + ' seconds.'
#app.sendEmail(logString)