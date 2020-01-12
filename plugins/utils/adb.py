import subprocess
import os
import re
import time
import platform
import threading
import binascii

from utils import base

ADB_EXEC_PATH = '/usr/local/bin/adb' if platform.system() == 'Darwin' else '/usr/bin/adb'


def scan_local_device():
	device_serial = None

	def parse_serial(line):
		global device_serial
		reg_obj = re.search(r'(emulator-\d+)', line)
		if reg_obj:
			device_serial = reg_obj.groups()[0]

	if exec_adb_cmd(['adb', 'devices'], logger=parse_serial) != 0:
		return None
	return device_serial


def connect_to_device(serial):
	connection = {
		'status': False
	}

	def parse_connection_status(line):
		reg_obj = re.search(r'connected to', line)
		connection['status'] |= (reg_obj is not None)

	if exec_adb_cmd(['adb', 'connect', serial], logger=parse_connection_status) != 0 or not connection['status']:
		return False
	# TODO
	# prevent adb response with 'device offline'
	# time.sleep(2)
	exec_adb_cmd(['adb', 'devices'])
	if exec_adb_cmd(['adb', 'shell', 'echo', 'ok'], serial=serial) != 0:
		return False
	return True


"""
:param args: [str]
:param serial: str
:param logger: lambda: (str) -> {}
"""


def exec_adb_cmd(args, serial=None, logger=None):
	adb_env = os.environ.copy()
	if serial:
		adb_env['ANDROID_SERIAL'] = serial
	# TODO replace ADB_EXEC_PATH
	with subprocess.Popen(args, executable=ADB_EXEC_PATH, stdout=subprocess.PIPE, env=adb_env) as process:
		def timeout_callback():
			print('process has timeout')
			process.kill()

		# kill process in timeout seconds unless the timer is restarted
		watchdog = base.WatchdogTimer(timeout=30, callback=timeout_callback, daemon=True)
		watchdog.start()
		for line in process.stdout:
			# don't invoke the watcthdog callback if do_something() takes too long
			with watchdog.blocked:
				if not line:
					process.kill()
					break
				if logger and callable(logger):
					logger(str(line))
				os.write(1, line)
				watchdog.restart()
		watchdog.cancel()
	return process.returncode


def spawn_logcat(serial=None, logger=None):
	def read_log():
		adb_env = os.environ.copy()
		if serial:
			adb_env['ANDROID_SERIAL'] = serial

		# ignore return code
		subprocess.call(args=["adb", "logcat", "-c"], executable=ADB_EXEC_PATH, env=adb_env)

		process = subprocess.Popen([
			"adb", "logcat",
			"-v", "tag",
			"-s", "TestResult.TestExecutionRecord"
		], executable=ADB_EXEC_PATH, stdout=subprocess.PIPE, env=adb_env)
		while True:
			line = process.stdout.readline()
			if not line:
				continue
			if logger and callable(logger):
				logger(str(line, encoding='utf-8'))

	t = threading.Thread(target=read_log, daemon=True)
	t.start()


def parse_logcat(chunk_cache, log):
	idx = log.find('TestResult.TestExecutionRecord')
	if idx == -1:
		return None

	data_str = log[idx + len('TestResult.TestExecutionRecord') + 1:]
	data_str = data_str.strip()

	data_str = chunk_cache.parse_chunk_data(data_str)
	if not data_str:
		return None

	print('data_str: ' + data_str)
	try:
		return base.base64_decode(data_str)
	except binascii.Error as e:
		print('Decode base64 data error: ' + str(e))
		return None


def get_app_version(serial, app_id):
	cur_apk_version = None

	def check_apk_version(line):
		global cur_apk_version
		reg_obj = re.search(r'versionName=(\d{8}_\d{4}_[0-9a-z]{7})', line)
		if reg_obj:
			cur_apk_version = reg_obj.groups()[0]

	exec_adb_cmd([
		'adb', 'shell', 'dumpsys', 'package', app_id
	], serial=serial, logger=check_apk_version)
	return cur_apk_version


def gen_adbShell(args):
	ADB_SHELL_PATH = '/tmp/test.sh'
	with open(ADB_SHELL_PATH, 'w') as sh:
		sh.write("#! /bin/bash\n")
		sh.write(" ".join(args))
		sh.close()


if __name__ == '__main__':
	exec_adb_cmd([
		'adb', 'devices'
	])
