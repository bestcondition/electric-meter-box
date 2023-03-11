import smtplib
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from config import config


def send_mail(
        to, content, subject,
        host=config.SMTP_HOST,
        port=config.SMTP_PORT,
        user=config.SMTP_USER,
        password=config.SMTP_PASSWORD,
):
    smtp = smtplib.SMTP(host, port=port)
    smtp.ehlo()  # send the extended hello to our server
    smtp.starttls()  # tell server we want to communicate with TLS encryption
    smtp.login(user, password)  # login to our email server

    message = MIMEMultipart()
    message['From'] = Header(user)
    message['To'] = Header(to)
    message['Subject'] = Header(subject, 'utf-8')
    # 设置正文
    message.attach(MIMEText(content, 'plain', 'utf-8'))
    smtp.sendmail(user, to, message.as_string())
    smtp.quit()  # finally, don't forget to close the connection
