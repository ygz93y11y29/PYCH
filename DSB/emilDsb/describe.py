# -*- coding:utf-8 -*-
###########################################################################
#                           emil                                          *
###########################################################################
import smtplib
from email import (header)
from email.mime import (text, application, multipart)
import time

def sender_mail():
    smt_p = smtplib.SMTP()
    smt_p.connect(host='smtp.qq.com', port=25)
    sender, password = '2211866596@qq.com', "atuiqvpuiwdiebdj"
    smt_p.login(sender, password)
    receiver_addresses, count_num = [
        '2833379826@qq.com'], 1
    for email_address in receiver_addresses:
        try:
            msg = multipart.MIMEMultipart()
            msg['From'] = "zhenguo"  # 发件人
            msg['To'] = email_address   #发件地址
            msg['subject'] = header.Header('这是邮件主题通知', 'utf-8')  #主题
            msg.attach(text.MIMEText(
                '这是一封测试邮件，请勿回复本邮件~', 'plain', 'utf-8')) #文本内容
            smt_p.sendmail(sender, email_address, msg.as_string())
            time.sleep(10)
            print('第%d次发送给%s' % (count_num, email_address))
            count_num = count_num + 1
        except Exception as e:
            print('第%d次给%s发送邮件异常' % (count_num, email_address))
            continue
    smt_p.quit()

sender_mail()