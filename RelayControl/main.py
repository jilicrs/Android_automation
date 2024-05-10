# This is a sample Python script.
import time

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from RelayDevice import RelayDevice

HOST = "bemfa.com"
PORT = 9501
UID = "80b6d5791d004501ae7218449abf664e"
USER = "alwayskeepmoving@hotmail.com"
PASSWORD = "kk99817749"
topicList = ['PZNS001']
deviceList = []


def print_log(*args, **kwargs):
    print("[MAIN] ", end="")
    print(*args, **kwargs)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    try:
        print_log('start BEMFA_MQTT client')
        for deviceName in topicList:
            for j in range(1):
                device = RelayDevice(HOST, PORT, UID, USER, PASSWORD, deviceName)
                device.setup()
                time.sleep(1)
                device.send_msg(device.CMD_CTRL_RELAY1_ON)
                time.sleep(1)
                device.send_msg(device.CMD_CTRL_RELAY2_ON)
                time.sleep(1)
                device.send_msg(device.CMD_CTRL_RELAY3_ON)
                time.sleep(1)
                device.send_msg(device.CMD_CTRL_RELAY4_ON)
                deviceList.append(device)
                print(deviceList)
                time.sleep(5)
                device.send_msg(device.CMD_CTRL_RELAY1_OFF)
                time.sleep(1)
                device.send_msg(device.CMD_CTRL_RELAY2_OFF)
                time.sleep(1)
                device.send_msg(device.CMD_CTRL_RELAY3_OFF)
                time.sleep(1)
                device.send_msg(device.CMD_CTRL_RELAY4_OFF)
                deviceList.append(device)
                print_log('Create device ' + device.mTopic + ' finish!')
                if j == 0:
                    print('down')
                    break
    except Exception as e:
        print(e)


    

