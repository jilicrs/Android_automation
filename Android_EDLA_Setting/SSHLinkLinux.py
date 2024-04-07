"""
!/usr/bin/env python
-*- coding:utf-8 -*-
@Time      :2024/2/28 14:17
@Author    :risheng.chen@lango-tech.cn
@File      :SSHLinkLinux.py
__version__ = '1.0.0'
"""

import paramiko
from paramiko.ssh_exception import NoValidConnectionsError
from paramiko.ssh_exception import AuthenticationException
from configparser import ConfigParser

class SSHLink(object):

    config = ConfigParser()
    config.read('config.ini', encoding='utf-8')

    HOST = config.get('SSH_DATABASE', 'HOST')
    PORT = config.getint('SSH_DATABASE', 'PORT')
    USER = config.get('SSH_DATABASE', 'USER')
    PASSWORD = config.get('SSH_DATABASE', 'PASSWORD')


    def __init__(self,  hostname = HOST,
                        port = PORT,
                        username = USER,
                        password = PASSWORD):
        try:
            self.ssh = paramiko.SSHClient()
            self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            self.ssh.connect(
                hostname=hostname,
                port=port,
                username=username,
                password=password
            )
        except NoValidConnectionsError as UserNotFind:
            print(f'用户名错误{UserNotFind}')
        except AuthenticationException as PasswordError:
            print(f'密码错误{PasswordError}')
        except Exception as ConnectError:
            print(f'SSH连接异常{ConnectError}')


    def SSHDisconnect(self):
        """
        SSHDisconnect:关闭远程SSH连接
        :return:
        """
        self.ssh.close()
        print('关闭SSH连接')


    def SSHSendCMD(self, cmd, info=True, error=True):
        """
        SSHSendCMD: 执行远程命令，注：cd是一个shell内置命令，无法直接通过Paramiko执行，需要添加额外的命令前缀来模拟cd命令的行为
                    例如：cd GMS-Tool-MCD && ls 才会进入GMS-Tool-MCD
                    edla测试脚本目录：cd GMS-Tool-MCD && cd EDLA_AUTO_TEST &&
        :param cmd: 远程命令
        :param info:
        :param error:
        :return:
        """
        if cmd == 'down':
            SSHLink().SSHDisconnect()
            return True
        else:
            print('\n' + f"-------->开始执行命令:{str(cmd)}" + '\n')
            stdin, stdout, stderr = self.ssh.exec_command(cmd, get_pty=True)
            result = stdout.read().decode('utf-8')
            stderr = stderr.read().decode('utf-8')
            if result and info:
                print(result)
                if 'Sts Test finished' in result:
                    return True

            elif stderr and error:
                print(stderr)
                return True
            print('\n' + "=============== 命令执行完成 ===============" + '\n')



def RunStsCase():
    """
    跑sts测试
    :return:
    """
    SSHLink().SSHSendCMD(cmd='cd GMS-Tool-MCD && cd EDLA_AUTO_TEST && ./sts.sh')



def MoreSend():
    """
    多命令执行
    :return:
    """
    # cd GMS-Tool-MCD && cd CTS && cd android-cts && cd tools && ls && ./cts-tradefed
    # ./GMS-Tool-MCD/CTS/android-cts/tools/cts-tradefed
    # chmod +777 /GMS-Tool-MCD/CTS/android-cts/tools/cts-tradefed && ./cts-tradefed
    while True:
        if SSHLink().SSHSendCMD(cmd=input('输入命令：')):
            break

