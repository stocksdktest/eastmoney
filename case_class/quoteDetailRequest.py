import time, os, ddt
from appium import webdriver
from utils.ParametrizedTestCase import ParametrizedTestCase
#from utils.desired_capabilities import get_desired_capabilities
from utils.desired_capabilities import connect_device
from function.quoteDetailRequest import QuoteDetailRequest_func
# from utils.xlsx_utils import get_test_xlsx
import pymongo

# path=os.getcwd()
# testcasedata=path+'/data/testcase_data.xlsx'
# data_test=get_test_xlsx(testcasedata,index=1)


myclient = pymongo.MongoClient("mongodb://localhost:27017/")
# myclient = pymongo.MongoClient("mongodb://localhost:8082/")
# myclient = pymongo.MongoClient("mongodb://114.212.189.141:31498")  # 远程MongoDB服务器
mydb = myclient["stockSdkTest_eastmoney_1202"]



@ddt.ddt
class QuoteDetailRequest(ParametrizedTestCase):
    def __init__(self, param, methodName = 'runTest'):
        super(QuoteDetailRequest, self).__init__(methodName)
        self.port = param['port']
        self.param = param

    def setUp(self):
        #self.dis_app = get_desired_capabilities(param=self.param)
        #self.driver = webdriver.Remote('http://localhost:'+self.port+'/wd/hub',self.dis_app)
        # self.driver = webdriver.Remote('http://localhost:' + self.param['port'] + '/wd/hub', self.dis_app)
        self.driver = connect_device(self.param)
        print("QuoteDetailRequest 测试启动")

    def tearDown(self):
        print('QuoteDetailRequest测试用例执行完毕')
        time.sleep(2)
        self.driver.quit()

    #@ddt.data(data_test)
    def test_QuoteDetailRequest(self, *args, **kwargs):
        #print('What is data_test: {}'.format(data_test))

        shszfun = QuoteDetailRequest_func(driver=self.driver)
        #print("**&*&*****", type(self.param))
        #print(self.param)
        self.result = shszfun.quoteDetailRequest_extract(**(self.param))
        #TODO merge 五档买卖 from ocr （异步再开一个func 或者 同步顺序执行 修改yaml文件)
        print(self.result)
        print("into mongodb")
        name = self.param['request_type'] + self.param['stock_code']
        mydb[name].insert_many(self.result)
