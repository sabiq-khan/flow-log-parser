#!/usr/bin/env python3
from logging import Logger
import sys
from flow_log_parser.constants import LOGGER_NAME
from flow_log_parser.logger_factory import LoggerFactory
from flow_log_parser.flow_log_parser import FlowLogParser, FlowLogParserArgs


def main():
    try:
        logger: Logger = LoggerFactory.get_logger(LOGGER_NAME)
        args: FlowLogParserArgs = FlowLogParser.read_args(sys.argv[1:])
        logger.info(f"Read the following arguments: {args}")

        flow_log_parser: FlowLogParser = FlowLogParser(args)
        flow_log_parser.parse_flow_logs()
 
    except Exception as e:
        logger.error(e)
        raise e


if __name__ == "__main__":
    main()
