import os
from utils_eastmoney.execute_case import Execute_case
# paths = os.getcwd() + '/eastmoney/data/location/quoteDetailRequest.yaml'
paths = '/Users/yuanganggang/airflow/plugins/data/location/quoteDetailRequest.yaml'



class QuoteDetailRequest_func:

    def __init__(self, driver, path=paths):
        self.driver = driver
        self.path = path
        self.exe = Execute_case(self.driver, path=self.path)

    def quoteDetailRequest_extract(self, **kwargs):
        print("******params:", kwargs)
        result = self.exe.exece_case(**kwargs)
        return result


