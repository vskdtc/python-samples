import smtplib

# Use sms gateway provided by mobile carrier:
# at&t:     number@mms.att.net
# t-mobile: number@tmomail.net
# verizon:  number@vtext.com
# sprint:   number@page.nextel.com

server = smtplib.SMTP( "smtp.gmail.com", 587 )

server.starttls()

server.login( 'vskdtc@gmail.com', 'amy1234567890volkmarscharfkatz' )
# Send text message through SMS gateway of destination number
server.sendmail( 'vskdtc@gmail.com', '6502079408@vtext.com', 'Test message' )
