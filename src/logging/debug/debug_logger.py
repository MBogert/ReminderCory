import shutil
from datetime import datetime
import os
import debug_level

class DebugLogger:

	debug_log_source_file = "logs/cory_debug.log"
	debug_log_previous_root_source = "logs/prev_session/cory_debug.log_"

	def __init__(self):
		move_old_log_file()
		self.fileWriter = initialize_log_file()

	def move_old_log_file():
		shutil.move(DebugLogger.debug_log_source_file, DebugLogger.debug_log_previous_root_source + datetime.now())

	# Should only be called AFTER move_old_log_file() has been called
	def initialize_log_file():
		if os.path.exists(DebugLogger.debug_log_source_file):
			os.remove(DebugLogger.debug_log_source_file)
		return open(DebugLogger.debug_log_source_file, "w")

	def log_line(message, level=DebugLevel.INFO):
		self.fileWriter.write(level + message + "\n")

	def close_log_file():
		self.fileWriter.close()
