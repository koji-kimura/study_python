from email import message
import smtplib

smtp_host = 'smtp.live.com'
smtp_port = 587
# 捨てアカウント
to_email = 'npug310ghhqp@sute.jp'
from_email = 'npug310ghhqp@sute.jp'
username = 'test'
password = 'test'

msg = message.EmailMessage()
msg.set_content('test email')
msg['Subject'] = 'test email sub'
msg['From'] = from_email
msg['To'] = to_email

server = smtplib.SMTP(smtp_host, smtp_port)
server.ehlo()
server.starttls()
server.ehlo()
server.login(username, password)
server.send.message(msg)
server.quit()
