import time,os,ddt
from appium import webdriver
from utils.ParametrizedTestCase import ParametrizedTestCase
from utils.desired_capabilities import get_desired_capabilities
from function.sh_sz import Sh_sz_func
from utils.xlsx_utils import get_test_xlsx

path=os.getcwd()
testcasedata=path+'/data/testcase_data.xlsx'
data_test=get_test_xlsx(testcasedata,index=3)

@ddt.ddt
class Hk(ParametrizedTestCase):
    def __init__(self, param , methodName = 'runTest'):
        super(Hk, self).__init__(methodName)
        self.port = param['port']
        self.param = param

    def setUp(self):
        self.dis_app = get_desired_capabilities()
        #self.driver = webdriver.Remote('http://localhost:'+self.port+'/wd/hub',self.dis_app)
        self.driver = webdriver.Remote('http://localhost:' + self.param['port'] + '/wd/hub', self.dis_app)
        print("Hk测试启动")

    def tearDown(self):
        print('Hk测试用例执行完毕')
        time.sleep(5)
        self.driver.quit()

    @ddt.data(data_test)
    def test_sh_sz(self, *args, **kwargs):
        print('What is data_test: {}'.format(data_test))
        hkfun = Sh_sz_func(driver=self.driver, path=path + '/data/location/hk.yaml')
        self.result = hkfun.sh_sz(**(data_test[5]))
        #TODO merge 五档买卖 from ocr （异步再开一个func 或者 同步顺序执行 修改yaml文件)
        print(self.result)