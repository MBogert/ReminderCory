from debug import debug_logger
from debug import debug_level
from console import console_logger

# Serves as a container class for the different loggers 

class LoggerBelt():

	def __init__(self):
		self.console = ConsoleLogger()
		self.debug = DebugLogger()

	def log_debug(message, message_level=DebugLevel.INFO):
		self.debug.log_debug(message, message_level)

	def log_console(message):
		self.console.log_console(message)

	def log_console_newline(num_lines=1):
		self.console.log_console_newline(num_lines)

	def log_console_tab(num_tabs=1):
		self.console.log_console_tab(num_tabs)