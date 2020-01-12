import json

import airflow
from airflow.models import DAG
from airflow.operators.dummy_operator import DummyOperator

from operators.data_compare_operator import DataCompareOperator
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
				'quoteitem':'600000.sh',
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
		print('i,case_list.length is ',case_list.__len__())
		runner_conf_list.append(runner_conf)

	return runner_conf_list

with DAG(
		dag_id='android_test_release',
		default_args={
			'owner': 'airflow',
			'start_date': airflow.utils.dates.days_ago(0)
		},
		schedule_interval='@once',
) as dag:
	start_task = DummyOperator(
		task_id='run_this_first',
		queue='worker'
	)

	# release_ok = DummyOperator(
	# 	task_id='release_ok',
	# 	queue='worker'
	# )

	run_this_last = DummyOperator(
		task_id='run_this_last',
		queue='worker'
	)

	runner_conf_list = initRunnerConfig()
	task_id_to_cmp_list = ['adb_release_cmp_a','adb_release_cmp_b']

	# android_release1 = AndroidReleaseOperator(
	# 	task_id='android_release1',
	# 	provide_context=False,
	# 	repo_name='stocksdktest/AndroidTestRunner',
	# 	tag_id='release-20191030-0.0.2',
	# 	tag_sha='91af71d21a42200c63ae4f37bd8f2bcf868866c5',
	# 	runner_conf=runner_conf_list[0]
	# )
	#
	# android_release2 = AndroidReleaseOperator(
	# 	task_id='android_release2',
	# 	provide_context=False,
	# 	repo_name='stocksdktest/AndroidTestRunner',
	# 	tag_id='release-20191113_v3.1.0.004',
	# 	tag_sha='eac1fb7aae8a4c23097a2d3c14be7e259aab88e0',
	# 	runner_conf=runner_conf_list[0]
	# )

	android_a = AndroidRunnerOperator(
		task_id=task_id_to_cmp_list[0],
		provide_context=False,
		apk_id='com.chi.ssetest',
		apk_version='release-20191030-0.0.2',
		runner_conf=runner_conf_list[0]
	)

	android_b = AndroidRunnerOperator(
		task_id=task_id_to_cmp_list[1],
		provide_context=False,
		apk_id='com.chi.ssetest',
		apk_version='release-20191113_v3.1.0.004',
		runner_conf=runner_conf_list[1]
	)

	android_cmp = DataCompareOperator(
		task_id='data_compare',
		task_id_list=task_id_to_cmp_list,
		retries=3,
		provide_context=False,
		runner_conf=RunnerConfig,
		dag=dag
	)

	# android_cmp2 = DataCompareOperator(
	# 	task_id='data_compare2',
	# 	task_id_list=task_id_to_cmp_list,
	# 	retries=3,
	# 	provide_context=False,
	# 	runner_conf=RunnerConfig,
	# 	dag=dag
	# )

	start_task >> [android_a, android_b] >> android_cmp >> run_this_last
	# start_task >> android_release >> android_a >> android_cmp >> run_this_last

if __name__ == "__main__":
	dag.cli()