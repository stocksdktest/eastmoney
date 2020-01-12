import json
from datetime import timedelta

import airflow
from airflow.models import DAG
from airflow.operators.dummy_operator import DummyOperator

from operators.data_compare_operator import DataCompareOperator, generate_id
from operators.ios_operator import IOSStockOperator
from protos_gen.config_pb2 import RunnerConfig, TestcaseConfig, Site

def gen2iOSCaseList():
	res = []
	for i in range(2):
		runner_conf = RunnerConfig()
		runner_conf.jobID = 'TJ-1'
		runner_conf.runnerID = generate_id('RUN-A')
		runner_conf.sdkConfig.appKeyIOS = 'VVW0Fno7BEZt1a/y6KLM36uj9qcjw7CAHDwWZKDlWDs='
		runner_conf.sdkConfig.appKeyAndroid = 'J6IPlk5AEU+2/Yi59rfYnsFQtdtOgAo9GAzysx8ciOM='
		runner_conf.sdkConfig.marketPerm.Level = "2"

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
		res.append(runner_conf)

	return  res

with DAG(
		dag_id='ios_test',
		default_args={
			'owner': 'airflow',
			'start_date': airflow.utils.dates.days_ago(0),
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


	task_id_to_cmp_list1 = ['ios_cmp_a1','ios_cmp_a2']
	# runner_conf_list = gen2iOSCaseList()

	runner_conf = RunnerConfig()
	runner_conf.jobID = 'TJ-1'
	runner_conf.runnerID = generate_id('RUN-A')

	runner_conf.sdkConfig.appKeyIOS = 'VVW0Fno7BEZt1a/y6KLM36uj9qcjw7CAHDwWZKDlWDs='
	runner_conf.sdkConfig.appKeyAndroid = 'J6IPlk5AEU+2/Yi59rfYnsFQtdtOgAo9GAzysx8ciOM='

	runner_conf.sdkConfig.marketPerm.Level = "1"
	runner_conf.sdkConfig.marketPerm.HKPerms.extend(["hk10", "hka1"])
	runner_conf.sdkConfig.serverSites["sh"].CopyFrom(Site(ips=["http://114.80.155.134:22016"]))
	runner_conf.sdkConfig.serverSites["sz"].CopyFrom(Site(ips=["http://114.80.155.134:22016"]))
	runner_conf.sdkConfig.serverSites["cf"].CopyFrom(Site(ips=["http://114.80.155.134:22016"]))
	runner_conf.sdkConfig.serverSites["nf"].CopyFrom(Site(ips=["http://114.80.155.134:22013"]))
	runner_conf.sdkConfig.serverSites["pb"].CopyFrom(Site(ips=["http://114.80.155.134:22016"]))
	runner_conf.sdkConfig.serverSites["hk10"].CopyFrom(Site(ips=["http://114.80.155.133:22016"]))

	case_conf = TestcaseConfig()
	case_conf.testcaseID = 'AHQuoteListTestCase1'
	case_conf.continueWhenFailed = False
	case_conf.roundIntervalSec = 3
	case_conf.paramStrs.extend([
		json.dumps({
			'PAGE_SIZE': '12',
			'PAGE_INDEX': '0',
			'ASC?': 'no',
			'FIELD': '2'
		})
	])

	runner_conf.casesConfig.extend([case_conf])

	ios_1 = IOSStockOperator(
		task_id=task_id_to_cmp_list1[0],
		provide_context=False,
		app_id="2",
		project_path="",
		runner_conf=runner_conf
	)

	ios_2 = IOSStockOperator(
		task_id=task_id_to_cmp_list1[1],
		provide_context=False,
		app_id="2",
		project_path="",
		runner_conf=runner_conf
	)

	ios_cmp1 = DataCompareOperator(
		task_id='data_compare',
		task_id_list=task_id_to_cmp_list1,
		retries=3,
		provide_context=False,
		runner_conf=RunnerConfig,
		dag=dag
	)

	start_task >> [ios_1, ios_2] >> ios_cmp1  >>run_this_last

if __name__ == "__main__":
	dag.cli()
