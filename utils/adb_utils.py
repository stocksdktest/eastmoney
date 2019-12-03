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


def getPhoneInfo(devices):
    '''获取设备的一些基本信息'''
    cmd = "adb -s " + devices +" shell cat /system/build.prop "
    phone_info = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).stdout.readlines()
    release = "ro.build.version.release=" # 版本
    model = "ro.product.model=" #型号
    brand = "ro.product.brand=" # 品牌
    device = "ro.product.device=" # 设备名
    result = {"release": release, "model": model, "brand": brand, "device": device}
    for line in phone_info:
         for i in line.split():
            temp = i.decode()
            if temp.find(release) >= 0:
                result["release"] = temp[len(release):]
                break
            if temp.find(model) >= 0:
                result["model"] = temp[len(model):]
                break
            if temp.find(brand) >= 0:
                result["brand"] = temp[len(brand):]
                break
            if temp.find(device) >= 0:
                result["device"] = temp[len(device) :]
                break
    #LOG.info(result)
    return result



'''--------------debug------------------
if __name__ == '__main__':
    abdd = AndroidDebugBridge()
    print(abdd.call_adb(""))
    print(abdd.get_attached_devices())
    
'''