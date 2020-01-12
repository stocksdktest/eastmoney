import os,logging
from utils_eastmoney.execute_case import Execute_case
path = os.getcwd() + '/eastmoney/data/location/login.yaml'



class Login_func:

    def __init__(self, driver):
        self.driver = driver
        self.path = path
        self.open = Execute_case(self.driver,path=self.path)

    def log(self,**kwargs):
        result = self.open.exece_case(**kwargs)
        if result['code'] == 1:
            logging.warning('无法获取断言')
            return
        else:
            return result['data']


