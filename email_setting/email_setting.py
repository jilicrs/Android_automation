"""
!/usr/bin/env python
-*- coding:utf-8 -*-
@Time      :2023/10/28 10:40
@Author    :risheng.chen@lango-tech.cn
@File      :email_setting.py
__version__ = '1.0.0'
"""

import smtplib
from email.mime.text import MIMEText
from email.header import Header

class SendEmail(object):
    def __init__(self):
        self.sendAddress = '771109694@qq.com'
        self.password = 'oqsjqthbheazbgad'
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
        message['From'] = Header('risheng<771109694@qq.com>')
        # 收件人昵称和地址
        message['To'] = Header('Risheng.Chen<risheng.chen@lango-tech.cn>')
        # 抄送人昵称和地址
        message['Cc'] = Header('黄少<shaoping.huang@lango-tech.cn>')
        message['Cc'] = Header('吴少<huiming.wu@lango-tech.cn>')
        # 邮件主题
        message['Subject'] = '自动测试执行已完成：'

        # 发送邮箱
        self.server.sendmail(self.sendAddress,
                             [to_address],
                        message.as_string())
        print('PASS')
        self.server.quit()

if __name__ == '__main__':
    SendEmail().send_email(contents='广州市黄浦区1030自动发送邮箱测试执行, 来自朗国第一帅《黄少》',
                           to_address=('risheng.chen@lango-tech.cn',
                                      'shaoping.huang@lango-tech.cn',
                                      'huiming.wu@lango-tech.cn'))









