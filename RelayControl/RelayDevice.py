import paho.mqtt.client as mqtt
import threading
import tkinter as tk


class RelayDevice:
    # 主机
    mHost: str = ""
    # 端口
    mPort: str = ""
    # 授权ID
    mUid: str = ""
    # 用户名
    mUser: str = ""
    # 密码
    mPwd: str = ""
    # 主题
    mTopic: str = ""
    # 设备句柄
    mClient = ""

    # Command - Relay 1
    CMD_CTRL_RELAY1_ON = 'ctl_relay1_on'
    CMD_CTRL_RELAY1_OFF = 'ctl_relay1_off'
    CMD_RELAY1_TOGGLE = 'ctl_relay1_toggle'
    CMD_CHK_RELAY1_DETAIL = 'relay1_detail'

    # Command - Relay 2
    CMD_CTRL_RELAY2_ON = 'ctl_relay2_on'
    CMD_CTRL_RELAY2_OFF = 'ctl_relay2_off'
    CMD_RELAY2_TOGGLE = 'ctl_relay2_toggle'
    CMD_CHK_RELAY2_DETAIL = 'relay2_detail'

    # Command - Relay 3
    CMD_CTRL_RELAY3_ON = 'ctl_relay3_on'
    CMD_CTRL_RELAY3_OFF = 'ctl_relay3_off'
    CMD_RELAY3_TOGGLE = 'ctl_relay3_toggle'
    CMD_CHK_RELAY3_DETAIL = 'relay3_detail'

    # Command - Relay 4
    CMD_CTRL_RELAY4_ON = 'ctl_relay4_on'
    CMD_CTRL_RELAY4_OFF = 'ctl_relay4_off'
    CMD_RELAY4_TOGGLE = 'ctl_relay4_toggle'
    CMD_CHK_RELAY4_DETAIL = 'relay4_detail'

    # Command - Common
    CMD_CHK_ALL_RELAY_STATUS = 'relay_status'
    CMD_SET_RELAY_TIMER = 'set_relay_timer'

    # 定义构造方法：
    def __init__(self, host, port, uid, user, password, topic):
        self.mHost = host
        self.mPort = port
        self.mUid = uid
        self.mUser = user
        self.mPwd = password
        self.mTopic = topic

    # 连接并订阅
    def on_connect(self, client, userdata, flags, rc):
        self.print_log("Connected with result code " + str(rc))
        client.subscribe(self.mTopic)  # 订阅消息

    # 消息接收
    def on_message(self, client, userdata, msg):
        if msg.topic == self.mTopic:
            self.print_log("Recv msg:" + str(msg.payload.decode('utf-8')))

    # 订阅成功
    # def on_subscribe(self, client, userdata, mid, granted_qos):
    #     self.print_log("On Subscribed: qos = %d" % granted_qos)

    # 失去连接
    def on_disconnect(self, client, userdata, rc):
        if rc != 0:
            self.print_log("Unexpected disconnection %s" % rc)

    # loop
    def loop(self):
        self.mClient.loop_forever(timeout=5)

    # 发布消息
    def send_msg(self, msg):
        self.print_log('Send msg:' + msg)
        self.mClient.publish(self.mTopic, payload=msg)

    # 打印日志
    def print_log(self, *args, **kwargs):
        print("[Device:" + self.mTopic + "] ", end="")
        print(*args, **kwargs)



    # 初始化设备
    def setup(self):
        self.print_log('Setup device')
        client = mqtt.Client(self.mUid)
        self.mClient = client
        client.username_pw_set(self.mUser, self.mPwd)
        client.on_connect = self.on_connect
        client.on_message = self.on_message
        # client.on_subscribe = self.on_subscribe
        client.on_disconnect = self.on_disconnect
        client.connect(self.mHost, self.mPort, 60)

        # 单独调用无需创建线程
        # mqtt_thread = threading.Thread(target=self.loop)
        # mqtt_thread.start()




