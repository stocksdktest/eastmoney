'''
appium的再封装
'''
from appium.webdriver.common.touch_action import TouchAction
class appium_driver_proxy():

    def __init__(self,driver):
        self.driver=driver

    '''
    寻找单个元素
    '''
    def  find_element(self, key, value):
        if key == 'id' :
            result = self.driver.find_element_by_id(value)
        elif key == 'xpath':
            result = self.driver.find_element_by_xpath(value)
        elif key == 'css':
            result = self.driver.find_element_by_css_selector(value)
        elif key == 'and':
            result = self.driver.find_element_by_android_uiautomator('new Uiselector().%s' % value)#这里在使用的时候比如使用text，那么这里的value为text('123')
        elif key == 'class':
            result = self.driver.find_element_by_class_name(value)
        elif key == 'name':
            result = self.driver.find_element_by_name(value)
        elif key == 'acces':
            result = self.driver.find_element_by_accessibility_id(value)
        elif key == 'text':
            result = self.driver.find_element_by_android_uiautomator(
                'text(\"%s\")' % value
            )
        elif key == 'partial':
            result = self.driver.find_element_by_partial_link_text(value)
        elif key == 'tag':
            result = self.driver.find_element_by_tag_name(value)
        elif key == 'uiautomator':
            x = value.split(',')
            str = '%s'%x[0]+'(\"%s\"'%x[1] + ')'
            result = self.driver.find_element_by_android_uiautomator(
                str
            )
        else:
            raise NameError('no element,please send tag,xpath,text,id,css,id,tag')
        return result


    '''
    寻找多个元素返回列表
    '''
    def find_elements(self, key, value):
        try:
            if key == 'id':
                results = self.driver.find_elements_by_id(value)
            elif key == 'xpath':
                results = self.driver.find_elements_by_xpath(value)
            elif key == 'css':
                results = self.driver.find_elements_by_css_selector(value)
            elif key == 'and':
                results = self.driver.find_elements_by_android_uiautomator(
                    'new Uiselector().%s' % value)  # 这里在使用的时候比如使用text，那么这里的value为text('123')
            elif key == 'class':
                results = self.driver.find_elements_by_class_name(value)
            elif key == 'name':
                results = self.driver.find_elements_by_name(value)
            elif key == 'acces':
                results = self.driver.find_elements_by_accessibility_id(value)
            elif key == 'text':
                #print("proxy :", 'text(\"%s\")' % value)
                results = self.driver.find_element_by_android_uiautomator('text(\"%s\")' % value)
                #results = self.driver.find_elements_by_link_text(value)
            elif key == 'partial':
                results = self.driver.find_elements_by_partial_link_text(value)
            elif key == 'tag':
                results = self.driver.find_elements_by_tag_name(value)
            else:
                raise NameError('no element,please send tag,xpath,text,id,css,id,tag')
            return results
        except Exception as e:
            return e

    '''
    uiautomator照旧
    '''
    def find_elements_by_android_uiautomator(self,key_word):
        #print('key_word:',key_word)
        return self.driver.find_elements_by_android_uiautomator(key_word)

    def get_size(self):
        size = self.driver.get_window_size()
        width = size['width']
        height = size['height']
        return [width/2, height/2]

    def press_center(self):
        size = self.driver.get_window_size()
        width = size['width']
        height = size['height']
        action = TouchAction(self.driver)
        action.press(x=width/2, y=height/2).release().perform()

    def press(self,x,y):
        action = TouchAction(self.driver)
        action.press(x=x, y=y).release().perform()

    def swipe_up(self):
        size = self.driver.get_window_size()
        width = size['width']
        height = size['height']
        self.driver.swipe(width / 2, height / 2, width / 2, height / 4)

    def get_screenshot_as_file(self, filename):
        self.driver.get_screenshot_as_file(filename)

    def swipe_down(self):
        size = self.driver.get_window_size()
        width = size['width']
        height = size['height']
        self.driver.swipe(width / 2, height / 4, width / 2, height / 2)

    def keyevent(self, num):
        self.driver.keyevent(num)
