import smtplib
import string
import traceback
import sys

fromaddr = 'bbrown@infromatics.uniname.ny.us'
password = 'secretpassword'
toaddrs  = 'myfriend@gmail.com'
server_smtp = 'unismtpserv.uniname.ny.us'
port_smtp = 465

msg = 'Test message ^^'
BODY = string.join((
        "From: %s" % fromaddr,
        "To: %s" % toaddrs,
        "Subject: %s" % 'Hello!!!' ,
        "",
        'What\'s up? :)'
        ), "\r\n")

try :


    server = smtplib.SMTP_SSL(host=server_smtp, port=port_smtp)
    server.set_debuglevel(True)
    server.esmtp_features['auth'] = 'LOGIN PLAIN'
    server.login('bbrown', password)
    server.sendmail(fromaddr, toaddrs, str(BODY))
    server.quit()

except smtplib.SMTPServerDisconnected :
    print "smtplib.SMTPServerDisconnected"
except smtplib.SMTPResponseException, e:
    print "smtplib.SMTPResponseException: " + str(e.smtp_code) + " " + str(e.smtp_error)
except smtplib.SMTPSenderRefused:
    print "smtplib.SMTPSenderRefused"
except smtplib.SMTPRecipientsRefused:
    print "smtplib.SMTPRecipientsRefused"
except smtplib.SMTPDataError:
    print "smtplib.SMTPDataError"
except smtplib.SMTPConnectError:
    print "smtplib.SMTPConnectError"
except smtplib.SMTPHeloError:
    print "smtplib.SMTPHeloError"
except smtplib.SMTPAuthenticationError:
    print "smtplib.SMTPAuthenticationError"
except Exception, e :
    print "Exception", e
    print traceback.format_exc()
    print sys.exc_info()[0]