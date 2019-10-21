import os,logging
from utils.execute_case import Execute_case
paths = os.getcwd() + '/data/location/sh_sz.yaml'



class Sh_sz_func:

    def __init__(self, driver,path=paths):
        self.driver = driver
        self.path = path
        self.open = Execute_case(self.driver,path=self.path)

    def sh_sz(self,**kwargs):
        result = self.open.exece_case(**kwargs)
        return result
        # if result['code'] == 1:
        #     logging.warning('获取信息不完整')
        #     return 'error'
        # else:
        #     return result['data']


