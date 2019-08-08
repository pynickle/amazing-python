import smtplib
from email.mime.text import MIMEText
from email.header import Header
import traceback

def mail(exception):
    sender = 'pynickle@sina.com'
    receivers = 'pynickle@sina.com'
    
    msg = ""
    msg += "<p>Exception happened when others using your cishen application:</p>"
    msg += "<pre><code>" + str(exception) + "</code></pre>"

    message = MIMEText(msg, 'html', 'utf-8')
    message['From'] = sender
    message['To'] =  receivers
    
    subject = 'cishen error occured'
    message['Subject'] = Header(subject, 'utf-8')
    
    try:
        smtp = smtplib.SMTP()
        smtp.connect("smtp.sina.com", 25)
        smtp.login("pynickle@sina.com", "32149d81f58043e6")
        smtp.sendmail(sender, receivers, message.as_string())
        smtp.quit()
        return True
    except Exception as e:
        # traceback.print_exc()
        return False

if __name__ == "__main__":
    mail("error")