import logging
import sys


class LoggerWriter:
    def __init__(self, logger, level):
        self.logger = logger
        self.level = level
        self._buffer = ''

    def write(self, message):
        message = message.rstrip()
        if message:
            self.logger.log(self.level, message)

    def flush(self):
        pass
