#!/usr/bin/env python3
from typing import Any, Dict, List, get_args
import unittest
from flow_log_parser.parser import LookupTable, FlowLogParserArgs


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
    def test_valid_values(self):
        flow_log_file: str = "vpc-flow.log"
        lookup_table_file: str = "lookup.csv"

        args: FlowLogParserArgs = FlowLogParserArgs(
            flow_log_file=flow_log_file,
            lookup_table_file=lookup_table_file
        )

        assert args.flow_log_file == flow_log_file
        assert args.lookup_table_file == lookup_table_file

    def test_invalid_flow_log_file(self):
        flow_log_file: str = ["vpc-flow.log"]
        lookup_table_file: str = "lookup.csv"

        with self.assertRaises(TypeError):
            FlowLogParserArgs(
                flow_log_file=flow_log_file,
                lookup_table_file=lookup_table_file
            )

    def test_invalid_lookup_table_file(self):
        flow_log_file: str = "vpc-flow.log"
        lookup_table_file: str = ["lookup.csv"]

        with self.assertRaises(TypeError):
            FlowLogParserArgs(
                flow_log_file=flow_log_file,
                lookup_table_file=lookup_table_file
            )


if __name__ == "__main__":
    unittest.main()
