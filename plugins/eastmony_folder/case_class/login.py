import time, ddt
from utils_eastmoney.ParametrizedTestCase import ParametrizedTestCase
from utils_eastmoney.desired_capabilities import connect_device
from function.login import Login_func


# path=os.getcwd()
# testcasedata=path+'/data/testcase_data.xlsx'
# data_test=get_test_xlsx(testcasedata,index=0)

@ddt.ddt
class Login(ParametrizedTestCase):
    def __init__(self, param, methodName = 'runTest'):
        super(Login, self).__init__(methodName)
        self.port = param['port']
        self.param = param

    def setUp(self):
        # self.dis_app = get_desired_capabilities()
        #self.driver = webdriver.Remote('http://localhost:'+self.port+'/wd/hub',self.dis_app)
        # self.driver = webdriver.Remote('http://localhost:' + self.param['port'] + '/wd/hub', self.dis_app)
        self.driver = connect_device(self.param)
        print("Login测试启动")

    def tearDown(self):
        print('Login测试用例执行完毕')
        time.sleep(2)
        self.driver.quit()

    # @ddt.data(*data_test)
    def test_login(self, *args, **kwargs):
        # print('What is data_test: {}'.format(data_test))
        logfun = Login_func(driver=self.driver)
        self.assert_content = logfun.log(**(self.param))
        # if data_test['assert_content'] == self.assert_content:
        #     print("!!!!!!PASS!!!!!!!")