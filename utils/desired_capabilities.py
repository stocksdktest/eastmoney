


import os


# Returns abs path relative to this file and not cwd
def PATH(p):
    return os.path.abspath(
        os.path.join(os.path.dirname(__file__), '..', p)
    )

#
#        'noReset': True,
def get_desired_capabilities(app = 'com.eastmoney.android.berlin_8.3_8003000.apk'):
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
    return desired_caps