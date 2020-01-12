import re
import os
import sys

import paramiko
import json

from airflow.contrib.hooks.mongo_hook import MongoHook
from airflow.exceptions import AirflowException
from airflow.utils.decorators import apply_defaults

from operators.stock_operator import StockOperator

# TODO only this import style can work on airflow
from protos_gen import *
from protos_gen.config_pb2 import Site
from utils import *
from utils.base import bytes_to_dict

# OSX_HOSTNAME = '172.27.135.151'
OSX_HOSTNAME = '172.27.142.94'
# OSX_USER_ID = 'yuanganggang'
OSX_USER_ID = 'env_test'
OSX_UESR_PWD = 'yuan020218'
# OSX_UESR_PWD = 'ab123456'
SSH_TIMEOUT = 20
IOS_REPO_PATH = '/Users/yuanganggang/Downloads/IOSTestRunner-master'
# IOS_REPO_PATH = '/Users/env_test/Documents/repo/IOSTestRunner'


class IOSStockOperator(StockOperator):
	@apply_defaults
	def __init__(self, app_id, project_path, runner_conf, *args, **kwargs):
		super(IOSStockOperator, self).__init__(queue='osx', runner_conf=runner_conf, *args, **kwargs)
		self.ssh_key_path = '/root/.ssh/id_rsa'
		self.app_id = app_id
		self.project_path = project_path
		self.ssh_cmd = 'ssh %s@%s ' % (OSX_USER_ID, OSX_HOSTNAME)
		self.ssh_client = paramiko.SSHClient()
		self.mongo_hk = MongoHook()
		self.conn = self.mongo_hk.get_conn()
		self.dict_list = []

	def pre_execute(self, context):
		# check login without password
		# ssh_client = paramiko.SSHClient()
		# ssh_client.load_host_keys(self.ssh_key_path)
		try:
			# ssh_client.connect(hostname=OSX_HOSTNAME, port=22, username=OSX_USER_ID, timeout=SSH_TIMEOUT)
			self.ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
			self.ssh_client.connect(hostname=OSX_HOSTNAME, port=22, username=OSX_USER_ID, password=OSX_UESR_PWD,
									timeout=SSH_TIMEOUT)
			stdin, stdout,stderr = self.ssh_client.exec_command('echo "ok"')
		except paramiko.SSHException as e:
			raise AirflowException(str(e))

	# self.ssh_client.exec_command('mkdir -p %s' % IOS_REPO_PATH)
	# self.ssh_client.exec_command('git clone --depth=1 %s %s')

	@staticmethod
	def protobuf_record_to_dict(record):
		if record is None:
			sys.stderr('TextExecutionRecordtoDict Type Error, param is NoneType')
			return
		if type(record) != TestExecutionRecord:
			sys.stderr('TextExecutionRecordtoDict Type Error, param is not TestExecutionRecord')
			return
		res = dict()
		res['jobID'] = record.jobID
		res['runnerID'] = record.runnerID
		res['testcaseID'] = record.testcaseID
		res['recordID'] = record.recordID
		res['isPass'] = record.isPass
		res['startTime'] = record.startTime
		res['paramData'] = bytes_to_dict(record.paramData)
		res['resultData'] = bytes_to_dict(record.resultData)
		res['exceptionData'] = bytes_to_dict(record.exceptionData)
		return res

	def execute(self, context):
		stdin, stdout, stderr = self.ssh_client.exec_command('echo "ok"')
		if len(stderr.read()) != 0:
			print(stderr.read())
			raise AirflowException('Broken SSH connection')



		# TODO Do not edit!
		print(base64_encode(self.runner_conf.SerializeToString()))
		if not config_plist(ssh_cmd=self.ssh_cmd, serialize_config=base64_encode(self.runner_conf.SerializeToString())):
			print("Config Info.Plist error")
			exit(1)

		print("-----------1---------------")

		chunk_cache = LogChunkCache()

		result = []

		def read_record(record_str):
			record = TestExecutionRecord()
			data = parse_sim_log(chunk_cache, record_str)
			if data:
				record.ParseFromString(data)
			if len(record.ListFields()) > 0:
				print("*************************")
				print(record)
				self.dict_list.append(self.protobuf_record_to_dict(record))
				print("*************************")

		spawn_xcrun_log(ssh_cmd=self.ssh_cmd,logger=read_record)

		test_result = False

		def check_test_result(line):
			global test_result
			if 'RUN-TESTS FAILED' in line:
				test_result = False
			elif 'RUN-TESTS SUCCEEDED' in line:
				test_result = True

		cmd_code = xctest_cmd(ssh_cmd=self.ssh_cmd, logger=check_test_result)
		print("status: ", (cmd_code == 0) and test_result)

		myclient = self.mongo_hk.client
		mydb = myclient["stockSdkTest"]
		col = mydb[self.task_id]
		print('Debug Airflow: dict_list:---------------')
		print(self.dict_list)
		try:
			col.insert_many(self.dict_list)
		except TypeError as s:
			print(s)
		finally:
			self.xcom_push(context, key=self.task_id, value=self.runner_conf.runnerID)


if __name__ == '__main__':
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

	ios_task = IOSStockOperator(
		task_id="1",
		app_id="2",
		project_path="",
		runner_conf=runner_conf
	)
	ios_task.pre_execute("")
	# ios_task.execute("")
	stdin, stdout, stderr = ios_task.ssh_client.exec_command('echo "ok"')
