import time,datetime
from data.dicts import get_dict
from PIL import Image


def get_data_pk(driver, dict):
    main_info = driver.find_elements_by_android_uiautomator(
        'className("android.support.v7.widget.RecyclerView").className("android.widget.LinearLayout")'
    )

    data = {}
    data['time'] = datetime.datetime.now()
    for i in range(len(main_info)):
        try:
            key = main_info[i].find_element_by_id("com.eastmoney.android.berlin:id/tv_name").text
            value = main_info[i].find_element_by_id("com.eastmoney.android.berlin:id/tv_value").text
            # print("keyyyyy:",key)
        except Exception as e:
            continue
        if key in dict:
            data[dict[key]] = value

    return data


def check_data_pk(dict, data):
    miss = {}
    for key in dict.keys():
        if not dict[key] in data:
            print("not found:", dict[key])
            miss[dict[key]] = 'Not_found'
    #print('result:::::', len(dict), len(data), data)
    if len(dict) == len(data):
        return {'code': 0, 'data': data}
    else:
        return {'code': 1, 'data': data, 'miss': miss}



def extract_QuoteDetailRequest_pankou(driver, **kwargs):
    if kwargs['request_type'] == 'QuoteDetailRequest':
        dict = get_dict(kwargs['stock_type'])
    else:
        pass
    print("this is pankou extract")

    #市盈率(动) right 页面上的注解

    if kwargs['stock_type'] == 'sci_tech':  #科创股 需滑动
        data1 = get_data_pk(driver, dict)
        driver.swipe_up()
        time.sleep(1)
        data2 = get_data_pk(driver, dict)
        data = {**data1, **data2}
        # result = check_data_pk(dict, data)
    else:
        data = get_data_pk(driver, dict)
        # result = check_data_pk(dict, data)
    # return result
    print(data)
    return data

def extract_QuoteDetailRequest_five(driver, **kwargs):
    all = driver.find_element(key='id', value="com.eastmoney.android.berlin:id/chart_container")
    views = all.find_elements_by_class_name("android.view.View")[1]
    driver.get_screenshot_as_file('123.png')
    location = views.location
    size = views.size
    box = (location["x"], location["y"], location["x"] + size["width"], location["y"] + size["height"])

    # 截取图片
    image = Image.open('123.png')
    newImage = image.crop(box)
    newImage.save('123.png')

    return {'five': 1}


def extract_QuoteDetailRequest_all(driver, **kwargs):
    result = []
    for i in range(kwargs['repeat']):
        result_five = extract_QuoteDetailRequest_five(driver, **kwargs)
        driver.press(648.0, 263.0)
        time.sleep(1)
        result_pk = extract_QuoteDetailRequest_pankou(driver, **kwargs)
        driver.keyevent(4) #back
        time.sleep(1)
        driver.swipe_down()
        time.sleep(1)
        result.append({**result_five, **result_pk})

    return result




def extract_TickRequest(driver, **kwargs):
        if kwargs['stock_type'] == 'option_future':
            dict =get_dict('TickRequest_option_future')
        else:
            dict = get_dict('TickRequest')

        # listview = driver.find_element_by_id('com.eastmoney.android.berlin:id/list')
        listview = driver.find_element(key='id', value='com.eastmoney.android.berlin:id/list')
        bounds = listview.location
        sub_list = listview.find_elements_by_class_name('android.widget.LinearLayout')
        # sub_list = listview.find_element(key='class', value='android.widget.LinearLayout')

        tickresult = {}
        old_res = {}

        while(True):
            sub_list = listview.find_elements_by_class_name('android.widget.LinearLayout')
            # sub_list = listview.find_element(key='class', value='android.widget.LinearLayout')
            new_res = {}
            for ll in sub_list:
                if ll.location['x'] != bounds['x']:
                    continue

                try:
                    if kwargs['stock_type'] == 'option_future':
                        tme = ll.find_element_by_id('com.eastmoney.android.berlin:id/time').text

                        price = ll.find_element_by_id('com.eastmoney.android.berlin:id/price').text

                        volume = ll.find_element_by_id('com.eastmoney.android.berlin:id/volume').text
                        diff = ll.find_element_by_id('com.eastmoney.android.berlin:id/warehousebad').text
                        type = ll.find_element_by_id('com.eastmoney.android.berlin:id/property').text

                    else:
                        tme = ll.find_element_by_id('com.eastmoney.android.berlin:id/time').text
                        # tme = ll.find_element(key='id', value='com.eastmoney.android.berlin:id/time').text

                        price = ll.find_element_by_id('com.eastmoney.android.berlin:id/price').text
                        # price = ll.find_element(key='id', value='com.eastmoney.android.berlin:id/price').text

                        volume = ll.find_element_by_id('com.eastmoney.android.berlin:id/volume').text
                        # volume = ll.find_element(key='id', value='com.eastmoney.android.berlin:id/volume').text

                except Exception as e:
                    print("TickRequest爬取失败(漏爬)：",e)
                    continue

                #new_res[tme] = [tme, price, volume]
                if kwargs['stock_type'] == 'option_future':
                    new_res[tme] = {
                        'getTransactionTime': tme,
                        'getTransactionPrice': price,
                        'getSingleVolume': volume,
                        'getOpenInterestDiff': diff,
                        'getType': type
                    }
                else:
                    new_res[tme] = {
                        'getTransactionTime': tme,
                        'getTransactionPrice': price,
                        'getSingleVolume': volume
                    }

              #  tickresult[tme] = [tme, price, volume]
                #print("hhhhh:",tme, price, volume)
            #driver.swipe(360, 960, 360, 320)
            if old_res == new_res:
                break
            tickresult = {**tickresult, **new_res}
            old_res = new_res
            driver.swipe_up()
            time.sleep(1)

        return tickresult

