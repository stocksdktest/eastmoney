


import os
from appium import webdriver

# Returns abs path relative to this file and not cwd
def PATH(p):
    return os.path.abspath(
        os.path.join(os.path.dirname(__file__), '..', p)
    )

#
#        'noReset': True,

# ,
#         'udid': param["devices"],
#         'systemPort': param["port"]
def get_desired_capabilities(param = None, app = 'com.eastmoney.android.berlin_8.3_8003000.apk'):
    desired_caps = {
        'platformName': 'Android',
        'deviceName': 'Android Emulator',
        'platformVersion': '8.1',
        'app': PATH('apps/{}'.format(app)),
        'newCommandTimeout': 240,
        'automationName': 'UIAutomator2',
        'uiautomator2ServerInstallTimeout': 120000,
        'adbExecTimeout': 120000,
        'appPackage': 'com.eastmoney.android.berlin',
        'appActivity': 'com.eastmoney.android.module.launcher.internal.home.HomeActivity',
        'androidInstallTimeout': 240000,
        'noReset': True
    }
   # print(desired_caps['app'])
    #print("nowwwwport:", param["port"])
    return desired_caps



def connect_device(devices):
    desired_caps = {}
    desired_caps['platformVersion'] = devices["platformVersion"]
    desired_caps['platformName'] = "Android" #devices["platformName"]
    desired_caps["automationName"] = "UiAutomator2" #devices['automationName']
    desired_caps['deviceName'] = devices["devices"] #devices["deviceName"]
    desired_caps["appPackage"] = 'com.eastmoney.android.berlin' #devices["appPackage"]
    desired_caps["appActivity"] = 'com.eastmoney.android.module.launcher.internal.home.HomeActivity' #devices["appActivity"]
    desired_caps["noReset"] = True
    desired_caps['noSign'] = True
    desired_caps["unicodeKeyboard"] = True
    desired_caps["resetKeyboard"] = True
    desired_caps["systemPort"] = devices["systemPort"]

    # desired_caps['app'] = devices["app"]
    remote = "http://127.0.0.1:" + str(devices["port"]) + "/wd/hub"
    # remote = "http://127.0.0.1:" + "4723" + "/wd/hub"
    driver = webdriver.Remote(remote, desired_caps)
    return driver

if __name__ == '__main__':
    get_desired_capabilities()