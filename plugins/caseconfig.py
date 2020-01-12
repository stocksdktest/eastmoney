import json
from protos_gen.config_pb2 import RunnerConfig, TestcaseConfig

from utils.base import generate_id

import unittest
import logging, datetime
from utils_eastmoney.ParametrizedTestCase import ParametrizedTestCase
from utils_eastmoney.AppiumServer import AppiumServer
from utils_eastmoney.adb_utils import AndroidDebugBridge, getPhoneInfo
from case_class.login import Login
from case_class.quoteDetailRequest import QuoteDetailRequest
from case_class.tickRequest import TickRequest





def addSuite(runner_conf, app):
    suite = unittest.TestSuite()
    for cases in runner_conf.casesConfig:
        # print(cases.paramStrs)
        # print(type(cases.paramStrs), len(cases.paramStrs))
        # print(len(cases.paramStrs))
        for case in cases.paramStrs:
            tmp = json.loads(case)
            if tmp['request_type'] == 'QuoteDetailRequest':
                params = {**app, **(json.loads(case))}
                suite.addTest(ParametrizedTestCase.parametrize(QuoteDetailRequest, param=params))
            elif tmp['request_type'] == 'TickRequest':
                params = {**app, **(json.loads(case))}
                for i in range(tmp['repeat']):
                    suite.addTest(ParametrizedTestCase.parametrize(TickRequest, param=params))
            else:  # login
                params = {**app, **(json.loads(case))}
                suite.addTest(ParametrizedTestCase.parametrize(Login, param=params))

    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == '__main__':
    runner_conf = RunnerConfig()
    runner_conf.jobID = 'TJ-1'
    runner_conf.runnerID = generate_id('RUN-A')

    # case_conf = TestcaseConfig()
    # case_conf.testcaseID = 'Login'
    # case_conf.continueWhenFailed = False
    # case_conf.roundIntervalSec = 0
    # case_conf.paramStrs.extend([
    #     json.dumps({
    #         'request_type': 'login',
    #         'username': '13770961374',
    #         'password': 'ab123456'
    #     })
    # ])
    # runner_conf.casesConfig.extend([case_conf])

    # case_conf = TestcaseConfig()
    # case_conf.testcaseID = '900903.sh'
    # case_conf.continueWhenFailed = False
    # case_conf.roundIntervalSec = 0
    # case_conf.paramStrs.extend([
    #     json.dumps({
    #         'request_type': 'TickRequest',
    #         'stock_type': 'sh_sz',
    #         'stock_code': '900903.sh',
    #         'repeat': 1
    #     })
    # ])
    # runner_conf.casesConfig.extend([case_conf])

    # case_conf = TestcaseConfig()
    # case_conf.testcaseID = 'a2009.dce'
    # case_conf.continueWhenFailed = False
    # case_conf.roundIntervalSec = 0
    # case_conf.paramStrs.extend([
    #     json.dumps({
    #         'request_type': 'TickRequest',
    #         'stock_type': 'option_future',
    #         'stock_code': 'a2009.dce',
    #         'repeat': 1
    #     })
    # ])
    # runner_conf.casesConfig.extend([case_conf])



    # case_conf = TestcaseConfig()
    # case_conf.testcaseID = '000001.sh'
    # case_conf.continueWhenFailed = False
    # case_conf.roundIntervalSec = 0
    # case_conf.paramStrs.extend([
    #     json.dumps({
    #         'request_type': 'QuoteDetailRequest',
    #         'stock_type': 'sh_sz_index',
    #         'stock_code': '000001.sh',
    #         'repeat': 1
    #     })
    # ])
    # runner_conf.casesConfig.extend([case_conf])
    #
    # case_conf = TestcaseConfig()
    # case_conf.testcaseID = '000027.sh'
    # case_conf.continueWhenFailed = False
    # case_conf.roundIntervalSec = 0
    # case_conf.paramStrs.extend([
    #     json.dumps({
    #         'request_type': 'QuoteDetailRequest',
    #         'stock_type': 'sh_sz_index',
    #         'stock_code': '000027.sh',
    #         'repeat': 1
    #     })
    # ])
    # runner_conf.casesConfig.extend([case_conf])
    #
    # case_conf = TestcaseConfig()
    # case_conf.testcaseID = '010303.sh'
    # case_conf.continueWhenFailed = False
    # case_conf.roundIntervalSec = 0
    # case_conf.paramStrs.extend([
    #     json.dumps({
    #         'request_type': 'QuoteDetailRequest',
    #         'stock_type': 'bond',
    #         'stock_code': '010303.sh',
    #         'repeat': 1
    #     })
    # ])
    # runner_conf.casesConfig.extend([case_conf])
    #
    #
    # case_conf = TestcaseConfig()
    # case_conf.testcaseID = '018006.sh'
    # case_conf.continueWhenFailed = False
    # case_conf.roundIntervalSec = 0
    # case_conf.paramStrs.extend([
    #     json.dumps({
    #         'request_type': 'QuoteDetailRequest',
    #         'stock_type': 'bond',
    #         'stock_code': '018006.sh',
    #         'repeat': 1
    #     })
    # ])
    # runner_conf.casesConfig.extend([case_conf])
    #
    #
    #
    # case_conf = TestcaseConfig()
    # case_conf.testcaseID = '204001.sh'
    # case_conf.continueWhenFailed = False
    # case_conf.roundIntervalSec = 0
    # case_conf.paramStrs.extend([
    #     json.dumps({
    #         'request_type': 'QuoteDetailRequest',
    #         'stock_type': 'bond_sh_gz',
    #         'stock_code': '204001.sh',
    #         'repeat': 1
    #     })
    # ])
    # runner_conf.casesConfig.extend([case_conf])
    #
    #
    # case_conf = TestcaseConfig()
    # case_conf.testcaseID = '204002.sh'
    # case_conf.continueWhenFailed = False
    # case_conf.roundIntervalSec = 0
    # case_conf.paramStrs.extend([
    #     json.dumps({
    #         'request_type': 'QuoteDetailRequest',
    #         'stock_type': 'bond_sh_gz',
    #         'stock_code': '204002.sh',
    #         'repeat': 1
    #     })
    # ])
    # runner_conf.casesConfig.extend([case_conf])
    #
    #
    #
    # case_conf = TestcaseConfig()
    # case_conf.testcaseID = '204003.sh'
    # case_conf.continueWhenFailed = False
    # case_conf.roundIntervalSec = 0
    # case_conf.paramStrs.extend([
    #     json.dumps({
    #         'request_type': 'QuoteDetailRequest',
    #         'stock_type': 'bond_sh_gz',
    #         'stock_code': '204003.sh',
    #         'repeat': 1
    #     })
    # ])
    # runner_conf.casesConfig.extend([case_conf])
    #
    # case_conf = TestcaseConfig()
    # case_conf.testcaseID = '512760.sh'
    # case_conf.continueWhenFailed = False
    # case_conf.roundIntervalSec = 0
    # case_conf.paramStrs.extend([
    #     json.dumps({
    #         'request_type': 'QuoteDetailRequest',
    #         'stock_type': 'fund_ETF',
    #         'stock_code': '512760.sh',
    #         'repeat': 1
    #     })
    # ])
    # runner_conf.casesConfig.extend([case_conf])
    #
    # case_conf = TestcaseConfig()
    # case_conf.testcaseID = '600000.sh'
    # case_conf.continueWhenFailed = False
    # case_conf.roundIntervalSec = 0
    # case_conf.paramStrs.extend([
    #     json.dumps({
    #         'request_type': 'QuoteDetailRequest',
    #         'stock_type': 'sh_sz',
    #         'stock_code': '600000.sh',
    #         'repeat': 20
    #     })
    # ])
    # runner_conf.casesConfig.extend([case_conf])
    #
    # case_conf = TestcaseConfig()
    # case_conf.testcaseID = '601688.sh'
    # case_conf.continueWhenFailed = False
    # case_conf.roundIntervalSec = 0
    # case_conf.paramStrs.extend([
    #     json.dumps({
    #         'request_type': 'QuoteDetailRequest',
    #         'stock_type': 'sh_sz',
    #         'stock_code': '601688.sh',
    #         'repeat': 1
    #     })
    # ])
    # runner_conf.casesConfig.extend([case_conf])
    #
    # case_conf = TestcaseConfig()
    # case_conf.testcaseID = '900902.sh'
    # case_conf.continueWhenFailed = False
    # case_conf.roundIntervalSec = 0
    # case_conf.paramStrs.extend([
    #     json.dumps({
    #         'request_type': 'QuoteDetailRequest',
    #         'stock_type': 'sh_sz',
    #         'stock_code': '900902.sh',
    #         'repeat': 1
    #     })
    # ])
    # runner_conf.casesConfig.extend([case_conf])
    #
    # case_conf = TestcaseConfig()
    # case_conf.testcaseID = '900903.sh'
    # case_conf.continueWhenFailed = False
    # case_conf.roundIntervalSec = 0
    # case_conf.paramStrs.extend([
    #     json.dumps({
    #         'request_type': 'QuoteDetailRequest',
    #         'stock_type': 'sh_sz',
    #         'stock_code': '900903.sh',
    #         'repeat': 1
    #     })
    # ])
    # runner_conf.casesConfig.extend([case_conf])
    #
    # case_conf = TestcaseConfig()
    # case_conf.testcaseID = '900911.sh'
    # case_conf.continueWhenFailed = False
    # case_conf.roundIntervalSec = 0
    # case_conf.paramStrs.extend([
    #     json.dumps({
    #         'request_type': 'QuoteDetailRequest',
    #         'stock_type': 'sh_sz',
    #         'stock_code': '900911.sh',
    #         'repeat': 1
    #     })
    # ])
    # runner_conf.casesConfig.extend([case_conf])
    #
    # case_conf = TestcaseConfig()
    # case_conf.testcaseID = '900913.sh'
    # case_conf.continueWhenFailed = False
    # case_conf.roundIntervalSec = 0
    # case_conf.paramStrs.extend([
    #     json.dumps({
    #         'request_type': 'QuoteDetailRequest',
    #         'stock_type': 'sh_sz',
    #         'stock_code': '900913.sh',
    #         'repeat': 1
    #     })
    # ])
    # runner_conf.casesConfig.extend([case_conf])
    #
    # case_conf = TestcaseConfig()
    # case_conf.testcaseID = '10001926.sh'
    # case_conf.continueWhenFailed = False
    # case_conf.roundIntervalSec = 0
    # case_conf.paramStrs.extend([
    #     json.dumps({
    #         'request_type': 'QuoteDetailRequest',
    #         'stock_type': 'option',
    #         'stock_code': '10001926.sh',
    #         'repeat': 1
    #     })
    # ])
    # runner_conf.casesConfig.extend([case_conf])

    case_conf = TestcaseConfig()
    case_conf.testcaseID = '688001.sh'
    case_conf.continueWhenFailed = False
    case_conf.roundIntervalSec = 0
    case_conf.paramStrs.extend([
        json.dumps({
            'request_type': 'QuoteDetailRequest',
            'stock_type': 'sci_tech',
            'stock_code': '688001.sh',
            'repeat': 3
        })
    ])
    runner_conf.casesConfig.extend([case_conf])

    logging.warning("测试开始执行")
    start_time = datetime.datetime.now()
    devices = AndroidDebugBridge().get_attached_devices()

    if len(devices) > 0:
        dev = devices[0]
        portint = 4700
        bpint = 4750
        systemPortint = 4800

        app = {}
        app["devices"] = dev
        # print(getPhoneInfo(devices=dev))
        # exit(1)
        app['platformVersion'] = getPhoneInfo(devices=dev)['release']
        app["port"] = str(portint)
        app["bp"] = str(bpint)
        app["systemPort"] = systemPortint

        app[
            'app'] = '/Users/yuanganggang/Documents/UItest/eastmoney_validation/apps/com.eastmoney.android.berlin_8.3_8003000.apk'

        appium_server = AppiumServer([app])
        appium_server.start_server()  # 启动服务

        addSuite(runner_conf, app)
        try:
            appium_server.stop_server([app])
        except Exception as e:
            logging.warning("关闭服务失败，原因：%s" % e)
        end_time = datetime.datetime.now()
        hour = end_time - start_time
        # create(filename=filenm,devices_list=devicess,Test_version='2.0.1',testtime=str(hour))
        logging.warning("测试执行完毕，耗时：%s" % hour)


    else:
        logging.warning("没有可用的安卓设备")
