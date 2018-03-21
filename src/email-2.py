import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEBase import MIMEBase
from email import encoders
 
fromaddr = "vskdtc@gmail.com"
toaddr = "vskdtc@gmail.com"
 
msg = MIMEMultipart()
 
msg['From'] = 'vskdtc@gmail.com'
msg['To'] = 'vskdtc@gmail.com'
msg['Subject'] = "PYTHON"
 
body = "HELLO"
 
msg.attach(MIMEText(body, 'plain'))
 
filename = "female.txt"
attachment = open("/Users/vskdtc/Documents/female.txt", "rb")
 
part = MIMEBase('application', 'octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
 
msg.attach(part)
 
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(fromaddr, "amy1234567890volkmarscharfkatz")
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
server.quit()
