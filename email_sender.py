import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def sendmail(subject, msg, toaddrs, fromaddr, smtpserver, password):
    mail_msg = MIMEMultipart()
    mail_msg['Subject'] = subject
    mail_msg['From'] = fromaddr
    mail_msg['To'] = ','.join(toaddrs)
    mail_msg.attach(MIMEText(msg, 'html', 'utf-8'))

    try:
        s = smtplib.SMTP_SSL(smtpserver)
        s.connect(smtpserver, 465)  # 连接smtp服务器
        s.login(fromaddr, password)  # 登录邮箱
        s.sendmail(fromaddr, toaddrs, mail_msg.as_string())  # 发送邮件
        s.quit()
        print("send successful！")
    except Exception as e:
        print(e)
        print("Failed to send ")
