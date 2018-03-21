import smtplib
 
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login("vskdtc@gmail.com", "amy1234567890volkmarscharfkatz")
 
msg = "sent with simple PYTHON code"
server.sendmail("vskdtc@gmail.com", "vskdtc@gmail.com", msg)
server.quit()
