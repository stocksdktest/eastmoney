import json
import re

from protos_gen.config_pb2 import RunnerConfig, TestcaseConfig
from protos_gen.record_pb2 import TestExecutionRecord
from utils.base import LogChunkCache, base64_encode, generate_id
from utils.adb import exec_adb_cmd, parse_logcat, spawn_logcat

if __name__ == '__main__':
    runner_conf = RunnerConfig()
    runner_conf.jobID = 'TJ-1'
    runner_conf.runnerID = generate_id('RUN-A')

    runner_conf.sdkConfig.appKeyIOS = 'VVW0Fno7BEZt1a/y6KLM36uj9qcjw7CAHDwWZKDlWDs='
    runner_conf.sdkConfig.appKeyAndroid = 'J6IPlk5AEU+2/Yi59rfYnsFQtdtOgAo9GAzysx8ciOM='

    # runner_conf.sdkConfig.serverSites["shl2"].CopyFrom(Site(ips=["http://114.80.155.50:22016"]))

    runner_conf.sdkConfig.marketPerm.Level = "2"
    # runner_conf.sdkConfig.marketPerm.CffLevel = "2"
    # runner_conf.sdkConfig.marketPerm.DceLevel = "2"
    # runner_conf.sdkConfig.marketPerm.CzceLevel = "2"
    # runner_conf.sdkConfig.marketPerm.FeLevel = "2"
    # runner_conf.sdkConfig.marketPerm.GILevel = "2"
    # runner_conf.sdkConfig.marketPerm.ShfeLevel = "2"
    # runner_conf.sdkConfig.marketPerm.HKPerms.extend(["hk10", "hka1"])

    case_conf = TestcaseConfig()
    case_conf.testcaseID = 'TESTCASE_0'
    case_conf.continueWhenFailed = False
    case_conf.roundIntervalSec = 3
    case_conf.paramStrs.extend([
        json.dumps({
            'QUOTE_NUMBERS': '600028.sh'
        }),
        json.dumps({
            'QUOTE_NUMBERS': '600000.sh'
        })
    ])

    case_conf_2 = TestcaseConfig()
    case_conf_2.testcaseID = 'TESTCASE_2'
    case_conf_2.continueWhenFailed = False
    case_conf_2.roundIntervalSec = 3
    case_conf_2.paramStrs.extend([
        json.dumps({
            'QUOTE_NUMBERS': '600028.sh'
        })
    ])

    runner_conf.casesConfig.extend([case_conf, case_conf_2])

    print(base64_encode(runner_conf.SerializeToString()))
    chunk_cache = LogChunkCache()
    def read_record(record_str):
        # print(record_str)
        record = TestExecutionRecord()
        data = parse_logcat(chunk_cache, record_str)
        if data:
            record.ParseFromString(data)
        if len(record.ListFields()) > 0:
            print("*************************")
            print(record)
            print("*************************")

    spawn_logcat(serial='ZX1G22DBHC', logger=read_record)

    test_status_code = []
    def check_test_result(line):
        if 'INSTRUMENTATION_STATUS_CODE' in line:
            # find number in string, https://stackoverflow.com/a/29581287/9797889
            codes = re.findall("[-+]?[.]?[\d]+(?:,\d\d\d)*[\.]?\d*(?:[eE][-+]?\d+)?", line)
            # check whether code ONLY contains '0' or '1'
            test_status_code.extend(codes)

    cmd_code = exec_adb_cmd([
        'adb', 'shell', 'am', 'instrument', '-w', '-r',
        '-e', 'debug', 'false',
        '-e', 'filter', 'com.chi.ssetest.TestcaseFilter',
        '-e', 'listener', 'com.chi.ssetest.TestcaseExecutionListener',
        '-e', 'collector_file', 'test.log',
        '-e', 'runner_config', base64_encode(runner_conf.SerializeToString()),
        'com.chi.ssetest.test/android.support.test.runner.AndroidJUnitRunner'
    ], serial='ZX1G22DBHC', logger=check_test_result)

    print("status: ", (cmd_code == 0) and \
			   len(test_status_code) > 0 and \
			   (test_status_code.count('0') + test_status_code.count('1') == len(test_status_code)))