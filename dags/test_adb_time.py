import json
from airflow.utils.timezone import datetime

import airflow
from airflow.models import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.dummy_operator import DummyOperator
from airflow.utils.timezone import datetime

from operators.data_compare_operator import DataCompareOperator, generate_id
from protos_gen.config_pb2 import RunnerConfig, TestcaseConfig, Site
from operators.android_runner_operator import AndroidRunnerOperator
from operators.android_release_operator import AndroidReleaseOperator


# TODO init RunnerConfig
def initRunnerConfig():
	runner_conf_list = []

	for i in range(2):
		runner_conf = RunnerConfig()

		runner_conf.sdkConfig.appKeyIOS = 'VVW0Fno7BEZt1a/y6KLM36uj9qcjw7CAHDwWZKDlWDs='
		runner_conf.sdkConfig.appKeyAndroid = 'J6IPlk5AEU+2/Yi59rfYnsFQtdtOgAo9GAzysx8ciOM='
		runner_conf.sdkConfig.marketPerm.Level = "2"
		runner_conf.sdkConfig.marketPerm.HKPerms.extend(["hk10"])

		if i == 0:
			runner_conf.sdkConfig.serverSites["sh"].CopyFrom(Site(ips=["http://114.80.155.134:22016"]))
			runner_conf.sdkConfig.serverSites["sz"].CopyFrom(Site(ips=["http://114.80.155.134:22016"]))
			runner_conf.sdkConfig.serverSites["bj"].CopyFrom(Site(ips=["http://114.80.155.134:22016"]))
			runner_conf.sdkConfig.serverSites["cf"].CopyFrom(Site(ips=["http://114.80.155.134:22016"]))
			runner_conf.sdkConfig.serverSites["nf"].CopyFrom(Site(ips=["http://114.80.155.134:22013"]))
			runner_conf.sdkConfig.serverSites["gf"].CopyFrom(Site(ips=["http://114.80.155.134:22013"]))
			runner_conf.sdkConfig.serverSites["pb"].CopyFrom(Site(ips=["http://114.80.155.134:22016"]))
			runner_conf.sdkConfig.serverSites["hk1"].CopyFrom(Site(ips=["http://114.80.155.133:22016"]))
			runner_conf.sdkConfig.serverSites["hk5"].CopyFrom(Site(ips=["http://114.80.155.133:22016"]))
			runner_conf.sdkConfig.serverSites["hk10"].CopyFrom(Site(ips=["http://114.80.155.133:22016"]))
			runner_conf.sdkConfig.serverSites["hka1"].CopyFrom(Site(ips=["http://114.80.155.133:22016"]))
			runner_conf.sdkConfig.serverSites["hkd1"].CopyFrom(Site(ips=["http://114.80.155.133:22016"]))
			runner_conf.sdkConfig.serverSites["hkaz"].CopyFrom(Site(ips=["http://114.80.155.133:22016"]))
			runner_conf.sdkConfig.serverSites["hkdz"].CopyFrom(Site(ips=["http://114.80.155.133:22016"]))
		else:
			runner_conf.sdkConfig.serverSites["sh"].CopyFrom(Site(ips=["http://114.80.155.134:22016"]))
			runner_conf.sdkConfig.serverSites["sz"].CopyFrom(Site(ips=["http://114.80.155.134:22016"]))
			runner_conf.sdkConfig.serverSites["bj"].CopyFrom(Site(ips=["http://114.80.155.134:22016"]))
			runner_conf.sdkConfig.serverSites["cf"].CopyFrom(Site(ips=["http://114.80.155.134:22016"]))
			runner_conf.sdkConfig.serverSites["nf"].CopyFrom(Site(ips=["http://114.80.155.134:22013"]))
			runner_conf.sdkConfig.serverSites["gf"].CopyFrom(Site(ips=["http://114.80.155.134:22013"]))
			runner_conf.sdkConfig.serverSites["pb"].CopyFrom(Site(ips=["http://114.80.155.134:22016"]))
			runner_conf.sdkConfig.serverSites["hk1"].CopyFrom(Site(ips=["http://114.80.155.58:8601"]))
			runner_conf.sdkConfig.serverSites["hk5"].CopyFrom(Site(ips=["http://114.80.155.58:8601"]))
			runner_conf.sdkConfig.serverSites["hk10"].CopyFrom(Site(ips=["http://114.80.155.58:8601"]))
			runner_conf.sdkConfig.serverSites["hka1"].CopyFrom(Site(ips=["http://114.80.155.58:8601"]))
			runner_conf.sdkConfig.serverSites["hkd1"].CopyFrom(Site(ips=["http://114.80.155.58:8601"]))
			runner_conf.sdkConfig.serverSites["hkaz"].CopyFrom(Site(ips=["http://114.80.155.58:8601"]))
			runner_conf.sdkConfig.serverSites["hkdz"].CopyFrom(Site(ips=["http://114.80.155.58:8601"]))
		case_list = []

		case_conf = TestcaseConfig()
		case_conf.testcaseID = 'OHLCTEST_1'
		case_conf.roundIntervalSec = 3
		case_conf.continueWhenFailed = False
		case_conf.paramStrs.extend([
			json.dumps({
				'stk': '00700.hk',
				'type': 'dayk'
			})
		])
		case_list.append(case_conf)

		case_conf = TestcaseConfig()
		case_conf.testcaseID = 'CHARTSUB_2'
		case_conf.roundIntervalSec = 3
		case_conf.continueWhenFailed = False
		case_conf.paramStrs.extend([
			json.dumps({
				'quoteitem': '600000.sh',
				'type': 'ChartTypeOneDay',
				'begin': '0',
				'end': '100',
				'select': 'time,ddx,ddy,ddz'
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
				'CODES': '00700.hk',
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
				'CODES': '00700.hk',
				'TYPES': 'dayk',
				'FqTypes': '1',
				'DATES': 'null'
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
				'CODES': '00700.hk',
				'TYPES': 'dayk',
				'FqTypes': '2',
				'Dates': 'null',
				'Numbers': '300'
			})
		])
		case_list.append(case_conf)

		runner_conf.casesConfig.extend(case_list)
		print('i,case_list.length is ', case_list.__len__())
		runner_conf_list.append(runner_conf)

	return runner_conf_list


def gen2confict_1():
	runner_conf_list = []
	for i in range(2):
		runner_conf = RunnerConfig()
		runner_conf.jobID = 'TJ-1'
		runner_conf.runnerID = generate_id('RUN-A')
		runner_conf.sdkConfig.appKeyIOS = 'VVW0Fno7BEZt1a/y6KLM36uj9qcjw7CAHDwWZKDlWDs='
		runner_conf.sdkConfig.appKeyAndroid = 'J6IPlk5AEU+2/Yi59rfYnsFQtdtOgAo9GAzysx8ciOM='
		runner_conf.sdkConfig.marketPerm.Level = "1"
		runner_conf.sdkConfig.marketPerm.HKPerms.extend(["hk10"])

		if i == 0:
			runner_conf.sdkConfig.serverSites["sh"].CopyFrom(Site(ips=["http://114.80.155.134:22016"]))
			runner_conf.sdkConfig.serverSites["sz"].CopyFrom(Site(ips=["http://114.80.155.134:22016"]))
			runner_conf.sdkConfig.serverSites["bj"].CopyFrom(Site(ips=["http://114.80.155.134:22016"]))
			runner_conf.sdkConfig.serverSites["cf"].CopyFrom(Site(ips=["http://114.80.155.134:22016"]))
			runner_conf.sdkConfig.serverSites["nf"].CopyFrom(Site(ips=["http://114.80.155.134:22013"]))
			runner_conf.sdkConfig.serverSites["gf"].CopyFrom(Site(ips=["http://114.80.155.134:22013"]))
			runner_conf.sdkConfig.serverSites["pb"].CopyFrom(Site(ips=["http://114.80.155.134:22016"]))
			runner_conf.sdkConfig.serverSites["hk1"].CopyFrom(Site(ips=["http://114.80.155.133:22016"]))
			runner_conf.sdkConfig.serverSites["hk5"].CopyFrom(Site(ips=["http://114.80.155.133:22016"]))
			runner_conf.sdkConfig.serverSites["hk10"].CopyFrom(Site(ips=["http://114.80.155.133:22016"]))
			runner_conf.sdkConfig.serverSites["hka1"].CopyFrom(Site(ips=["http://114.80.155.133:22016"]))
			runner_conf.sdkConfig.serverSites["hkd1"].CopyFrom(Site(ips=["http://114.80.155.133:22016"]))
			runner_conf.sdkConfig.serverSites["hkaz"].CopyFrom(Site(ips=["http://114.80.155.133:22016"]))
			runner_conf.sdkConfig.serverSites["hkdz"].CopyFrom(Site(ips=["http://114.80.155.133:22016"]))
		else:
			runner_conf.sdkConfig.serverSites["sh"].CopyFrom(Site(ips=["http://114.80.155.134:22016"]))
			runner_conf.sdkConfig.serverSites["sz"].CopyFrom(Site(ips=["http://114.80.155.134:22016"]))
			runner_conf.sdkConfig.serverSites["bj"].CopyFrom(Site(ips=["http://114.80.155.134:22016"]))
			runner_conf.sdkConfig.serverSites["cf"].CopyFrom(Site(ips=["http://114.80.155.134:22016"]))
			runner_conf.sdkConfig.serverSites["nf"].CopyFrom(Site(ips=["http://114.80.155.134:22013"]))
			runner_conf.sdkConfig.serverSites["gf"].CopyFrom(Site(ips=["http://114.80.155.134:22013"]))
			runner_conf.sdkConfig.serverSites["pb"].CopyFrom(Site(ips=["http://114.80.155.134:22016"]))
			runner_conf.sdkConfig.serverSites["hk1"].CopyFrom(Site(ips=["http://114.80.155.58:8601"]))
			runner_conf.sdkConfig.serverSites["hk5"].CopyFrom(Site(ips=["http://114.80.155.58:8601"]))
			runner_conf.sdkConfig.serverSites["hk10"].CopyFrom(Site(ips=["http://114.80.155.58:8601"]))
			runner_conf.sdkConfig.serverSites["hka1"].CopyFrom(Site(ips=["http://114.80.155.58:8601"]))
			runner_conf.sdkConfig.serverSites["hkd1"].CopyFrom(Site(ips=["http://114.80.155.58:8601"]))
			runner_conf.sdkConfig.serverSites["hkaz"].CopyFrom(Site(ips=["http://114.80.155.58:8601"]))
			runner_conf.sdkConfig.serverSites["hkdz"].CopyFrom(Site(ips=["http://114.80.155.58:8601"]))

		case_conf = TestcaseConfig()
		case_conf.testcaseID = 'OHLCTEST_1'
		case_conf.roundIntervalSec = 3
		case_conf.continueWhenFailed = False
		case_conf.paramStrs.extend([
			json.dumps({
				'stk': '00700.hk',
				'type': 'dayk'
			})
		])
		runner_conf.casesConfig.extend([case_conf])
		runner_conf_list.append(runner_conf)
	return runner_conf_list


def gen2confict_2():
	runner_conf_list = []
	for i in range(2):
		runner_conf = RunnerConfig()
		runner_conf.jobID = 'TJ-1'
		runner_conf.runnerID = generate_id('RUN-A')
		runner_conf.sdkConfig.appKeyIOS = 'VVW0Fno7BEZt1a/y6KLM36uj9qcjw7CAHDwWZKDlWDs='
		runner_conf.sdkConfig.appKeyAndroid = 'J6IPlk5AEU+2/Yi59rfYnsFQtdtOgAo9GAzysx8ciOM='
		runner_conf.sdkConfig.marketPerm.Level = "1"
		runner_conf.sdkConfig.marketPerm.HKPerms.extend(["hk10"])

		if i == 0:
			runner_conf.sdkConfig.serverSites["sh"].CopyFrom(Site(ips=["http://114.80.155.134:22016"]))
			runner_conf.sdkConfig.serverSites["sz"].CopyFrom(Site(ips=["http://114.80.155.134:22016"]))
			runner_conf.sdkConfig.serverSites["bj"].CopyFrom(Site(ips=["http://114.80.155.134:22016"]))
			runner_conf.sdkConfig.serverSites["cf"].CopyFrom(Site(ips=["http://114.80.155.134:22016"]))
			runner_conf.sdkConfig.serverSites["nf"].CopyFrom(Site(ips=["http://114.80.155.134:22013"]))
			runner_conf.sdkConfig.serverSites["gf"].CopyFrom(Site(ips=["http://114.80.155.134:22013"]))
			runner_conf.sdkConfig.serverSites["pb"].CopyFrom(Site(ips=["http://114.80.155.134:22016"]))
			runner_conf.sdkConfig.serverSites["hk1"].CopyFrom(Site(ips=["http://114.80.155.133:22016"]))
			runner_conf.sdkConfig.serverSites["hk5"].CopyFrom(Site(ips=["http://114.80.155.133:22016"]))
			runner_conf.sdkConfig.serverSites["hk10"].CopyFrom(Site(ips=["http://114.80.155.133:22016"]))
			runner_conf.sdkConfig.serverSites["hka1"].CopyFrom(Site(ips=["http://114.80.155.133:22016"]))
			runner_conf.sdkConfig.serverSites["hkd1"].CopyFrom(Site(ips=["http://114.80.155.133:22016"]))
			runner_conf.sdkConfig.serverSites["hkaz"].CopyFrom(Site(ips=["http://114.80.155.133:22016"]))
			runner_conf.sdkConfig.serverSites["hkdz"].CopyFrom(Site(ips=["http://114.80.155.133:22016"]))
		else:
			runner_conf.sdkConfig.serverSites["sh"].CopyFrom(Site(ips=["http://114.80.155.61:22016"]))
			runner_conf.sdkConfig.serverSites["sz"].CopyFrom(Site(ips=["http://114.80.155.61:22016"]))
			runner_conf.sdkConfig.serverSites["bj"].CopyFrom(Site(ips=["http://114.80.155.61:22016"]))
			runner_conf.sdkConfig.serverSites["cf"].CopyFrom(Site(ips=["http://114.80.155.61:22016"]))
			runner_conf.sdkConfig.serverSites["nf"].CopyFrom(Site(ips=["http://114.80.155.61:22013"]))
			runner_conf.sdkConfig.serverSites["gf"].CopyFrom(Site(ips=["http://114.80.155.61:22013"]))
			runner_conf.sdkConfig.serverSites["pb"].CopyFrom(Site(ips=["http://114.80.155.61:22016"]))
			runner_conf.sdkConfig.serverSites["hk1"].CopyFrom(Site(ips=["http://114.80.155.133:22016"]))
			runner_conf.sdkConfig.serverSites["hk5"].CopyFrom(Site(ips=["http://114.80.155.133:22016"]))
			runner_conf.sdkConfig.serverSites["hk10"].CopyFrom(Site(ips=["http://114.80.155.133:22016"]))
			runner_conf.sdkConfig.serverSites["hka1"].CopyFrom(Site(ips=["http://114.80.155.133:22016"]))
			runner_conf.sdkConfig.serverSites["hkd1"].CopyFrom(Site(ips=["http://114.80.155.133:22016"]))
			runner_conf.sdkConfig.serverSites["hkaz"].CopyFrom(Site(ips=["http://114.80.155.133:22016"]))
			runner_conf.sdkConfig.serverSites["hkdz"].CopyFrom(Site(ips=["http://114.80.155.133:22016"]))

		case_conf = TestcaseConfig()
		case_conf.testcaseID = 'CHARTSUB_2'
		case_conf.roundIntervalSec = 3
		case_conf.continueWhenFailed = False
		case_conf.paramStrs.extend([
			json.dumps({
				'quoteitem': '600000.sh',
				'type': 'ChartTypeOneDay',
				'begin': '0',
				'end': '100',
				'select': 'time,ddx,ddy,ddz'
			})
		])

		runner_conf.casesConfig.extend([case_conf])
		runner_conf_list.append(runner_conf)
	return runner_conf_list


with DAG(
		dag_id='android_test_time',
		default_args={
			'owner': 'airflow',
			# 'start_date': airflow.utils.dates.days_ago(0),
			'start_date': datetime(2019,11,14,1,30),
		},
		schedule_interval='@once',
) as dag:
	start_task = DummyOperator(
		task_id='run_this_first',
	)

	run_this_last = DummyOperator(
		task_id='run_this_last',
		queue='android'
	)

	runner_conf_list1 = initRunnerConfig()
	runner_conf_list2 = gen2confict_1()
	runner_conf_list3 = gen2confict_2()
	task_id_to_cmp_list1 = ['adb_cmp_pro_a1', 'adb_cmp_pro_b1']
	task_id_to_cmp_list2 = ['adb_cmp_pro_a2', 'adb_cmp_pro_b2']
	task_id_to_cmp_list3 = ['adb_cmp_pro_a3', 'adb_cmp_pro_b3']

	# android_release = AndroidReleaseOperator(
	# 	task_id='android_release',
	# 	provide_context=False,
	# 	repo_name='stocksdktest/AndroidTestRunner',
	# 	tag_id='release-20191016-0.0.3',
	# 	tag_sha='16a5ad8d128df1b55f962b52e87bac481f98475f',
	# 	runner_conf=runner_conf_list[0]
	# )

	android_1 = AndroidRunnerOperator(
		task_id=task_id_to_cmp_list1[0],
		provide_context=False,
		apk_id='com.chi.ssetest',
		apk_version='release-20191016-0.0.3',
		runner_conf=runner_conf_list3[0]
	)

	android_2 = AndroidRunnerOperator(
		task_id=task_id_to_cmp_list1[1],
		provide_context=False,
		apk_id='com.chi.ssetest',
		apk_version='release-20191016-0.0.3',
		runner_conf=runner_conf_list3[1]
	)

	android_3 = AndroidRunnerOperator(
		task_id=task_id_to_cmp_list2[0],
		provide_context=False,
		apk_id='com.chi.ssetest',
		apk_version='release-20191016-0.0.3',
		runner_conf=runner_conf_list3[0]
	)

	android_4 = AndroidRunnerOperator(
		task_id=task_id_to_cmp_list2[1],
		provide_context=False,
		apk_id='com.chi.ssetest',
		apk_version='release-20191016-0.0.3',
		runner_conf=runner_conf_list3[1]
	)

	android_5 = AndroidRunnerOperator(
		task_id=task_id_to_cmp_list3[0],
		provide_context=False,
		apk_id='com.chi.ssetest',
		apk_version='release-20191016-0.0.3',
		runner_conf=runner_conf_list3[0]
	)

	android_6 = AndroidRunnerOperator(
		task_id=task_id_to_cmp_list3[1],
		provide_context=False,
		apk_id='com.chi.ssetest',
		apk_version='release-20191016-0.0.3',
		runner_conf=runner_conf_list3[1]
	)

	android_cmp1 = DataCompareOperator(
		task_id='data_compare',
		task_id_list=task_id_to_cmp_list1,
		retries=3,
		provide_context=False,
		runner_conf=RunnerConfig,
		dag=dag
	)

	android_cmp2 = DataCompareOperator(
		task_id='data_compare2',
		task_id_list=task_id_to_cmp_list2,
		retries=3,
		provide_context=False,
		runner_conf=RunnerConfig,
		dag=dag
	)

	android_cmp3 = DataCompareOperator(
		task_id='data_compare3',
		task_id_list=task_id_to_cmp_list3,
		retries=3,
		provide_context=False,
		runner_conf=RunnerConfig,
		dag=dag
	)

	start_task >> [android_1, android_2] >> android_cmp1 >> [android_3, android_4] >> android_cmp2 >> [android_5,android_6] >> android_cmp3 >> run_this_last



if __name__ == "__main__":
	dag.cli()
