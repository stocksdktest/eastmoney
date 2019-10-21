from appium import webdriver
import time
import logging
import re
from utils.yaml_utils import open_yaml
from utils.appium_proxy import appium_driver_proxy as driver_proxy
from utils.extract import extract_sh_sz, extract_sci_tech,extract_hk,extract_fund





class Execute_case():
    def __init__(self, driver, path):
        self.driver = driver
        self.path = path

    def open_file(self):
        return open_yaml(path=self.path)

    def exece_case(self,**kwargs):
        data = self.open_file()
        if data['code'] == 1:
            print('Data code is 1')
            return
        data = data['data']
        case_driver = driver_proxy(driver=self.driver)
        for i in range(len(data)-1):
            #有try的情况： 尝试寻找异常页面 有页面就点掉 或者获取断言判断 所以只能是click


            if data[i]['operate_type'] == 'sleep':
                time.sleep(data[i]['index'])
            elif data[i]['operate_type'] == 'press_center':
                case_driver.press_center()
            elif data[i]['operate_type'] == 'press':
                case_driver.press(x=data[i]['x'],y=data[i]['y'])
            elif data[i]['operate_type'] == 'extract_sh_sz' :
                case_driver


            else:
                print()
                if 'try' in data[i]:
                    try:
                        f = case_driver.find_element(key=data[i]['find_type'], value=data[i]['element_info'])
                    except Exception as e:
                        continue
                else:
                    f = case_driver.find_element(key=data[i]['find_type'], value=data[i]['element_info'])

                if data[i]['operate_type'] == 'click':
                    f.click()
                elif data[i]['operate_type'] == 'get_text':
                    f.text
                elif data[i]['operate_type'] == 'send_key':
                    key = kwargs.get(data[i]['key'])
                    f.clear()
                    if re.match('\d+\.[a-z]+', key):
                        key = re.split('\.', key)[0]
                    f.set_value(key)
                else:
                    logging.warning('请检查您的测试步骤') #log
            time.sleep(3) #TODO 确定暂停秒数

        f = case_driver.find_element(key=data[-1]['find_type'], value=data[-1]['element_info'])
        if data[-1]['operate_type'] == 'get_text':
            result = {'code': 0, 'data': f.text}
        elif data[-1]['operate_type'] == 'extract_sh_sz':
            result = extract_sh_sz(case_driver)
        elif data[-1]['operate_type'] == 'extract_sci_tech':
            result = extract_sci_tech(case_driver)
        elif data[-1]['operate_type'] == 'extract_hk':
            result = extract_hk(case_driver)
        elif data[-1]['operate_type'] == 'extract_fund':
            result = extract_fund(case_driver)
        else:
            result = {'code': 1, 'data': "请检查您的测试步骤最后一步为断言用的"}
            logging.warning('请检查您的测试步骤最后一步为断言用的') #log
        return result
        #return {'code': 1,'assertcontent': "我知道了" }