#不理解发邮件为什么会用到pandas，发邮件这个功能有待优化
#邮箱授权码：TWQVJPRXXDLIUTIH

from smtplib import SMTP_SSL
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header

# smtplib模块主要负责发送邮件：是一个发送邮件的动作，连接邮箱服务器，登录邮箱，发送邮件（有发件人，收信人，邮件内容）。
# email模块主要负责构造邮件：指的是邮箱页面显示的一些构造，如发件人，收件人，主题，正文，附件等。

def send_message(content):
    host_server = 'smtp.163.com'  #163邮箱smtp服务器
    sender = 'kirobot@163.com' #发件人邮箱
    pwd = 'TWQVJPRXXDLIUTIH'
    receiver = ['s17865563709@163.com']#收件人邮箱
    mail_title = 'Python自动发送的邮件' #邮件标题
    #mail_content = "自动发送邮件测试" #邮件正文内容
    #函数调用时，mail_content=content

    # 初始化一个邮件主体
    msg = MIMEMultipart()
    msg["Subject"] = Header(mail_title,'utf-8')
    msg["From"] = sender
    msg['To'] = ";".join(receiver)
    msg.attach(MIMEText(mail_content,'plain','utf-8'))  # 邮件正文内容

    smtp = SMTP_SSL(host_server) # ssl登录
    smtp.login(sender,pwd)
    # as_string()是将msg(MIMEText对象或者MIMEMultipart对象)变为str。
    smtp.sendmail(sender,receiver,msg.as_string())

    # quit():用于结束SMTP会话。
    smtp.quit()
if __name__ == '__main__':
    send_message()