from pathlib import Path
from random import randint

import os
import sys

class Logger:

log_src="logs/cory_file.log"

	def __init__(self):
		self.log_file = open_file()

	def open_file():
		if Path(Logger.log_src).is_file():
			rename_previous_log()
		# TODO leave where I left off

	def rename_previous_log():
		os.rename(log_src, log_src + randint(1, sys.maxsize))

