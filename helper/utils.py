from appium import webdriver



#X = 720
#Y = 1280

'''
唤醒、解锁手机
:param : driver
'''
def wake_up_device(driver):
    X = driver.manage().window().getSize().width
    Y = driver.manage().window().getSize().height
    driver.press_keycode(224)
    driver.swipe( X / 2, Y * 2 / 3,X / 2,Y * 1 / 3)

'''
将网络设置为 Wi-Fi 本地网络 皆可
:param : driver
'''
def set_net_connected(driver):
    driver.set_network_connection(6)


'''
获取当前页面的activity
:param: driver
:return: activity
'''
def get_current_activity(driver):
    return driver.current_activity

'''
获取当前页面源码
:param driver
:return: 返回数据类型为str
'''
def get_current_pagesource(driver):
    return driver.page_source

'''
获取当前窗口的所有context名称
:param driver
:return: 返回当前所有窗口context,可以进行切换，switch_to_context()
'''
def get_contexts(driver):
    return driver.contexts

