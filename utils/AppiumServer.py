'''
appiumSever
'''

import os,urllib.request,time
import platform,subprocess,threading
from multiprocessing import Process


class RunServer(threading.Thread):#启动服务的线程
    def __init__(self, cmd):
        threading.Thread.__init__(self)
        self.cmd = cmd
    def run(self):
        os.system(self.cmd)

class AppiumServer(object):
    def __init__(self, kwargs):
        self.kwargs = kwargs

    def run(self, url):
        time.sleep(10)
        response = urllib.request.urlopen(url,timeout=5)
        if str(response.getcode()).startswith('2'):
            return True

    def start_server(self):
        for i in range(0,len(self.kwargs)):
            # cmd = "appium --session-override -p %s  -U %s" % (self.kwargs[i]["port"], self.kwargs[i]["devices"])
            cmd = "appium  --session-override -p %s -bp %s -U %s" % (self.kwargs[i]["port"], self.kwargs[i]["bp"], self.kwargs[i]["devices"])
            # cmd = "appium  -p %s --session-override -U %s" % (self.kwargs[i]["port"],  self.kwargs[i]["devices"])

            if platform.system() == "Windows" :
                t1 = RunServer(cmd)
                p = Process(target=t1.start())
                p.start()
                while True:
                    time.sleep(4)
                    if self.run("http://127.0.0.1:" + self.kwargs[i]["port"] + "/wd/hub/status"):
                        LOG.info("-------win_server_ 成功--------------")
                        break
            #TODO check in windows

            else :
                appium = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, bufsize=1,
                                           close_fds=True)
                while(True):
                    appium_result = appium.stdout.readline().strip().decode()
                    #print("appium_result:",appium_result)
                    time.sleep(2)
                    print("-----------start_server-----------")
                    if "listener started" in appium_result or "Error:listen" in appium_result :
                        print("-------server启动成功: %s---------" % self.kwargs[i]["port"])
                        break


    def stop_server(self, devices : list):
        sysstr = platform.system()
        print("devices:",devices,type(devices))#
        if sysstr == 'Windows':
            os.popen("taskkill /f /im node.exe")
            #TODO check in windows
        else:
            for device in devices:
                cmd = "lsof -i :{0}".format(device["port"])
                plist = os.popen(cmd).readlines()
                plisttmp = plist[1].split("    ")
                plists = plisttmp[1].split(" ")
                os.popen("kill -9 {0}".format(plists[0]))
                print("--------sever已关闭-------")



'''------debug in MacOS------'''
if __name__ ==  "__main__":
    app = {}
    app["port"] = 4726
    app["devices"] = "2a2930f7d71"
    appl = []
    appl.append(app)
    hh = AppiumServer(appl)
    hh.start_server()
    hh.stop_server(appl)



