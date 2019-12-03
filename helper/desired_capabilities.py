


import os


# Returns abs path relative to this file and not cwd
def PATH(p):
    return os.path.abspath(
        os.path.join(os.path.dirname(__file__), '..', p)
    )

#
#        'noReset': True,
# ,
#         'appPackage': 'com.eastmoney.android.berlin',
#         'appActivity': 'com.eastmoney.android.module.launcher.internal.home.HomeActivity'
# 'automationName': 'UIAutomator2',
def get_desired_capabilities(app):
    desired_caps = {
        'platformName': 'Android',
        'deviceName': 'Android Emulator',
        'platformVersion': '8.1',
        'app': PATH('apps/{}'.format(app)),
        'newCommandTimeout': 240,
        'uiautomator2ServerInstallTimeout': 120000,
        'adbExecTimeout': 120000,
        'appPackage': 'com.eastmoney.android.berlin',
        'appActivity': 'com.eastmoney.android.module.launcher.internal.home.HomeActivity',
        'automationName': 'UIAutomator2',
        'androidInstallTimeout': 240000,
        'autoGrantPermissions': True
    }
    #'com.eastmoney.android.module.launcher.internal.home.HomeActivity' com.eastmoney.android.activity.StockActivity

    #print("nowwwwappppp:",PATH('apps/{}'.format(app)))

    return desired_caps