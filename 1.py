import os 
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEImage import MIMEImage
from email.MIMEBase import MIMEBase
from email import Encoders
import outlook
import time


gmail_user = "llynch701@gmail.com"
gmail_pwd = "12345qwert@321"

Yahoo_user = "kleineschlampe89@yahoo.de"
Yahoo_pwd = "0147852qwert"

hotmail_user = "martin_trigaux@hotmail.com"
hotmail_pwd = "apple@123"

files = "Z:/11/share/file/mail/file/"
file = open("output.txt", "a")
filenames = [os.path.join(files)] 

file.write("\n-----------------------------------------------------------------------------gmail Report-------------------------------------------------\n")
file.write(time.strftime("%I:%M:%S")+ "\n"+time.strftime("%d/%m/%Y")+"\n")

for filenames in os.listdir(files):	
		
		print(filenames+" gmail")
			 
		recipients = [gmail_user , Yahoo_user, hotmail_user]

		def mail(to, subject, text, attach):
		   msg = MIMEMultipart()
		   msg['From'] = gmail_user
		   msg['To'] = ", ".join(recipients)
		   msg['Subject'] = subject

		   msg.attach(MIMEText(text))

		   try :	
			   part = MIMEBase('application', 'octet-stream')
			   part.set_payload(open(files+filenames, 'rb').read())
			   Encoders.encode_base64(part)
			   part.add_header('Content-Disposition', 'attachment; filename="%s"' % files+filenames)
			   msg.attach(part)
				
			   mailServer = smtplib.SMTP("smtp.gmail.com", 587)
			   mailServer.ehlo()
			   mailServer.starttls()
			   mailServer.ehlo()
			   mailServer.login(gmail_user, gmail_pwd)
			   mailServer.sendmail(gmail_user, to, msg.as_string())
			   # Should be mailServer.quit(), but that crashes...
			   mailServer.close()
			   print "pass"
			   file.write( filenames+"					is pass \n ")
			   
		   except:
			   print "Detected"
			   file.write( filenames+" 					is Detected \n ")
		mail(recipients,"Todays report","Test email", filenames)
		
file.write("\n-----------------------------------------------------------------------------Yahoo Report------------------------------------------------\n")
file.write(time.strftime("%I:%M:%S")+ "\n"+time.strftime("%d/%m/%Y")+"\n")

for filenames in os.listdir(files):	
	
	print (filenames+" yahoo")
	
	recipients = [gmail_user , Yahoo_user, hotmail_user]

	#Create Module
	def mail(to, subject, text, attach):
	   msg = MIMEMultipart()
	   msg['From'] = Yahoo_user
	   msg['To'] = ", ".join(recipients)
	   msg['Subject'] = subject

	   msg.attach(MIMEText(text))
	
	   try :	
		   part = MIMEBase('application', 'octet-stream')
		   part.set_payload(open(files+filenames, 'rb').read())
		   Encoders.encode_base64(part)
		   part.add_header('Content-Disposition', 'attachment; filename="%s"' % files+filenames)
		   msg.attach(part)
			
		   mailServer = smtplib.SMTP("smtp.mail.yahoo.com", 587)
		   mailServer.ehlo()
		   mailServer.starttls()
		   mailServer.ehlo()
		   mailServer.login(Yahoo_user, Yahoo_pwd)
		   mailServer.sendmail(Yahoo_user, to, msg.as_string())
		   mailServer.close()
		   print "pass"
		   file.write( filenames+"					 is pass \n ")
		   
	   except:
		   print "Detected"
		   file.write( filenames+"					 is Detected \n ")
	mail(recipients,"Todays report","Test email", filenames)
	
file.write("\n-----------------------------------------------------Hotmail Report-----------------------------------------------------------------------\n")
file.write(time.strftime("%I:%M:%S")+ "\n"+time.strftime("%d/%m/%Y")+"\n")


for filenames in os.listdir(files):	
	
	print (filenames+" outlook")
	
	recipients = [gmail_user , Yahoo_user, hotmail_user]

	#Create Module
	def mail(to, subject, text, attach):
	   msg = MIMEMultipart()
	   msg['From'] = hotmail_user
	   msg['To'] = ", ".join(recipients)
	   msg['Subject'] = subject

	   msg.attach(MIMEText(text))
	
	   try :	
		   part = MIMEBase('application', 'octet-stream')
		   part.set_payload(open(files+filenames, 'rb').read())
		  # Encoders.encode_base64(part)
		   part.add_header('Content-Disposition', 'attachment; filename="%s"' % files+filenames)
		   msg.attach(part)
			
		   mailServer = smtplib.SMTP("smtp-mail.outlook.com", 587)
		   mailServer.ehlo()
		   mailServer.starttls()
		   mailServer.ehlo()
		   mailServer.login(hotmail_user,hotmail_pwd)
		   mailServer.sendmail(Yahoo_user, to, msg.as_string())
		   mailServer.close()
		   print "pass"
		   file.write( filenames+"					 is pass \n ")		   
	   except:
		   print "Detected"
		   file.write( filenames+"					 is Detected \n ")
	mail(recipients,"Todays report","Test email", filenames)
#--------------------------------------------------------------------gmail cleen ------------------------------------------------------------------------
import imaplib
box = imaplib.IMAP4_SSL('imap.gmail.com',993)
box.login(gmail_user,gmail_pwd )

box.select('Inbox')
typ, data = box.search(None, 'ALL')
for num in data[0].split():
		box.store(num, '+FLAGS', '\\Deleted')
		box.expunge()

box.select('[Gmail]/Trash')
typ, data = box.search(None, 'ALL')
for num in data[0].split():
		box.store(num, '+FLAGS', '\\Deleted')
		box.expunge()


box.select('[Gmail]/Spam')			
typ, data = box.search(None, 'ALL')
for num in data[0].split():
		box.store(num, '+FLAGS', '\\Deleted')
		box.expunge()


box.close()
box.logout()

file.write( "\n gmailis all mails are delete \n ")
print "cleen gmail"	
#-------------------------------------outlook------------------------------------------------------------------------------------------------------------------
import imaplib
box = imaplib.IMAP4_SSL('imap-mail.outlook.com',993)
box.login(hotmail_user,hotmail_pwd )

box.select('Inbox')
typ, data = box.search(None, 'ALL')
for num in data[0].split():
		box.store(num, '+FLAGS', '\\Deleted')
		box.expunge()

box.select('Deleted')
typ, data = box.search(None, 'ALL')
for num in data[0].split():
		box.store(num, '+FLAGS', '\\Deleted')
		box.expunge()

box.close()
box.logout()

file.write( "\n hotmail all mails are delete \n ")
print "cleen hotmail"	

#------------------------------------------------------yahoo cleen--------------------------------------------------------------------------------------------

import imaplib
box = imaplib.IMAP4_SSL('imap.mail.yahoo.com',993)
box.login(Yahoo_user,Yahoo_pwd )

box.select('INBOX')
typ, data = box.search(None, 'ALL')
for num in data[0].split():
		box.store(num, '+FLAGS', '\\Deleted')
		box.expunge()

box.select('Trash')
typ, data = box.search(None, 'ALL')
for num in data[0].split():
		box.store(num, '+FLAGS', '\\Deleted')
		box.expunge()

box.close()
box.logout()

file.write( "\n yahoo all mails are delete \n ")
print "cleen yahoo"	