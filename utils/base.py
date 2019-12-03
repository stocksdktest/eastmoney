import uuid
import base64
import re
from threading import Event, Lock, Thread
from time import monotonic

def generate_id(prefix):
	return prefix + '-' + str(uuid.uuid4())

def base64_encode(data):
	return bytes.decode(base64.b64encode(data))

def base64_decode(data_str):
	return base64.b64decode(data_str)

def test_base64_str(test_str):
	return re.match(r'^(?:[A-Za-z0-9+/]{4})*(?:[A-Za-z0-9+/]{2}==|[A-Za-z0-9+/]{3}=)?$', test_str)

class LogChunkCache(object):
	def __init__(self):
		# chunk_id: data_string
		self._cache = dict()

	"""
	:return str
	if chunk has finished, return concat string, else return None
	"""
	def parse_chunk_data(self, raw_str):
		chunk_match = re.search(r'Chunk\.(.+)\.(\d+):', raw_str)
		# log has only one chunk
		if not chunk_match:
			return raw_str
		chunk_data = raw_str[chunk_match.span()[1]:]
		chunk_data = chunk_data.strip()
		chunk_id, idx = chunk_match.groups()
		print('chunk_data: ' + chunk_data)
		if chunk_id in self._cache:
			self._cache[chunk_id] += chunk_data
		else:
			self._cache[chunk_id] = chunk_data

		# chunks not finished
		if int(idx) > 0:
			return None
		return self._cache.pop(chunk_id, None)

class WatchdogTimer(Thread):
	"""Run *callback* in *timeout* seconds unless the timer is restarted."""

	def __init__(self, timeout, callback, *args, timer=monotonic, **kwargs):
		super().__init__(**kwargs)
		self.timeout = timeout
		self.callback = callback
		self.args = args
		self.timer = timer
		self.cancelled = Event()
		self.blocked = Lock()

	def run(self):
		self.restart() # don't start timer until `.start()` is called
		# wait until timeout happens or the timer is canceled
		while not self.cancelled.wait(self.deadline - self.timer()):
			# don't test the timeout while something else holds the lock
			# allow the timer to be restarted while blocked
			with self.blocked:
				if self.deadline <= self.timer() and not self.cancelled.is_set():
					return self.callback(*self.args)  # on timeout

	def restart(self):
		"""Restart the watchdog timer."""
		self.deadline = self.timer() + self.timeout

	def cancel(self):
		self.cancelled.set()