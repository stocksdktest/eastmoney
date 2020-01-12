import json

from protos_gen.config_pb2 import RunnerConfig, TestcaseConfig
from protos_gen.record_pb2 import TestExecutionRecord
from utils.base import generate_id, base64_encode, LogChunkCache
from utils.ios import config_plist, xctest_cmd, spawn_xcrun_log, parse_sim_log

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
            'QUOTE_NUMBERS': '600000.sh'
        })
    ])

    runner_conf.casesConfig.extend([case_conf])

    # case_conf = TestcaseConfig()
    # case_conf.testcaseID = 'TESTCASE_1'
    # case_conf.continueWhenFailed = False
    # case_conf.roundIntervalSec = 3
    # case_conf.paramStrs.extend([
    #     json.dumps({
    #         'QUOTE_NUMBERS': '600000.sh'
    #     })
    # ])
    #
    # runner_conf.casesConfig.extend([case_conf])

    # TODO Do not edit!
    print(base64_encode(runner_conf.SerializeToString()))
    if not config_plist(base64_encode(runner_conf.SerializeToString())):
        print("Config Info.Plist error")
        exit(1)

    chunk_cache = LogChunkCache()
    def read_record(record_str):
        record = TestExecutionRecord()
        data = parse_sim_log(chunk_cache, record_str)
        if data:
            record.ParseFromString(data)
        if len(record.ListFields()) > 0:
            print("*************************")
            print(record)
            print("*************************")

    spawn_xcrun_log(logger=read_record)


    test_result = False
    def check_test_result(line):
        global test_result
        if 'RUN-TESTS FAILED' in line:
            test_result = False
        elif 'RUN-TESTS SUCCEEDED' in line:
            test_result = True

    cmd_code = xctest_cmd(logger=check_test_result)
    print("status: ", (cmd_code == 0) and test_result)