from protos_gen.config_pb2 import RunnerConfig, TestcaseConfig
import json


# 站点134
def get_case1():
    case_list = []
    market_level = "1"
    hk_perms = []
    server_sites = {}

    # AH股联动 方法一
    case_conf = TestcaseConfig()
    case_conf.testcaseID = 'AHQUOTE_1'
    case_conf.roundIntervalSec = 3
    case_conf.continueWhenFailed = False
    case_conf.paramStrs.extend([
        json.dumps({
            'CODES': '600028.sh'
        })
    ])
    case_list.append(case_conf)

    # AH股列表 方法一
    case_conf = TestcaseConfig()
    case_conf.testcaseID = 'AHLIST_1'
    case_conf.roundIntervalSec = 3
    case_conf.continueWhenFailed = False
    case_conf.paramStrs.extend([
        json.dumps({
            'param': '0,12,2,1'
        })
    ])
    case_list.append(case_conf)

    # AH股列表 方法二
    case_conf = TestcaseConfig()
    case_conf.testcaseID = 'AHLIST_2'
    case_conf.roundIntervalSec = 3
    case_conf.continueWhenFailed = False
    case_conf.paramStrs.extend([
        json.dumps({
            'param': '0,12,2,1'
        })
    ])
    case_list.append(case_conf)

    # CDR,GDR联动 方法一
    case_conf = TestcaseConfig()
    case_conf.testcaseID = 'DRLINKQUOTE_1'
    case_conf.continueWhenFailed = False
    case_conf.roundIntervalSec = 3
    case_conf.paramStrs.extend([
        json.dumps({
            'code': 'HTSC.uk'
        })
    ])
    case_list.append(case_conf)

    # CDR,GDR列表 方法一
    case_conf = TestcaseConfig()
    case_conf.testcaseID = 'DRQUOTELIST_1'
    case_conf.continueWhenFailed = False
    case_conf.roundIntervalSec = 3
    case_conf.paramStrs.extend([
        json.dumps({
            'code': 'gdr',
            'param': '0,10,3,1'
        })
    ])
    case_list.append(case_conf)

    # K线复权信息 方法一
    case_conf = TestcaseConfig()
    case_conf.testcaseID = 'OHLCSUB_1'
    case_conf.continueWhenFailed = False
    case_conf.roundIntervalSec = 3
    case_conf.paramStrs.extend([
        json.dumps({
            'code': '600000.sh'
        })
    ])
    case_list.append(case_conf)

    # K线数据 方法一对应文档方法三   不用于对比，需测试接口是否通
    case_conf = TestcaseConfig()
    case_conf.testcaseID = 'OHLCTEST_1'
    case_conf.roundIntervalSec = 3
    case_conf.continueWhenFailed = False
    case_conf.paramStrs.extend([
        json.dumps({
            'stk': '06886.hk',
            'type': 'dayk'
        })
    ])
    case_list.append(case_conf)

    # K线数据 方法二对应文档方法四
    case_conf = TestcaseConfig()
    case_conf.testcaseID = 'OHLCTEST_2'
    case_conf.roundIntervalSec = 3
    case_conf.continueWhenFailed = False
    case_conf.paramStrs.extend([
        json.dumps({
            'stk': '06886.hk',
            'type': 'dayk',
            'sub': '1'
        })
    ])
    case_list.append(case_conf)

    # uk市场快照单独接口 方法一
    case_conf = TestcaseConfig()
    case_conf.testcaseID = 'UKQUOTE_1'
    case_conf.continueWhenFailed = False
    case_conf.roundIntervalSec = 3
    case_conf.paramStrs.extend([
        json.dumps({
            'code': 'HTSC.uk'
        })
    ])
    case_list.append(case_conf)

    # 板块排序 方法一
    case_conf = TestcaseConfig()
    case_conf.testcaseID = 'BANKUAISORTING_1'
    case_conf.roundIntervalSec = 3
    case_conf.continueWhenFailed = False
    case_conf.paramStrs.extend([
        json.dumps({
            'symbol': 'Notion',
            'param1': '0,12,hsl,0'
        })
    ])
    case_list.append(case_conf)

    # 板块排序 方法二
    case_conf = TestcaseConfig()
    case_conf.testcaseID = 'BANKUAISORTING_2'
    case_conf.roundIntervalSec = 3
    case_conf.continueWhenFailed = False
    case_conf.paramStrs.extend([
        json.dumps({
            'symbol': 'Notion',
            'param1': '0,12,hsl,0'
        })
    ])
    case_list.append(case_conf)

    # 板块指数 方法一   不用于对比，需测试接口是否通
    case_conf = TestcaseConfig()
    case_conf.testcaseID = 'PLATEINDEXQUOTE_1'
    case_conf.continueWhenFailed = False
    case_conf.roundIntervalSec = 3
    case_conf.paramStrs.extend([
        json.dumps({
            'CODES': 'A20010.bk'
        }),
        json.dumps({
            'CODES': 'A20010.bk'
        })
    ])
    case_list.append(case_conf)

    # 板块指数 方法二
    case_conf = TestcaseConfig()
    case_conf.testcaseID = 'PLATEINDEXQUOTE_2'
    case_conf.continueWhenFailed = False
    case_conf.roundIntervalSec = 3
    case_conf.paramStrs.extend([
        json.dumps({
            'CODES': 'A20010.bk',
            'COSTOMFILEDS': 'null'
        })
    ])
    case_list.append(case_conf)

    # 次新股 方法一
    case_conf = TestcaseConfig()
    case_conf.testcaseID = 'SUBNEWSTOCKRANKING_1'
    case_conf.continueWhenFailed = False
    case_conf.roundIntervalSec = 3
    case_conf.paramStrs.extend([
        json.dumps({
            'param': '0,10,3,1'
        })
    ])
    case_list.append(case_conf)

    # 次新债 方法一
    case_conf = TestcaseConfig()
    case_conf.testcaseID = 'SUBNEWBONDSTOCKRANKING_1'
    case_conf.continueWhenFailed = False
    case_conf.roundIntervalSec = 3
    case_conf.paramStrs.extend([
        json.dumps({
            'param': '0,10,3,1'
        })
    ])
    case_list.append(case_conf)

    # 分价 方法一
    case_conf = TestcaseConfig()
    case_conf.testcaseID = 'MOREPRICE_1'
    case_conf.roundIntervalSec = 3
    case_conf.continueWhenFailed = False
    case_conf.paramStrs.extend([
        json.dumps({
            'code': '06886.hk',
            'subtype': '1001'
            # 'code': 'IC1910.cff',
            # 'subtype': 'futureIC'
        })
    ])
    case_list.append(case_conf)

    # 分价 方法二 仅用于中金所
    case_conf = TestcaseConfig()
    case_conf.testcaseID = 'MOREPRICE_2'
    case_conf.roundIntervalSec = 3
    case_conf.continueWhenFailed = False
    case_conf.paramStrs.extend([
        json.dumps({
            'code': 'IC1910.cff'
        })
    ])
    case_list.append(case_conf)

    # 分时明细 方法一
    case_conf = TestcaseConfig()
    case_conf.testcaseID = 'TICK_1'
    case_conf.continueWhenFailed = False
    case_conf.roundIntervalSec = 3
    case_conf.paramStrs.extend([
        json.dumps({
            'CODES': '600000.sh',
            'PAGES': '0,100,-1',
            'SUBTYPES': '1001'
        })
    ])
    case_list.append(case_conf)

    # 港股其他 方法一
    case_conf = TestcaseConfig()
    case_conf.testcaseID = 'HKSTOCKINFO_1'
    case_conf.continueWhenFailed = False
    case_conf.roundIntervalSec = 3
    case_conf.paramStrs.extend([
        json.dumps({
            'code': '00005.hk',
            'subtype': '1001'
        })
    ])
    case_list.append(case_conf)

    # 个股所属板块行情 方法一
    case_conf = TestcaseConfig()
    case_conf.testcaseID = 'BANKUAIQUOTE_1'
    case_conf.roundIntervalSec = 3
    case_conf.continueWhenFailed = False
    case_conf.paramStrs.extend([
        json.dumps({
            'code': '600425.sh',
            'params': 'Trade'
        }),
        json.dumps({
            'code': 'sw_600425.sh',
            'params': 'null'
        })
    ])
    case_list.append(case_conf)

    # 股票查询 方法一
    case_conf = TestcaseConfig()
    case_conf.testcaseID = 'SEARTEST_1'
    case_conf.continueWhenFailed = False
    case_conf.roundIntervalSec = 3
    case_conf.paramStrs.extend([
        json.dumps({
            'market': 'sh'
        })
    ])
    case_list.append(case_conf)

    # 股票查询 方法二
    case_conf = TestcaseConfig()
    case_conf.testcaseID = 'SEARTEST_2'
    case_conf.continueWhenFailed = False
    case_conf.roundIntervalSec = 3
    case_conf.paramStrs.extend([
        json.dumps({
            'keyword': '9800',
            'searchSize': '1'
        })
    ])
    case_list.append(case_conf)

    # 股票查询 方法三
    case_conf = TestcaseConfig()
    case_conf.testcaseID = 'SEARTEST_3'
    case_conf.continueWhenFailed = False
    case_conf.roundIntervalSec = 3
    case_conf.paramStrs.extend([
        json.dumps({
            'keyword': '60000',
            'searchCode': 'SH1001',
            'searchSize': '10'
        })
    ])
    case_list.append(case_conf)

    # 股票查询 方法四
    case_conf = TestcaseConfig()
    case_conf.testcaseID = 'SEARTEST_4'
    case_conf.continueWhenFailed = False
    case_conf.roundIntervalSec = 3
    case_conf.paramStrs.extend([
        json.dumps({
            'keyword': '100',
            'searchCode': 'Sh1001',
            'searchSize': '10',
            'querySts': '9800'
        })
    ])
    case_list.append(case_conf)

    # 股票查询 方法五
    case_conf = TestcaseConfig()
    case_conf.testcaseID = 'SEARTEST_5'
    case_conf.continueWhenFailed = False
    case_conf.roundIntervalSec = 3
    case_conf.paramStrs.extend([
        json.dumps({
            'keyword': '00',
            'searchCode': 'SH1001',
            'searchSize': '10',
            'querySts': '9800'
        })
    ])
    case_list.append(case_conf)

    # 行情快照 方法一
    case_conf = TestcaseConfig()
    case_conf.testcaseID = 'QUOTEDETAIL_1'
    case_conf.continueWhenFailed = False
    case_conf.roundIntervalSec = 3
    case_conf.paramStrs.extend([
        json.dumps({
            'CODES': '600000.sh'
        })
    ])
    case_list.append(case_conf)

    # 行情快照 方法二
    case_conf = TestcaseConfig()
    case_conf.testcaseID = 'QUOTEDETAIL_2'
    case_conf.continueWhenFailed = False
    case_conf.roundIntervalSec = 3
    case_conf.paramStrs.extend([
        json.dumps({
            'CODES': '600000.sh',
            'COUNTS': '10',
            'INTS1': 'null',
            'INTS2': 'null'
        })
    ])
    case_list.append(case_conf)

    # 行情快照  期货 方法三
    case_conf = TestcaseConfig()
    case_conf.testcaseID = 'QUOTEDETAIL_3'
    case_conf.continueWhenFailed = False
    case_conf.roundIntervalSec = 3
    case_conf.paramStrs.extend([
        json.dumps({
            'CODES': 'AP001.czce',
            'FIELDS': 'null'
        })
    ])
    case_list.append(case_conf)

    # 沪股通和深股通额度 方法一
    case_conf = TestcaseConfig()
    case_conf.testcaseID = 'HSAMOUNT_1'
    case_conf.continueWhenFailed = False
    case_conf.roundIntervalSec = 3
    case_conf.paramStrs.extend([
        json.dumps({

        })
    ])
    case_list.append(case_conf)

    # 沪深A股及指数涨跌平家数 方法一
    case_conf = TestcaseConfig()
    case_conf.testcaseID = 'UPDOWNS_1'
    case_conf.continueWhenFailed = False
    case_conf.roundIntervalSec = 3
    case_conf.paramStrs.extend([
        json.dumps({
            'code': 'SHSZ'
        })
    ])
    case_list.append(case_conf)

    # 沪深当日涨跌统计数据 方法一
    case_conf = TestcaseConfig()
    case_conf.testcaseID = 'MARKETUPDOWN_1'
    case_conf.continueWhenFailed = False
    case_conf.roundIntervalSec = 3
    case_conf.paramStrs.extend([
        json.dumps({
        })
    ])
    case_list.append(case_conf)

    # 获取港股价差对照表 方法一
    case_conf = TestcaseConfig()
    case_conf.testcaseID = 'HKPRICEINFO_1'
    case_conf.continueWhenFailed = False
    case_conf.roundIntervalSec = 3
    case_conf.paramStrs.extend([
        json.dumps({
        })
    ])
    case_list.append(case_conf)

    # 集合竞价走势接口 方法一
    case_conf = TestcaseConfig()
    case_conf.testcaseID = 'BIDCHART_1'
    case_conf.continueWhenFailed = False
    case_conf.roundIntervalSec = 3
    case_conf.paramStrs.extend([
        json.dumps({
            'code': '600000.sh'
        })
    ])
    case_list.append(case_conf)

    # 集合竞价走势接口 方法二
    case_conf = TestcaseConfig()
    case_conf.testcaseID = 'BIDCHART_2'
    case_conf.continueWhenFailed = False
    case_conf.roundIntervalSec = 3
    case_conf.paramStrs.extend([
        json.dumps({
            'quoteitem': '600000.sh'
        })
    ])
    case_list.append(case_conf)

    # 交易行情 方法一
    case_conf = TestcaseConfig()
    case_conf.testcaseID = 'TRADEQUOTE_1'
    case_conf.continueWhenFailed = False
    case_conf.roundIntervalSec = 3
    case_conf.paramStrs.extend([
        json.dumps({
            'code': '600000.sh'
        })
    ])
    case_list.append(case_conf)

    # 节假日 方法一
    case_conf = TestcaseConfig()
    case_conf.testcaseID = 'HOLIDAY_1'
    case_conf.roundIntervalSec = 3
    case_conf.continueWhenFailed = False
    case_conf.paramStrs.extend([
        json.dumps({
        })
    ])
    case_list.append(case_conf)

    # 经纪席位 方法一
    case_conf = TestcaseConfig()
    case_conf.testcaseID = 'BROKERINFO_1'
    case_conf.continueWhenFailed = False
    case_conf.roundIntervalSec = 3
    case_conf.paramStrs.extend([
        json.dumps({
            'stockID': '00001.hk'
        })
    ])
    case_list.append(case_conf)

    # 可转债溢价查询 方法一
    case_conf = TestcaseConfig()
    case_conf.testcaseID = 'CONVERTIBLE_1'
    case_conf.continueWhenFailed = False
    case_conf.roundIntervalSec = 3
    case_conf.paramStrs.extend([
        json.dumps({
            'code': '113009.sh'
        })
    ])
    case_list.append(case_conf)

    # 历史K线方法一
    case_conf = TestcaseConfig()
    case_conf.testcaseID = 'OHLCV3_1'
    case_conf.continueWhenFailed = False
    case_conf.roundIntervalSec = 3
    case_conf.paramStrs.extend([
        json.dumps({
            'CODES': '600000.sh',
            'TYPES': 'dayk'
        })
    ])
    case_list.append(case_conf)

    # 历史K线方法二
    case_conf = TestcaseConfig()
    case_conf.testcaseID = 'OHLCV3_2'
    case_conf.continueWhenFailed = False
    case_conf.roundIntervalSec = 3
    case_conf.paramStrs.extend([
        json.dumps({
            'CODES': '600000.sh',
            'TYPES': 'dayk',
            'FqTypes': '1',
            'DATES': 'null'
        })
    ])
    case_list.append(case_conf)

    # 历史K线方法三
    case_conf = TestcaseConfig()
    case_conf.testcaseID = 'OHLCV3_3'
    case_conf.continueWhenFailed = False
    case_conf.roundIntervalSec = 3
    case_conf.paramStrs.extend([
        json.dumps({
            'CODES': '600000.sh',
            'DATES': '20190828',
            'TYPES': 'dayk',
            'FqTypes': '2'
        })
    ])
    case_list.append(case_conf)

    # 历史K线方法四
    case_conf = TestcaseConfig()
    case_conf.testcaseID = 'OHLCV3_4'
    case_conf.continueWhenFailed = False
    case_conf.roundIntervalSec = 3
    case_conf.paramStrs.extend([
        json.dumps({
            'CODES': '600000.sh',
            'BeginDates': '20190812',
            'EndDates': 'null',
            'TYPES': 'dayk',
            'FqTypes': '2'
        })
    ])
    case_list.append(case_conf)

    # 历史K线方法五
    case_conf = TestcaseConfig()
    case_conf.testcaseID = 'OHLCV3_5'
    case_conf.continueWhenFailed = False
    case_conf.roundIntervalSec = 3
    case_conf.paramStrs.extend([
        json.dumps({
            'CODES': '600000.sh',
            'TYPES': 'dayk',
            'FqTypes': '2',
            'Dates': 'null',
            'Numbers': '300'
        })
    ])
    case_list.append(case_conf)

    # 历史分时 方法一  传单只股票
    case_conf = TestcaseConfig()
    case_conf.testcaseID = 'HISTORYCHART_1'
    case_conf.roundIntervalSec = 3
    case_conf.continueWhenFailed = False
    case_conf.paramStrs.extend([
        json.dumps({
            'code': '600000.sh',
            'date': '20190826'
        })
    ])
    case_list.append(case_conf)

    # 历史分时 方法二  传快照
    case_conf = TestcaseConfig()
    case_conf.testcaseID = 'HISTORYCHART_2'
    case_conf.roundIntervalSec = 3
    case_conf.continueWhenFailed = False
    case_conf.paramStrs.extend([
        json.dumps({
            'quoteitem': '600000.sh',
            'date': '20190826'
        })
    ])
    case_list.append(case_conf)

    # 两市港股通额度资讯 方法一
    case_conf = TestcaseConfig()
    case_conf.testcaseID = 'HKMARINFO_1'
    case_conf.roundIntervalSec = 3
    case_conf.continueWhenFailed = False
    case_conf.paramStrs.extend([
        json.dumps({
        })
    ])
    case_list.append(case_conf)

    # 期权—T型报价 方法一
    case_conf = TestcaseConfig()
    case_conf.testcaseID = 'OPTIONTQUOTE_1'
    case_conf.continueWhenFailed = False
    case_conf.roundIntervalSec = 3
    case_conf.paramStrs.extend([
        json.dumps({
            'stockID': '10001908.sh',
            'yearmonth': '1808'
        })
    ])
    case_list.append(case_conf)

    # 期权——标的行情 方法一
    case_conf = TestcaseConfig()
    case_conf.testcaseID = 'OPTIONLIST_1'
    case_conf.roundIntervalSec = 3
    case_conf.continueWhenFailed = False
    case_conf.paramStrs.extend([
        json.dumps({
        })
    ])
    case_list.append(case_conf)

    # 期权—商品行情 方法一
    case_conf = TestcaseConfig()
    case_conf.testcaseID = 'OPTIONQUOTE_1'
    case_conf.continueWhenFailed = False
    case_conf.roundIntervalSec = 3
    case_conf.paramStrs.extend([
        json.dumps({
            'stockID': '510050.sh',
            'page': '2'
        })
    ])
    case_list.append(case_conf)

    # 增值指标  方法一
    case_conf = TestcaseConfig()
    case_conf.testcaseID = 'ADDVALUE_1'
    case_conf.continueWhenFailed = False
    case_conf.roundIntervalSec = 3
    case_conf.paramStrs.extend([
        json.dumps({
            'code': '600000.sh',
            'subtype': '1001'
        })
    ])
    case_list.append(case_conf)

    # 增值指标 方法二
    case_conf = TestcaseConfig()
    case_conf.testcaseID = 'ADDVALUE_2'
    case_conf.continueWhenFailed = False
    case_conf.roundIntervalSec = 3
    case_conf.paramStrs.extend([
        json.dumps({
            'code': '600000.sh',
            'market': 'sh',
            'subtype': '1001'
        })
    ])
    case_list.append(case_conf)

    # 走势数据方法一
    case_conf = TestcaseConfig()
    case_conf.testcaseID = 'CHARTV2TEST_1'
    case_conf.continueWhenFailed = False
    case_conf.roundIntervalSec = 3
    case_conf.paramStrs.extend([
        json.dumps({
            'CODES': '600000.sh',
            'Chart_Types': 'ChartTypeOneDay',
            'SUBTYPES': '1001'
        })
    ])
    case_list.append(case_conf)

    # 走势数据方法二
    case_conf = TestcaseConfig()
    case_conf.testcaseID = 'CHARTV2TEST_2'
    case_conf.continueWhenFailed = False
    case_conf.roundIntervalSec = 3
    case_conf.paramStrs.extend([
        json.dumps({
            'CODES': '600000.sh',
            'Chart_Types': 'ChartTypeOneDay'
        })
    ])
    case_list.append(case_conf)

    # 走势数据方法三
    case_conf = TestcaseConfig()
    case_conf.testcaseID = 'CHARTV2TEST_3'
    case_conf.continueWhenFailed = False
    case_conf.roundIntervalSec = 3
    case_conf.paramStrs.extend([
        json.dumps({
            'CODES': '600000.sh',
            'Chart_Types': 'ChartTypeOneDay',
            'PointAddTypes': '0'
        })
    ])
    case_list.append(case_conf)

    # 走势数据方法四
    case_conf = TestcaseConfig()
    case_conf.testcaseID = 'CHARTV2TEST_4'
    case_conf.continueWhenFailed = False
    case_conf.roundIntervalSec = 3
    case_conf.paramStrs.extend([
        json.dumps({
            'CODES': '600000.sh',
            'Chart_Types': 'ChartTypeOneDay'
        })
    ])
    case_list.append(case_conf)

    # 走势数据方法五
    case_conf = TestcaseConfig()
    case_conf.testcaseID = 'CHARTV2TEST_5'
    case_conf.continueWhenFailed = False
    case_conf.roundIntervalSec = 3
    case_conf.paramStrs.extend([
        json.dumps({
            'CODES': '600000.sh',
            'Chart_Types': 'ChartTypeOneDay',
            'PointAddTypes': '1'
        })
    ])
    case_list.append(case_conf)

    # 走势数据方法六
    case_conf = TestcaseConfig()
    case_conf.testcaseID = 'CHARTV2TEST_6'
    case_conf.continueWhenFailed = False
    case_conf.roundIntervalSec = 3
    case_conf.paramStrs.extend([
        json.dumps({
            'CODES': '600000.sh',
            'Chart_Types': 'ChartTypeOneDay',
            'isNeedAfterHours': 'false'
        })
    ])
    case_list.append(case_conf)

    # 板块类股票行情 方法一
    case_conf = TestcaseConfig()
    case_conf.testcaseID = 'CATEQUOTE_1'
    case_conf.roundIntervalSec = 3
    case_conf.continueWhenFailed = False
    case_conf.paramStrs.extend([
        json.dumps({
            'CateType': 'HK1010',
            'page': '0'
        })
    ])
    case_list.append(case_conf)

    # 盘后走势（科创板） 方法一
    case_conf = TestcaseConfig()
    case_conf.testcaseID = 'AFTERHOURSCHART_1'
    case_conf.continueWhenFailed = False
    case_conf.roundIntervalSec = 3
    case_conf.paramStrs.extend([
        json.dumps({
            'code': '688028.sh'
        })
    ])
    case_list.append(case_conf)

    # 盘后走势（科创板） 方法二
    case_conf = TestcaseConfig()
    case_conf.testcaseID = 'AFTERHOURSCHART_2'
    case_conf.continueWhenFailed = False
    case_conf.roundIntervalSec = 3
    case_conf.paramStrs.extend([
        json.dumps({
            'code': '688028.sh'
        })
    ])
    case_list.append(case_conf)

    # 排序接口 方法一
    case_conf = TestcaseConfig()
    case_conf.testcaseID = 'CATESORTING_1'
    case_conf.roundIntervalSec = 3
    case_conf.continueWhenFailed = False
    case_conf.paramStrs.extend([
        json.dumps({
            'id': 'SH1001',
            'param': '0,10,7,1,1',
        })
    ])
    case_list.append(case_conf)

    # 排序接口 方法二
    case_conf = TestcaseConfig()
    case_conf.testcaseID = 'CATESORTING_2'
    case_conf.roundIntervalSec = 3
    case_conf.continueWhenFailed = False
    case_conf.paramStrs.extend([
        json.dumps({
            'id': 'SH1001',
            'param': '0,10,7,1,1',
            'quoteCustom': 'null',
            'addvalueCustom': 'null'
        })
    ])
    case_list.append(case_conf)

    # 排序接口 方法三
    case_conf = TestcaseConfig()
    case_conf.testcaseID = 'CATESORTING_3'
    case_conf.roundIntervalSec = 3
    case_conf.continueWhenFailed = False
    case_conf.paramStrs.extend([
        json.dumps({
            'id': 'SH1001',
            'param': '0,10,7,1,1',
            'quoteCustom': 'null',
            'addvalueCustom': 'null'
        })
    ])
    case_list.append(case_conf)

    # 排序接口 方法四
    case_conf = TestcaseConfig()
    case_conf.testcaseID = 'CATESORTING_4'
    case_conf.roundIntervalSec = 3
    case_conf.continueWhenFailed = False
    case_conf.paramStrs.extend([
        json.dumps({
            'id': 'dce_all',
            'param': '0,10,last,1',
            'quoteCustom': 'null'
        })
    ])
    case_list.append(case_conf)
    return case_list, market_level, hk_perms, server_sites


# F10 134
def get_case2():
    case_list = []
    market_level = "1"
    hk_perms = ["hk10", "hka1"]
    server_sites = {}
    server_sites["sh"] = "http://114.80.155.134:22016"
    server_sites["sz"] = "http://114.80.155.134:22016"
    server_sites["cf"] = "http://114.80.155.134:22016"
    server_sites["nf"] = "http://114.80.155.134:22013"
    server_sites["pb"] = "http://114.80.155.134:22016"

    # 财经资讯列表 方法一
    case_conf = TestcaseConfig()
    case_conf.testcaseID = 'F10_NEWSLIST_1'
    case_conf.continueWhenFailed = False
    case_conf.roundIntervalSec = 3
    case_conf.paramStrs.extend([
        json.dumps({
            'newsType': '0000',
            'updateType': '-1',
            'newsID': 'null',
            'src': 'g'
        })
    ])
    case_list.append(case_conf)

    # 财经资讯明細  方法一
    case_conf = TestcaseConfig()
    case_conf.testcaseID = 'F10_NEWS_1'
    case_conf.continueWhenFailed = False
    case_conf.roundIntervalSec = 3
    case_conf.paramStrs.extend([
        json.dumps({
            'newsID': '86168553164',
            'src': 'g'
        })
    ])
    case_list.append(case_conf)

    # 财经资讯图片  方法一 iOS无此接口
    case_conf = TestcaseConfig()
    case_conf.testcaseID = 'F10_FININFOIMAGE_1'
    case_conf.continueWhenFailed = False
    case_conf.roundIntervalSec = 3
    case_conf.paramStrs.extend([
        json.dumps({
            'FininfoimageID': '86148253782',
            'src': 'g'
        }),
        json.dumps({
            'FininfoimageID': '86148253782',
            'src': 'd'
        })
    ])
    case_list.append(case_conf)

    # 财务报表  方法一
    case_conf = TestcaseConfig()
    case_conf.testcaseID = 'F10_MAINFINADATANASS_1'
    case_conf.continueWhenFailed = False
    case_conf.roundIntervalSec = 3
    case_conf.paramStrs.extend([
        json.dumps({
            'stockId': '600000.sh',
            'dataSourceType': 'g'
        })
    ])
    case_list.append(case_conf)

    # 财务报表  方法二 仅用于港股
    case_conf = TestcaseConfig()
    case_conf.testcaseID = 'F10_MAINFINADATANASS_2'
    case_conf.continueWhenFailed = False
    case_conf.roundIntervalSec = 3
    case_conf.paramStrs.extend([
        json.dumps({
            'stockId': '00001.hk',
            'dataSourceType': 'd',
            'cueryContent': 'null'
        })
    ])
    case_list.append(case_conf)

    # 财务指标  方法一
    case_conf = TestcaseConfig()
    case_conf.testcaseID = 'F10_MAINFINAINDEXNAS_1'
    case_conf.continueWhenFailed = False
    case_conf.roundIntervalSec = 3
    case_conf.paramStrs.extend([
        json.dumps({
            'stockId': '600000.sh',
            'dataSourceType': 'g'
        })
    ])
    case_list.append(case_conf)

    # 财务指标  方法二 仅用于港股
    case_conf = TestcaseConfig()
    case_conf.testcaseID = 'F10_MAINFINAINDEXNAS_2'
    case_conf.continueWhenFailed = False
    case_conf.roundIntervalSec = 3
    case_conf.paramStrs.extend([
        json.dumps({
            'stockId': '00001.hk',
            'dataSourceType': 'd',
            'cueryContent': 'null'
        })
    ])
    case_list.append(case_conf)

    # 大事提醒  方法一
    case_conf = TestcaseConfig()
    case_conf.testcaseID = 'F10_IMPORTANTNOTICE_1'
    case_conf.continueWhenFailed = False
    case_conf.roundIntervalSec = 3
    case_conf.paramStrs.extend([
        json.dumps({
            'code': '600000.sh',
            'src': 'g'
        })
    ])
    case_list.append(case_conf)

    # 大宗交易 方法一 iOS无
    case_conf = TestcaseConfig()
    case_conf.testcaseID = 'F10_BLOCKTRADE_1'
    case_conf.continueWhenFailed = False
    case_conf.roundIntervalSec = 3
    case_conf.paramStrs.extend([
        json.dumps({
            'send': '600000.sh',
            'src': 'd'
        })
    ])
    case_list.append(case_conf)

    # 分红配送  方法一
    case_conf = TestcaseConfig()
    case_conf.testcaseID = 'F10_BONUSFINANCE_1'
    case_conf.continueWhenFailed = False
    case_conf.roundIntervalSec = 3
    case_conf.paramStrs.extend([
        json.dumps({
            'code': '600000.sh',
            'src': 'g'
        })
    ])
    case_list.append(case_conf)

    # 份额结构 方法一
    case_conf = TestcaseConfig()
    case_conf.testcaseID = 'F10_SHARESTRUCTURE_1'
    case_conf.continueWhenFailed = False
    case_conf.roundIntervalSec = 3
    case_conf.paramStrs.extend([
        json.dumps({
            'stockId': '518880.sh',
            'src': 'd'
        })
    ])
    case_list.append(case_conf)

    # 付息情况 方法一
    case_conf = TestcaseConfig()
    case_conf.testcaseID = 'F10_BNDINTERESTPAY_1'
    case_conf.continueWhenFailed = False
    case_conf.roundIntervalSec = 3
    case_conf.paramStrs.extend([
        json.dumps({
            'stockId': '019535.sh',
            'src': 'd'
        })
    ])
    case_list.append(case_conf)

    # 个股公告内文  方法一
    case_conf = TestcaseConfig()
    case_conf.testcaseID = 'F10_STOCKBULLETIN_1'
    case_conf.continueWhenFailed = False
    case_conf.roundIntervalSec = 3
    case_conf.paramStrs.extend([
        json.dumps({
            'bulletinID': '00175.hk_1414344',
            'src': 'd'
        })
    ])
    case_list.append(case_conf)

    # 个股新闻内文  方法一
    case_conf = TestcaseConfig()
    case_conf.testcaseID = 'F10_STOCKNEWS_1'
    case_conf.continueWhenFailed = False
    case_conf.roundIntervalSec = 3
    case_conf.paramStrs.extend([
        json.dumps({
            'stockNewsID': '00651.hk_20190830020009252990',
            'src': 'd'
        })
    ])
    case_list.append(case_conf)

    # 个股研报内文  方法一
    case_conf = TestcaseConfig()
    case_conf.testcaseID = 'F10_STOCKREPORT_1'
    case_conf.continueWhenFailed = False
    case_conf.roundIntervalSec = 3
    case_conf.paramStrs.extend([
        json.dumps({
            'code': '600000.sh_85830396633',
            'src': 'g'
        })
    ])
    case_list.append(case_conf)

    # 个股/自选公告  方法一
    case_conf = TestcaseConfig()
    case_conf.testcaseID = 'F10_STOCKBULLETINLIST_1'
    case_conf.continueWhenFailed = False
    case_conf.roundIntervalSec = 3
    case_conf.paramStrs.extend([
        json.dumps({
            'stockId': '600000.sh',
            'updateType': '-1',
            'newsID': 'null',
            'src': 'd'
        })
    ])
    case_list.append(case_conf)

    # 个股/自选公告  方法二
    case_conf = TestcaseConfig()
    case_conf.testcaseID = 'F10_STOCKBULLETINLIST_2'
    case_conf.continueWhenFailed = False
    case_conf.roundIntervalSec = 3
    case_conf.paramStrs.extend([
        json.dumps({
            'stockId': '600000.sh',
            'updateType': '-1',
            'newsID': 'null',
            'src': 'd',
            'count': '10'
        })
    ])
    case_list.append(case_conf)

    # 个股/自选新闻  方法一
    case_conf = TestcaseConfig()
    case_conf.testcaseID = 'F10_STOCKNEWSLIST_1'
    case_conf.continueWhenFailed = False
    case_conf.roundIntervalSec = 3
    case_conf.paramStrs.extend([json.dumps({
        'stockId': '600000.sh',
        'updateType': '-1',
        'newsID': 'null',
        'src': 'd'
    })
    ])
    case_list.append(case_conf)

    # 个股/自选新闻  方法二
    case_conf = TestcaseConfig()
    case_conf.testcaseID = 'F10_STOCKNEWSLIST_2'
    case_conf.continueWhenFailed = False
    case_conf.roundIntervalSec = 3
    case_conf.paramStrs.extend([
        json.dumps({
            'stockId': '600000.sh',
            'updateType': '-1',
            'newsID': 'null',
            'src': 'd',
            'count': '10'
        })
    ])
    case_list.append(case_conf)

    # 个股/自选研报 方法一
    case_conf = TestcaseConfig()
    case_conf.testcaseID = 'F10_STOCKREPORTLIST_1'
    case_conf.continueWhenFailed = False
    case_conf.roundIntervalSec = 3
    case_conf.paramStrs.extend([
        json.dumps({
            'code': '603903.sh',
            'updateType': '-1',
            'newsID': 'null',
            'src': 'd'
        })
    ])
    case_list.append(case_conf)

    # 个股/自选研报 方法二
    case_conf = TestcaseConfig()
    case_conf.testcaseID = 'F10_STOCKREPORTLIST_2'
    case_conf.continueWhenFailed = False
    case_conf.roundIntervalSec = 3
    case_conf.paramStrs.extend([
        json.dumps({
            'code': '600000.sh',
            'updateType': '-1',
            'newsID': 'null',
            'src': 'd',
            'count': '10'
        })
    ])
    case_list.append(case_conf)

    # 股本变动  方法一
    case_conf = TestcaseConfig()
    case_conf.testcaseID = 'F10_STOCKSHARECHANGEINFO_1'
    case_conf.continueWhenFailed = False
    case_conf.roundIntervalSec = 3
    case_conf.paramStrs.extend([
        json.dumps({
            'code': '600000.sh',
            'src': 'g'
        })
    ])
    case_list.append(case_conf)

    # 股本结构  方法一
    case_conf = TestcaseConfig()
    case_conf.testcaseID = 'F10_STOCKSHAREINFO_1'
    case_conf.continueWhenFailed = False
    case_conf.roundIntervalSec = 3
    case_conf.paramStrs.extend([
        json.dumps({
            'code': '600000.sh',
            'src': 'g'
        })
    ])
    case_list.append(case_conf)

    # 股东变动  方法一
    case_conf = TestcaseConfig()
    case_conf.testcaseID = 'F10_SHAREHOLDERHISTORYINFO_1'
    case_conf.continueWhenFailed = False
    case_conf.roundIntervalSec = 3
    case_conf.paramStrs.extend([
        json.dumps({
            'code': '600000.sh',
            'src': 'g'
        })
    ])
    case_list.append(case_conf)

    # 股票组合 方法一
    case_conf = TestcaseConfig()
    case_conf.testcaseID = 'F10_STOCKPORTFOLIO_1'
    case_conf.continueWhenFailed = False
    case_conf.roundIntervalSec = 3
    case_conf.paramStrs.extend([
        json.dumps({
            'stockId': '518880.sh',
            'src': 'd'
        })
    ])
    case_list.append(case_conf)

    # 管理层  方法一
    case_conf = TestcaseConfig()
    case_conf.testcaseID = 'F10_LEADERPERSONINFO_1'
    case_conf.continueWhenFailed = False
    case_conf.roundIntervalSec = 3
    case_conf.paramStrs.extend([
        json.dumps({
            'code': '600000.sh',
            'src': 'g'
        })
    ])
    case_list.append(case_conf)

    # 行业组合 方法一
    case_conf = TestcaseConfig()
    case_conf.testcaseID = 'F10_INDUSTRYPORTFOLIO_1'
    case_conf.continueWhenFailed = False
    case_conf.roundIntervalSec = 3
    case_conf.paramStrs.extend([
        json.dumps({
            'stockId': '518880.sh',
            'src': 'd'
        })
    ])
    case_list.append(case_conf)

    # 机构评等  方法一
    case_conf = TestcaseConfig()
    case_conf.testcaseID = 'F10_FORECASTRATING_1'
    case_conf.continueWhenFailed = False
    case_conf.roundIntervalSec = 3
    case_conf.paramStrs.extend([
        json.dumps({
            'code': '600000.sh',
            'src': 'g'
        })
    ])
    case_list.append(case_conf)

    # 机构预测  方法一
    case_conf = TestcaseConfig()
    case_conf.testcaseID = 'F10_FORECASTYEAR_1'
    case_conf.continueWhenFailed = False
    case_conf.roundIntervalSec = 3
    case_conf.paramStrs.extend([
        json.dumps({
            'code': '600000.sh',
            'src': 'g'
        })
    ])
    case_list.append(case_conf)

    # 基本情况  方法一
    case_conf = TestcaseConfig()
    case_conf.testcaseID = 'F10_COMPANYINFO_1'
    case_conf.continueWhenFailed = False
    case_conf.roundIntervalSec = 3
    case_conf.paramStrs.extend([
        json.dumps({
            'code': '600000.sh',
            'src': 'g'
        })
    ])
    case_list.append(case_conf)

    # 基金财务 方法一
    case_conf = TestcaseConfig()
    case_conf.testcaseID = 'F10_FNDFINANCE_1'
    case_conf.continueWhenFailed = False
    case_conf.roundIntervalSec = 3
    case_conf.paramStrs.extend([
        json.dumps({
            'stockId': '518880.sh',
            'src': 'd'
        })
    ])
    case_list.append(case_conf)

    # 基金分红 方法一
    case_conf = TestcaseConfig()
    case_conf.testcaseID = 'F10_FNDDIVIDEEND_1'
    case_conf.continueWhenFailed = False
    case_conf.roundIntervalSec = 3
    case_conf.paramStrs.extend([
        json.dumps({
            'stockId': '518880.sh',
            'src': 'd'
        })
    ])
    case_list.append(case_conf)

    # 基金概况 方法一
    case_conf = TestcaseConfig()
    case_conf.testcaseID = 'F10_FUNDBASIC_1'
    case_conf.continueWhenFailed = False
    case_conf.roundIntervalSec = 3
    case_conf.paramStrs.extend([
        json.dumps({
            'stockId': '512330.sh',
            'src': 'd'
        })
    ])
    case_list.append(case_conf)

    # 基金净值(12月) 方法一
    case_conf = TestcaseConfig()
    case_conf.testcaseID = 'F10_FNDNAVINDEX_1'
    case_conf.continueWhenFailed = False
    case_conf.roundIntervalSec = 3
    case_conf.paramStrs.extend([
        json.dumps({
            'stockId': '502041.sh',
            'type': '12',
            'src': 'd'
        })
    ])
    case_list.append(case_conf)

    # 基金净值（五日） 方法一
    case_conf = TestcaseConfig()
    case_conf.testcaseID = 'F10_FUNDVALUE_1'
    case_conf.continueWhenFailed = False
    case_conf.roundIntervalSec = 3
    case_conf.paramStrs.extend([
        json.dumps({
            'stockId': '502041.sh',
            'src': 'd'
        })
    ])
    case_list.append(case_conf)

    # 新股日历 方法一
    case_conf = TestcaseConfig()
    case_conf.testcaseID = 'F10_CALENDAR_1'
    case_conf.continueWhenFailed = False
    case_conf.roundIntervalSec = 3
    case_conf.paramStrs.extend([
        json.dumps({
            'src': 'd'
        })
    ])
    case_list.append(case_conf)

    # 新债日历   方法一
    case_conf = TestcaseConfig()
    case_conf.testcaseID = 'F10_BONDTRADINGDAY_1'
    case_conf.continueWhenFailed = True
    case_conf.roundIntervalSec = 3
    case_conf.paramStrs.extend([
        json.dumps({
            'src': 'd'
        })
    ])
    case_list.append(case_conf)

    # 新股详情 方法一
    case_conf = TestcaseConfig()
    case_conf.testcaseID = 'F10_NEWSHAREDETAIL_1'
    case_conf.continueWhenFailed = False
    case_conf.roundIntervalSec = 3
    case_conf.paramStrs.extend([
        json.dumps({
            'code': '002961.sz',
            'src': 'd'
        })
    ])
    case_list.append(case_conf)

    # 新债详情 方法一
    case_conf = TestcaseConfig()
    case_conf.testcaseID = 'F10_BNDSHAREIPODETAI_1'
    case_conf.continueWhenFailed = False
    case_conf.roundIntervalSec = 3
    case_conf.paramStrs.extend([
        json.dumps({
            'code': '113543.sh',
            'src': 'd'
        })
    ])
    case_list.append(case_conf)

    # 债券概况 方法一
    case_conf = TestcaseConfig()
    case_conf.testcaseID = 'F10_BONDBASIC_1'
    case_conf.continueWhenFailed = False
    case_conf.roundIntervalSec = 3
    case_conf.paramStrs.extend([
        json.dumps({
            'stockId': '019535.sh',
            'src': 'd'
        })
    ])
    case_list.append(case_conf)

    # 债券回购 方法一
    case_conf = TestcaseConfig()
    case_conf.testcaseID = 'F10_BNDBUYBACKS_1'
    case_conf.continueWhenFailed = True
    case_conf.roundIntervalSec = 3
    case_conf.paramStrs.extend([
        json.dumps({
            'stockId': '019535.sh',
            'src': 'd'
        })
    ])
    case_list.append(case_conf)

    # 主要业务  方法一
    case_conf = TestcaseConfig()
    case_conf.testcaseID = 'F10_COREBUSINESS_1'
    case_conf.continueWhenFailed = False
    case_conf.roundIntervalSec = 3
    case_conf.paramStrs.extend([
        json.dumps({
            'code': '000001.sz',
            'src': 'g'
        })
    ])
    case_list.append(case_conf)

    # 资产配置 方法一
    case_conf = TestcaseConfig()
    case_conf.testcaseID = 'F10_ASSETALLOCATION_1'
    case_conf.continueWhenFailed = False
    case_conf.roundIntervalSec = 3
    case_conf.paramStrs.extend([
        json.dumps({
            'stockId': '518880.sh',
            'src': 'd'
        })
    ])
    case_list.append(case_conf)

    # 最新基金持股  方法一
    case_conf = TestcaseConfig()
    case_conf.testcaseID = 'F10_FUNDSHAREHOLDERINFO_1'
    case_conf.continueWhenFailed = False
    case_conf.roundIntervalSec = 3
    case_conf.paramStrs.extend([
        json.dumps({
            'code': '600000.sh',
            'src': 'g'
        })
    ])
    case_list.append(case_conf)

    # 最新十大股东  方法一
    case_conf = TestcaseConfig()
    case_conf.testcaseID = 'F10_TOPSHAREHOLDER_1'
    case_conf.continueWhenFailed = False
    case_conf.roundIntervalSec = 3
    case_conf.paramStrs.extend([
        json.dumps({
            'code': '600000.sh',
            'src': 'g'
        })
    ])
    case_list.append(case_conf)

    # 最新十大流通股股东  方法一
    case_conf = TestcaseConfig()
    case_conf.testcaseID = 'F10_TOPLIQUIDSHAREHOLDER_1'
    case_conf.continueWhenFailed = False
    case_conf.roundIntervalSec = 3
    case_conf.paramStrs.extend([
        json.dumps({
            'code': '600000.sh',
            'src': 'g'
        })
    ])
    case_list.append(case_conf)

    # 最新指标  方法一
    case_conf = TestcaseConfig()
    case_conf.testcaseID = 'F10_NEWINDEX_1'
    case_conf.continueWhenFailed = False
    case_conf.roundIntervalSec = 3
    case_conf.paramStrs.extend([
        json.dumps({
            'code': '600000.sh',
            'src': 'g'
        })
    ])
    case_list.append(case_conf)

    # 当日新债 方法一
    case_conf = TestcaseConfig()
    case_conf.testcaseID = 'F10_BNDNEWSHARESCAL_1'
    case_conf.continueWhenFailed = False
    case_conf.roundIntervalSec = 3
    case_conf.paramStrs.extend([
        json.dumps({
            'date': '2019-08-22',
            'src': 'g'
        })
    ])
    case_list.append(case_conf)

    # 融资融券  方法一iOS无
    case_conf = TestcaseConfig()
    case_conf.testcaseID = 'F10_TRADEDETAIL_1'
    case_conf.continueWhenFailed = False
    case_conf.roundIntervalSec = 3
    case_conf.paramStrs.extend([
        json.dumps({
            'code': '600000.sh',
            'src': 'g'
        })
    ])
    case_list.append(case_conf)

    return case_list, market_level, hk_perms, server_sites


# L1_pb站点58
def get_case3():
    case_list = []
    market_level = "1"
    hk_perms = ["hk10", "hka1"]
    server_sites = {}
    server_sites["sh"] = "http://114.80.155.134:22016"
    server_sites["sz"] = "http://114.80.155.134:22016"
    server_sites["cf"] = "http://114.80.155.134:22016"
    server_sites["nf"] = "http://114.80.155.134:22013"
    server_sites["pb"] = "http://114.80.155.134:22016"

    # 要约收购接口请求  方法一 pb站点58
    case_conf = TestcaseConfig()
    case_conf.testcaseID = 'OFFERQUOTE_1'
    case_conf.continueWhenFailed = False
    case_conf.roundIntervalSec = 3
    case_conf.paramStrs.extend([
        json.dumps({
            'code': '000048.sz'
        })
    ])
    case_list.append(case_conf)

    # 要约收购接口请求  方法二 pb站点58
    case_conf = TestcaseConfig()
    case_conf.testcaseID = 'OFFERQUOTE_2'
    case_conf.continueWhenFailed = False
    case_conf.roundIntervalSec = 3
    case_conf.paramStrs.extend([
        json.dumps({
            'pageNum': '0',
            'pageSize': '20',
            'sortField': '4',
            'sortType': '1'
        })
    ])
    case_list.append(case_conf)

    # 涨跌分布请求接口  方法一 pb站点58
    case_conf = TestcaseConfig()
    case_conf.testcaseID = 'COMPOUNDUPDOWN_1'
    case_conf.continueWhenFailed = False
    case_conf.roundIntervalSec = 3
    case_conf.paramStrs.extend([
        json.dumps({
            'market': 'all',
            'time': '201909120940',
            'datetype': '1'
        })
    ])
    case_list.append(case_conf)
    return case_list, market_level, hk_perms, server_sites


# L2站点50
def get_case4():
    case_list = []
    market_level = "2"
    hk_perms = ["hk10", "hka1"]
    server_sites = {}
    # L2分笔
    case_conf = TestcaseConfig()
    case_conf.testcaseID = 'L2TICKV2_1'
    case_conf.continueWhenFailed = False
    case_conf.roundIntervalSec = 3
    case_conf.paramStrs.extend([
        json.dumps({
            'CODES': '600000.sh',
            'PAGES': '0,100,-1',
            'SUBTYPES': '1001'
        })
    ])
    case_list.append(case_conf)

    # L2逐笔
    case_conf = TestcaseConfig()
    case_conf.testcaseID = 'L2TICKDETAILV2_1'
    case_conf.continueWhenFailed = False
    case_conf.roundIntervalSec = 3
    case_conf.paramStrs.extend([
        json.dumps({
            'CODES': '603927.sh',
            'PAGES': '0,100,-1',
            'SUBTYPES': '1001'
        })
    ])
    case_list.append(case_conf)

    # 买卖队列 方法一
    case_conf = TestcaseConfig()
    case_conf.testcaseID = 'ORDERQUANTITY_1'
    case_conf.continueWhenFailed = False
    case_conf.roundIntervalSec = 3
    case_conf.paramStrs.extend([
        json.dumps({
            'symbolID': '600000.sh'
        })
    ])
    case_list.append(case_conf)

    # 买卖队列 方法二
    case_conf = TestcaseConfig()
    case_conf.testcaseID = 'ORDERQUANTITY_2'
    case_conf.continueWhenFailed = False
    case_conf.roundIntervalSec = 3
    case_conf.paramStrs.extend([
        json.dumps({
            'symbolID': '600000.sh',
            'market': 'sh',
            'subtype': '1001'
        })
    ])
    case_list.append(case_conf)
    return case_list, market_level, hk_perms, server_sites


def get_case_list():
    case1, m1, hk1, ssite1 = get_case1()
    case2, m2, hk2, ssite2 = get_case2()
    case3, m3, hk3, ssite3 = get_case3()
    case4, m4, hk4, ssite4 = get_case4()
    case_list = [case1, case2, case3, case4]
    m_list = [m1, m2, m3, m4]
    hk_list = [hk1, hk2, hk3, hk4]
    ssite_list = [ssite1, ssite2, ssite3, ssite4]
    return case_list, m_list, hk_list, ssite_list


if __name__ == '__main__':
    case1, m1, hk1, ssite1 = get_case1()
    case2, m2, hk2, ssite2 = get_case2()
    case3, m3, hk3, ssite3 = get_case3()
    case4, m4, hk4, ssite4 = get_case4()
