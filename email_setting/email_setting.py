"""
!/usr/bin/env python
-*- coding:utf-8 -*-
@Time      :2023/10/28 10:40
@Author    :risheng.chen@lango-tech.cn
@File      :email_setting.py
__version__ = '1.0.9'
"""

import smtplib
from email.mime.text import MIMEText
from email.header import Header
import datetime

class SendEmail(object):
    def __init__(self, email_user='771109694@qq.com', email_password='oqsjqthbheazbgad'):
        self.sendAddress = email_user
        self.password = email_password
        self.server = smtplib.SMTP_SSL('smtp.qq.com', 465)

    def send_email(self, contents, to_address):
        # 正文
        loginResult = self.server.login(self.sendAddress, self.password)
        print(loginResult)
        content = """
        尊敬的用户：
            {}
        """.format(str('   '+contents))
        # 定义一个可以添加正文的邮件消息对象
        message = MIMEText(content, 'plain', 'utf-8')

        # 发件人昵称和地址
        message['From'] = Header('Test the robot<771109694@qq.com>')
        # 收件人昵称和地址
        message['To'] = Header('陈日升<risheng.chen@lango-tech.cn>')
        message['To'] = Header('陈芳微<fangwei.chen@lango-tech.cn>')
        # 抄送人昵称和地址
        message['Cc'] = Header('')
        message['Cc'] = Header('')
        # 邮件主题
        message['Subject'] = '自动测试执行已完成：'

        try:
            # 发送邮箱
            self.server.sendmail(self.sendAddress,[to_address], message.as_string())
            print('PASS')
            self.server.quit()
        except Exception as e:
            print('Fail:', e )
            self.server.quit()

if __name__ == '__main__':
    SendEmail().send_email(contents='测试：\n'+'               '+
                                    '{}广州市黄浦区{}自动发送邮箱测试执行, 来自朗国第一帅《黄少》'.
                           format(datetime.datetime.now().strftime('%Y/%m/%d %H:%M:%S:'),
                                  datetime.datetime.now().strftime('%m%d')),
                           to_address=('<risheng.chen@lango-tech.cn>',
                                      ))









