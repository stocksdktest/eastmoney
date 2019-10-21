import os
import subprocess
class AndroidDebugBridge(object):
    def call_adb(self, command):
        # TODO check
        command_result = ''
        command_text = 'adb %s' % command
        results = os.popen(command_text, "r")
        while True :
            line = results.readline()
            if not line: break
            command_result += line
        results.close()
        return command_result
    # 拉数据到本地
    def pull(self, remote, local):
        result = self.call_adb("pull %s %s" % (remote, local))
        return result
    #获取连接的设备
    def get_attached_devices(self):
        devices = []
        result = subprocess.Popen("adb devices", shell=True, stdout=subprocess.PIPE,
                                  stderr=subprocess.PIPE).stdout.readlines()

        for item in result:
            t = item.decode().split("\tdevice")
            if len(t) >= 2:
                devices.append(t[0])
        return devices

'''--------------debug------------------
if __name__ == '__main__':
    abdd = AndroidDebugBridge()
    print(abdd.call_adb(""))
    print(abdd.get_attached_devices())
    
'''