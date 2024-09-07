#!/usr/bin/env python3
import unittest
import sys
from logging import Formatter, Logger, INFO, StreamHandler
from flow_log_parser.logger_factory import LoggerFactory

LOGGER_NAME: str = "test_logger"


class TestLoggerFactory(unittest.TestCase):
    def test_get_logger_new_logger(self):
        logger: Logger = LoggerFactory.get_logger(LOGGER_NAME)

        assert logger.level == INFO
        assert len(logger.handlers) == 1
        assert isinstance(logger.handlers[0], StreamHandler)
        assert logger.handlers[0].stream == sys.stdout
        assert isinstance(logger.handlers[0].formatter, Formatter)

    def test_get_logger_already_exists(self):
        logger_1: Logger = LoggerFactory.get_logger(LOGGER_NAME)
        logger_2: Logger = LoggerFactory.get_logger(LOGGER_NAME)

        assert logger_2 is logger_1


if __name__ == "__main__":
    unittest.main()
