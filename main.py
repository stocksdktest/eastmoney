'''
运行主程序
'''
import unittest
import logging, datetime, random
from utils.ParametrizedTestCase import ParametrizedTestCase
from utils.AppiumServer import AppiumServer
from utils.adb_utils import AndroidDebugBridge
from cases.login import Login
from cases.sh_sz import Sh_sz
from cases.sci_tech import Sci_tech
from cases.hk import Hk
from cases.fund import Fund

# 可以增加加进程池

def runnerCaseApp(devices):
    #TODO testcase参数再设计 现在只传了device号  还要传递测试用例参数 和 测试用例类型
    suite = unittest.TestSuite()
    #suite.addTest(ParametrizedTestCase.parametrize(Login, param=devices)) # 扩展的其他的传参测试用例
    suite.addTest(ParametrizedTestCase.parametrize(Sh_sz, param=devices))
    #suite.addTest(ParametrizedTestCase.parametrize(Sci_tech, param=devices))
    #suite.addTest(ParametrizedTestCase.parametrize(Hk, param=devices))
    #suite.addTest(ParametrizedTestCase.parametrize(Fund, param=devices))
    #suite.addTest(unittest.TestLoader().loadTestsFromTestCase(Test))  # 添加其他的不用传参的测试用例
    #suite.addTest(unittest.TestLoader().loadTestsFromTestCase(TestTwo))  # 执行顺序就是添加顺序
    unittest.TextTestRunner(verbosity=2).run(suite)

l_devices = []
if __name__=="__main__":
    logging.warning("测试开始执行")
    start_time=datetime.datetime.now()
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
        rcp=runnerCaseApp(l_devices[0]) #先只测试一个appiumServer

        try:
            appium_server.stop_server(l_devices)
        except Exception as e:
            logging.warning("关闭服务失败，原因：%s"%e)
        end_time=datetime.datetime.now()
        hour=end_time-start_time
        #create(filename=filenm,devices_list=devicess,Test_version='2.0.1',testtime=str(hour))
        logging.warning("测试执行完毕，耗时：%s"%hour)
    else:
        logging.warning("没有可用的安卓设备")
        print("没有可用的安卓设备")