'''
运行主程序
'''
import unittest
import logging, datetime, random
from concurrent.futures.process import ProcessPoolExecutor
from multiprocessing import Pool
from utils.ParametrizedTestCase import ParametrizedTestCase
from utils.AppiumServer import AppiumServer
from utils.adb_utils import AndroidDebugBridge, getPhoneInfo
#from case_class.login import Login
from case_class.quoteDetailRequest import QuoteDetailRequest

# 可以增加加进程池


def runnerCaseApp(params):
    #TODO testcase参数再设计 现在只传了device号  还要传递测试用例参数 和 测试用例类型
    suite = unittest.TestSuite()
    #suite.addTest(ParametrizedTestCase.parametrize(Login, param=devices)) # 扩展的其他的传参测试用例
    if params['request_type'] == 'QuoteDetailRequest':
        for i in range(0, 300):
            suite.addTest(ParametrizedTestCase.parametrize(QuoteDetailRequest, param=params))
    else:
        # 分时和逐笔的例子 登陆
        pass

    #suite.addTest(unittest.TestLoader().loadTestsFromTestCase(Test))  # 添加其他的不用传参的测试用例
    #suite.addTest(unittest.TestLoader().loadTestsFromTestCase(TestTwo))  # 执行顺序就是添加顺序
    unittest.TextTestRunner(verbosity=2).run(suite)

l_devices = []

def runnerPool(caseConfig):
    '''
           根据链接的设备生成不同的dict
           然后放到设备的list里面
           设备list的长度产生进程池大小
        '''
    # devices_Pool = []
    # for i in range(0, len(caseConfig)):
    #     _pool = []
    #     _initApp = {}
    #     _initApp["deviceName"] = caseConfig[i]["devices"]
    #     _initApp["udid"] = caseConfig[i]["devices"]
    #     _initApp["platformVersion"] = getPhoneInfo(devices=_initApp["deviceName"])["release"]
    #     _initApp["platformName"] = "android"
    #     _initApp["port"] = caseConfig[i]["port"]
    #     _initApp["appPackage"] = 'com.aixuetang.online'
    #     _initApp["appActivity"] = 'com.aixuetang.mobile.activities.HomeActivity'
    #     _pool.append(_initApp)
    #     devices_Pool.append(_initApp)
    # pool = Pool(len(devices_Pool))
    # pool.map(runnerCaseApp, devices_Pool)
    # pool.close()
    # pool.join()

    # pool = Pool(len(caseConfig))
    # pool.map(runnerCaseApp, caseConfig)
    # pool.close()
    # pool.join()

    devices_Pool = []
    for i in range(0, len(caseConfig)):
        _initApp = {}
        _initApp = casesConfig[i]
        _initApp["deviceName"] = caseConfig[i]["devices"]
        _initApp["platformVersion"] = getPhoneInfo(devices=_initApp["deviceName"])["release"]
        _initApp["platformName"] = "Android"
        _initApp["port"] = caseConfig[i]["port"]
        _initApp["automationName"] = "UiAutomator2"
        _initApp["systemPort"] = caseConfig[i]["systemPort"]
        _initApp["appPackage"] = 'com.eastmoney.android.berlin'
        _initApp["appActivity"] = 'com.eastmoney.android.module.launcher.internal.home.HomeActivity'
        _initApp["app"] = '/Users/yuanganggang/Documents/UItest/eastmoney_validation/apps/com.eastmoney.android.berlin_8.3_8003000.apk'

        devices_Pool.append(_initApp)
    print(f'devices pool are {devices_Pool}')

    with ProcessPoolExecutor(len(devices_Pool)) as pool:
        pool.map(runnerCaseApp, devices_Pool)


if __name__ == "__main__":
    logging.warning("测试开始执行")
    start_time = datetime.datetime.now()
    devices = AndroidDebugBridge().get_attached_devices()
    casesConfig = []

    param = {}
    # param['port'] = l_devices[0]['port']
    # param['devices'] = l_devices[0]['devices']
    param['request_type'] = 'QuoteDetailRequest'
    param['stock_type'] = 'sh_sz_index'
    param['stock_code'] = '000001.sh'
    casesConfig.append(param)

    param = {}
    # param['port'] = l_devices[0]['port']
    # param['devices'] = l_devices[0]['devices']
    param['request_type'] = 'QuoteDetailRequest'
    param['stock_type'] = 'sh_sz_index'
    param['stock_code'] = '000027.sh'
    casesConfig.append(param)

    param = {}
    # param['port'] = l_devices[0]['port']
    # param['devices'] = l_devices[0]['devices']
    param['request_type'] = 'QuoteDetailRequest'
    param['stock_type'] = 'bond'
    param['stock_code'] = '010303.sh '
    casesConfig.append(param)
    #print(casesConfig)


    param = {}
    # param['port'] = l_devices[0]['port']
    # param['devices'] = l_devices[0]['devices']
    param['request_type'] = 'QuoteDetailRequest'
    param['stock_type'] = 'bond'
    param['stock_code'] = '018006.sh'
    casesConfig.append(param)
    #print(casesConfig)

    param = {}
    # param['port'] = l_devices[0]['port']
    # param['devices'] = l_devices[0]['devices']
    param['request_type'] = 'QuoteDetailRequest'
    param['stock_type'] = 'bond_sh_gz'
    param['stock_code'] = '204001.sh'
    casesConfig.append(param)

    param = {}
    # param['port'] = l_devices[0]['port']
    # param['devices'] = l_devices[0]['devices']
    param['request_type'] = 'QuoteDetailRequest'
    param['stock_type'] = 'bond_sh_gz'
    param['stock_code'] = '204002.sh'
    casesConfig.append(param)

    param = {}
    # param['port'] = l_devices[0]['port']
    # param['devices'] = l_devices[0]['devices']
    param['request_type'] = 'QuoteDetailRequest'
    param['stock_type'] = 'bond_sh_gz'
    param['stock_code'] = '204003.sh'
    casesConfig.append(param)

    param = {}
    # param['port'] = l_devices[0]['port']
    # param['devices'] = l_devices[0]['devices']
    param['request_type'] = 'QuoteDetailRequest'
    param['stock_type'] = 'fund_ETF'
    param['stock_code'] = '512760.sh'
    casesConfig.append(param)

    param = {}
    # param['port'] = l_devices[0]['port']
    # param['devices'] = l_devices[0]['devices']
    param['request_type'] = 'QuoteDetailRequest'
    param['stock_type'] = 'sh_sz'
    param['stock_code'] = '600000.sh'
    casesConfig.append(param)

    param = {}
    # param['port'] = l_devices[0]['port']
    # param['devices'] = l_devices[0]['devices']
    param['request_type'] = 'QuoteDetailRequest'
    param['stock_type'] = 'sh_sz'
    param['stock_code'] = '601688.sh'
    casesConfig.append(param)

    param = {}
    # param['port'] = l_devices[0]['port']
    # param['devices'] = l_devices[0]['devices']
    param['request_type'] = 'QuoteDetailRequest'
    param['stock_type'] = 'sh_sz'
    param['stock_code'] = '900902.sh'
    casesConfig.append(param)


    param = {}
    # param['port'] = l_devices[0]['port']
    # param['devices'] = l_devices[0]['devices']
    param['request_type'] = 'QuoteDetailRequest'
    param['stock_type'] = 'sh_sz'
    param['stock_code'] = '900903.sh'
    casesConfig.append(param)

    param = {}
    # param['port'] = l_devices[0]['port']
    # param['devices'] = l_devices[0]['devices']
    param['request_type'] = 'QuoteDetailRequest'
    param['stock_type'] = 'sh_sz'
    param['stock_code'] = '900911.sh'
    casesConfig.append(param)

    param = {}
    # param['port'] = l_devices[0]['port']
    # param['devices'] = l_devices[0]['devices']
    param['request_type'] = 'QuoteDetailRequest'
    param['stock_type'] = 'sh_sz'
    param['stock_code'] = '900913.sh'
    casesConfig.append(param)

    param = {}
    # param['port'] = l_devices[0]['port']
    # param['devices'] = l_devices[0]['devices']
    param['request_type'] = 'QuoteDetailRequest'
    param['stock_type'] = 'option'
    param['stock_code'] = '10001926.sh'
    casesConfig.append(param)

    # print(len(casesConfig))
    # exit(1)
    if len(devices) > 0:
        # bpint = 2251
        portint = 4700
        bpint = 4750
        systemPortint = 4800
        for dev in devices:
            # app = {}
            # app["devices"] = dev
            # app["port"] = str(random.randint(4593, 4598))
            # app["bp"] = str(bpint)
            # bpint += 1

            app = {}
            app["devices"] = dev
            # app["port"] = str(random.randint(4700, 4900))
            # app["bp"] = str(random.randint(4700, 4900))
            # app["systemPort"] = random.randint(4700, 4900)
            app["port"] = str(portint)
            app["bp"] = str(bpint)
            app["systemPort"] = systemPortint

            portint += 1
            bpint += 1
            systemPortint += 1

            l_devices.append(app)

        print("now l_devices:", len(l_devices))
        appium_server = AppiumServer(l_devices)
        appium_server.start_server()#启动服务
        #runnerPool(l_devices)

        #rcp = runnerCaseApp(l_devices[0]) #先只测试一个appiumServer



        for i in range(len(l_devices)):
            casesConfig[i]['port'] = l_devices[i]['port']
            casesConfig[i]['devices'] = l_devices[i]['devices']
            casesConfig[i]['bp'] = l_devices[i]['bp']
            casesConfig[i]['systemPort'] = l_devices[i]['systemPort']

        #runnerCaseApp(param) #先只测试一个appiumServer
        # runnerPool(l_devices)
        runnerPool(casesConfig[:len(l_devices)])

        try:
            appium_server.stop_server(l_devices)
        except Exception as e:
            logging.warning("关闭服务失败，原因：%s"%e)
        end_time = datetime.datetime.now()
        hour = end_time - start_time
        #create(filename=filenm,devices_list=devicess,Test_version='2.0.1',testtime=str(hour))
        logging.warning("测试执行完毕，耗时：%s"%hour)
    else:
        logging.warning("没有可用的安卓设备")
        print("没有可用的安卓设备")