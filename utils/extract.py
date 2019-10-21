import time
from data.dicts import dict_hh

def swipe_up(driver):
    size = driver.get_window_size()
    width = size['width']
    height = size['height']
    driver.swipe(width / 2, height / 2, x=width / 2, y=height / 4)


def get_data_pk(driver, dict):
    main_info = driver.find_elements_by_android_uiautomator(
        'className("android.support.v7.widget.RecyclerView").className("android.widget.LinearLayout")'
    )

    data = {}
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
    print('result:::::', len(dict), len(data), data)
    if len(dict) == len(data):
        return {'code': 0, 'data': data}
    else:
        return {'code': 1, 'data': data, 'miss': miss}


#TODO 将词典放入data/dicts.py  重写
def extract_sh_sz(driver):
    print("this is sh_sz extract")
    dict_sh_sz = {
        '最新': 'lastPrice',
        '均价': 'averageValue',
        '涨幅': 'changeRate',
        '涨跌': 'change',
        '总手': 'volume',
        '金额': 'amount',
        '换手': 'turnoverRate',
        '量比': 'volumeRatio',
        '最高': 'highPrice',
        '最低': 'lowPrice',
        '今开': 'openPrice',
        '昨收': 'preClosePrice',
        '涨停': 'limitUp',
        '跌停': 'limitDown',
        '外盘': 'buyVolume',
        '内盘': 'sellVolume',
        '委比': 'orderRatio',
        '振幅': 'amplitudeRate',
        '市盈率(动) right': 'pe',
        '市盈率(静) right': 'pe2',
        '每股净资产': 'netAsset',
        '市净率': 'pb',
        '总股本': 'capitalization',
        '总值': 'totalValue',
        '流通股': 'circulatingShares',
        '流值': 'flowValue'
    }
    #市盈率(动) right 页面上的注解

    data = get_data_pk(driver, dict_sh_sz)
    result = check_data_pk(dict_sh_sz, data)
    # tickRequest = driver.find_elements_by_android_uiautomator(
    #     'className("android.support.v7.widget.RecyclerView").className("android.widget.LinearLayout")'
    # )

    return result


def extract_sci_tech(driver):
    print("this is tech extract")
    dict_sci_tech = {
        '最新': 'lastPrice',
        '均价': 'averageValue',
        '涨幅': 'changeRate',
        '涨跌': 'change',
        '总手': 'volume',
        '金额': 'amount',
        '换手': 'turnoverRate',
        '量比': 'volumeRatio',
        '最高': 'highPrice',
        '最低': 'lowPrice',
        '今开': 'openPrice',
        '昨收': 'preClosePrice',
        '涨停': 'limitUp',
        '跌停': 'limitDown',
        '外盘': 'buyVolume',
        '内盘': 'sellVolume',
        '委比': 'orderRatio',
        '振幅': 'amplitudeRate',
        '盘后量': 'afterHoursVolume',
        '盘后额': 'afterHoursAmount',
        '盘后成交笔数': 'afterHoursTransactionNumber',
        '盘后撤单数量': 'afterHoursWithdrawBuyCount',
        '盘后撤单笔数': 'afterHoursWithdrawBuyVolume',
        '市盈率(动) right': 'pe',
        '市盈率(静) right': 'pe2',
        '每股净资产': 'netAsset',
        '市净率': 'pb',
        '是否同股同权': 'vote',
        '总股本': 'capitalization',
        '总值': 'totalValue',
        '流通股': 'circulatingShares',
        '流值': 'flowValue',
        '发行股本': 'issuedCapital',
        '是否盈利': 'upf'
    } #市盈率有所改动 #TODO L2账号盘后成交笔数查看

    data1 = get_data_pk(driver, dict_sci_tech)

    driver.swipe_up()#360, 640, 360, 320
    time.sleep(3)

    data2 = get_data_pk(driver, dict_sci_tech)
    data = dict(data1, **data2)

    result = check_data_pk(dict_sci_tech, data)
    return result

def extract_hk(driver):
    print("this is hk extract")
    dict_hk ={
        '最新': 'lastPrice',
        '均价': 'averageValue',
        '涨幅': 'changeRate',
        '涨跌': 'change',
        '总手': 'volume',
        '金额': 'amount',
        '换手': 'turnoverRate',
        '今开': 'openPrice',
        '昨收': 'preClosePrice',
        '最高': 'highPrice',
        '最低': 'lowPrice',
        '外盘': 'buyVolume',
        '内盘': 'sellVolume',
        '市盈率(TTM)': 'pe',
        '每股净资产': 'netAsset',
        '市净率': 'pb',
        '总股本': 'capitalization',
        '总值': 'totalValue',
        '港股本': 'hs',
        '港值': 'HKTotalValue'
    }

    data = get_data_pk(driver, dict_hk)
    result = check_data_pk(dict_hk, data)
    return result

def extract_fund(driver):
    dict_fund ={
        '最新': 'lastPrice',
        '涨跌': 'change',
        '涨幅': 'changeRate',
        '换手': 'turnoverRate',
        '涨停': 'limitUp',
        '跌停': 'limitDown',
        '今开': 'openPrice',
        '昨收': 'preClosePrice',
        '最高': 'highPrice',
        '最低': 'lowPrice',
        '量比': 'volumeRatio',
        '总手': 'volume',
        '金额': 'amount',
        '实时净值': 'IOPV'
    }

    data = get_data_pk(driver, dict_fund)
    result = check_data_pk(dict_fund, data)
    return result
