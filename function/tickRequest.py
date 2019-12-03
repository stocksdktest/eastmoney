import os, logging
from utils.execute_case import Execute_case

paths = os.getcwd() + '/data/location/tickRequest.yaml'


class TickRequest_func:

    def __init__(self, driver, path=paths):
        self.driver = driver
        self.path = path
        self.exe = Execute_case(self.driver, path=self.path)

    def tickRequest_extract(self, **kwargs):
        print("******params:", kwargs)
        result = self.exe.exece_case(**kwargs)
        return result
        # if result['code'] == 1:
        #     logging.warning('获取信息不完整')
        #     return 'error'
        # else:
        #     return result['data']
