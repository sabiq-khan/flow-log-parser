#!/usr/bin/env python3
from flow_log_parser.parser import FlowLogParser, FlowLogParserArgs


def main():
    args: FlowLogParserArgs = FlowLogParser.read_args()
    flow_log_parser: FlowLogParser = FlowLogParser(args)
    flow_log_parser.parse_flow_logs()


if __name__ == "__main__":
    main()
