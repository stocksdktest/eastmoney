'''
运行主程序
'''
import unittest
import logging, datetime, random
from utils.ParametrizedTestCase import ParametrizedTestCase
from utils.AppiumServer import AppiumServer
from utils.adb_utils import AndroidDebugBridge
#from case_class.login import Login
from case_class.quoteDetailRequest import QuoteDetailRequest

# 可以增加加进程池


def runnerCaseApp(params):
    #TODO testcase参数再设计 现在只传了device号  还要传递测试用例参数 和 测试用例类型
    suite = unittest.TestSuite()
    #suite.addTest(ParametrizedTestCase.parametrize(Login, param=devices)) # 扩展的其他的传参测试用例
    if params['request_type'] == 'QuoteDetailRequest':
        suite.addTest(ParametrizedTestCase.parametrize(QuoteDetailRequest, param=params))
    else:
        # 分时和逐笔的例子 登陆
        pass

    #suite.addTest(unittest.TestLoader().loadTestsFromTestCase(Test))  # 添加其他的不用传参的测试用例
    #suite.addTest(unittest.TestLoader().loadTestsFromTestCase(TestTwo))  # 执行顺序就是添加顺序
    unittest.TextTestRunner(verbosity=2).run(suite)

l_devices = []

if __name__ == "__main__":
    logging.warning("测试开始执行")
    start_time = datetime.datetime.now()
    devices = AndroidDebugBridge().get_attached_devices()
    #makecasefile('reg','reg','reg')#没有的时候才会生成，一般都会有这个文件
    #path=os.getcwd()
    #filenm=path+'//testreport//'+'result.xls'

    if len(devices) > 0:
        for dev in devices:
            app = {}
            app["devices"] = dev
            #TODO 控制appium端口不冲突
            app["port"] = str(random.randint(4593, 4598))
            l_devices.append(app)
        appium_server = AppiumServer(l_devices)
        appium_server.start_server()#启动服务
        #runnerPool(l_devices)

        #rcp = runnerCaseApp(l_devices[0]) #先只测试一个appiumServer

        param = {}
        param['port'] = l_devices[0]['port']
        param['devices'] = l_devices[0]['devices']
        param['request_type'] = 'QuoteDetailRequest'
        param['stock_type'] = 'sh_sz'
        param['stock_code'] = '600000.sh'

        runnerCaseApp(param) #先只测试一个appiumServer

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