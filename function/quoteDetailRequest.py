import os, logging
from utils.execute_case import Execute_case
paths = os.getcwd() + '/data/location/quoteDetailRequest.yaml'



class QuoteDetailRequest_func:

    def __init__(self, driver, path=paths):
        self.driver = driver
        self.path = path
        self.exe = Execute_case(self.driver, path=self.path)

    def quoteDetailRequest_extract(self, **kwargs):
        print("******params:", kwargs)
        result = self.exe.exece_case(**kwargs)
        return result


