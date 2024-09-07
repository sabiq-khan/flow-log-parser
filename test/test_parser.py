#!/usr/bin/env python3
from typing import Any, Dict, List, get_args
import unittest
from flow_log_parser.parser import LookupTable, FlowLogParserArgs, FlowLogParser

FLOW_LOG_FILE: str = "vpc-flow.log"
LOOKUP_TABLE_FILE: str = "lookup.csv"


class TestLookupTable(unittest.TestCase):
    def test_valid_values(self):
        columns: List[str] = ["dstport", "protocol", "tag"]
        rows: List[Dict[str, Any]] = [
            {"dstport": "25", "protocol": "tcp", "tag": "sv_P1"}, 
            {"dstport": "68", "protocol": "udp", "tag": "sv_P2"}, 
            {"dstport": "23", "protocol": "tcp", "tag": "sv_P1"}
        ]

        lookup_table: LookupTable = LookupTable(
            columns=columns,
            rows=rows
        )

        assert lookup_table.columns == columns
        assert lookup_table.rows == rows

    def test_invalid_columns(self):
        columns: str = "dstport protocol tag"
        rows: List[Dict[str, Any]] = [
            {"dstport": "25", "protocol": "tcp", "tag": "sv_P1"}, 
            {"dstport": "68", "protocol": "udp", "tag": "sv_P2"}, 
            {"dstport": "23", "protocol": "tcp", "tag": "sv_P1"}
        ]

        with self.assertRaises(TypeError):
            LookupTable(
                columns=columns,
                rows=rows
            )
    
    def test_invalid_rows(self):
        columns: List[str] = ["dstport", "protocol", "tag"]
        rows: str = "25 tcp sv_P1"

        with self.assertRaises(TypeError):
            LookupTable(
                columns=columns,
                rows=rows
            )


class TestFlowLogParserArgs(unittest.TestCase):
    def test_argc(self):
        assert FlowLogParserArgs.argc == 2

    def test_valid_values(self):
        args: FlowLogParserArgs = FlowLogParserArgs(
            flow_log_file=FLOW_LOG_FILE,
            lookup_table_file=LOOKUP_TABLE_FILE
        )

        assert args.flow_log_file == FLOW_LOG_FILE
        assert args.lookup_table_file == LOOKUP_TABLE_FILE

    def test_invalid_flow_log_file(self):
        with self.assertRaises(TypeError):
            FlowLogParserArgs(
                flow_log_file=[FLOW_LOG_FILE],
                lookup_table_file=LOOKUP_TABLE_FILE
            )

    def test_invalid_lookup_table_file(self):
        with self.assertRaises(TypeError):
            FlowLogParserArgs(
                flow_log_file=FLOW_LOG_FILE,
                lookup_table_file=[LOOKUP_TABLE_FILE]
            )


class TestFlowLogParser(unittest.TestCase):
    def test_read_args_valid(self):
        args: List[str] = ["--flow-log-file", FLOW_LOG_FILE, "--lookup-table-file", LOOKUP_TABLE_FILE]
        
        flow_log_parser_args: FlowLogParserArgs = FlowLogParser.read_args(args)

        assert flow_log_parser_args == FlowLogParserArgs(
            flow_log_file=FLOW_LOG_FILE,
            lookup_table_file=LOOKUP_TABLE_FILE
        )

    def test_read_args_invalid_values(self):
        args: List[str] = ["--file", FLOW_LOG_FILE, "--lookup", LOOKUP_TABLE_FILE]

        with self.assertRaises(ValueError):
            FlowLogParser.read_args(args)

    def test_read_args_invalid_number(self):
        flow_log_file: str = "vpc-flow.log"
        args: List[str] = ["--file", flow_log_file, "--lookup"]

        with self.assertRaises(ValueError):
            FlowLogParser.read_args(args)

    def test_init_valid_args(self):
        args: FlowLogParserArgs = FlowLogParserArgs(
            flow_log_file=FLOW_LOG_FILE,
            lookup_table_file=LOOKUP_TABLE_FILE
        )

        flow_log_parser: FlowLogParser = FlowLogParser(args)

        assert flow_log_parser.flow_log_file == FLOW_LOG_FILE
        assert flow_log_parser.lookup_table_file == LOOKUP_TABLE_FILE

    def test_init_invalid_args(self):
        with self.assertRaises(AttributeError):
            FlowLogParser("")

    def test_flow_log_file_property_readonly(self):
        args: FlowLogParserArgs = FlowLogParserArgs(
            flow_log_file=FLOW_LOG_FILE,
            lookup_table_file=LOOKUP_TABLE_FILE
        )

        flow_log_parser: FlowLogParser = FlowLogParser(args)

        with self.assertRaises(AttributeError):
            flow_log_parser.flow_log_file = "new-vpc-flow.log"

    def test_lookup_table_file_property_readonly(self):
        args: FlowLogParserArgs = FlowLogParserArgs(
            flow_log_file=FLOW_LOG_FILE,
            lookup_table_file=LOOKUP_TABLE_FILE
        )

        flow_log_parser: FlowLogParser = FlowLogParser(args)

        with self.assertRaises(AttributeError):
            flow_log_parser.lookup_table_file = "new-lookup.csv"
        

if __name__ == "__main__":
    unittest.main()
