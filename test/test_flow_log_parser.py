#!/usr/bin/env python3
from typing import List
import unittest
from flow_log_parser.flow_log_parser import FlowLogParserArgs, FlowLogParser

FLOW_LOG_FILE: str = "vpc-flow.log"
LOOKUP_TABLE_FILE: str = "lookup.csv"
TAG_COUNTS_OUTPUT_FILE: str = "tag-counts.csv"
COLUMN_COUNTS_OUTPUT_FILE: str = "column-counts.csv"


class TestFlowLogParserArgs(unittest.TestCase):
    def test_argc(self):
        assert FlowLogParserArgs.argc == 4

    def test_valid_values(self):
        args: FlowLogParserArgs = FlowLogParserArgs(
            flow_log_file=FLOW_LOG_FILE,
            lookup_table_file=LOOKUP_TABLE_FILE,
            tag_counts_output_file=TAG_COUNTS_OUTPUT_FILE,
            column_counts_output_file=COLUMN_COUNTS_OUTPUT_FILE
        )

        assert args.flow_log_file == FLOW_LOG_FILE
        assert args.lookup_table_file == LOOKUP_TABLE_FILE
        assert args.tag_counts_output_file == TAG_COUNTS_OUTPUT_FILE
        assert args.column_counts_output_file == COLUMN_COUNTS_OUTPUT_FILE

    def test_invalid_flow_log_file(self):
        with self.assertRaises(TypeError):
            FlowLogParserArgs(
                flow_log_file=[FLOW_LOG_FILE],
                lookup_table_file=LOOKUP_TABLE_FILE,
                tag_counts_output_file=TAG_COUNTS_OUTPUT_FILE,
                column_counts_output_file=COLUMN_COUNTS_OUTPUT_FILE
            )

    def test_invalid_lookup_table_file(self):
        with self.assertRaises(TypeError):
            FlowLogParserArgs(
                flow_log_file=FLOW_LOG_FILE,
                lookup_table_file=[LOOKUP_TABLE_FILE],
                tag_counts_output_file=TAG_COUNTS_OUTPUT_FILE,
                column_counts_output_file=COLUMN_COUNTS_OUTPUT_FILE
            )

    def test_invalid_tag_counts_output_file(self):
        with self.assertRaises(TypeError):
            FlowLogParserArgs(
                flow_log_file=FLOW_LOG_FILE,
                lookup_table_file=LOOKUP_TABLE_FILE,
                tag_counts_output_file=[TAG_COUNTS_OUTPUT_FILE],
                column_counts_output_file=COLUMN_COUNTS_OUTPUT_FILE
            )

    def test_invalid_column_counts_output_file(self):
        with self.assertRaises(TypeError):
            FlowLogParserArgs(
                flow_log_file=FLOW_LOG_FILE,
                lookup_table_file=LOOKUP_TABLE_FILE,
                tag_counts_output_file=TAG_COUNTS_OUTPUT_FILE,
                column_counts_output_file=[COLUMN_COUNTS_OUTPUT_FILE]
            )


class TestFlowLogParser(unittest.TestCase):
    def test_read_args_valid(self):
        args: List[str] = ["--flow-log-file", FLOW_LOG_FILE, "--lookup-table-file", LOOKUP_TABLE_FILE, "--tag-counts-output-file", TAG_COUNTS_OUTPUT_FILE, "--column-counts-output-file", COLUMN_COUNTS_OUTPUT_FILE]
        
        flow_log_parser_args: FlowLogParserArgs = FlowLogParser.read_args(args)

        assert flow_log_parser_args == FlowLogParserArgs(
            flow_log_file=FLOW_LOG_FILE,
            lookup_table_file=LOOKUP_TABLE_FILE,
            tag_counts_output_file=TAG_COUNTS_OUTPUT_FILE,
            column_counts_output_file=COLUMN_COUNTS_OUTPUT_FILE
        )

    def test_read_args_invalid_values(self):
        args: List[str] = ["--file", FLOW_LOG_FILE, "--lookup", LOOKUP_TABLE_FILE, "--tag-counts", TAG_COUNTS_OUTPUT_FILE, "--column-counts", COLUMN_COUNTS_OUTPUT_FILE]

        with self.assertRaises(ValueError):
            FlowLogParser.read_args(args)

    def test_read_args_invalid_number(self):
        args: List[str] = ["--file", FLOW_LOG_FILE, "--lookup", LOOKUP_TABLE_FILE, "--tag-counts", TAG_COUNTS_OUTPUT_FILE, "--column-counts"]

        with self.assertRaises(ValueError):
            FlowLogParser.read_args(args)

    def test_init_valid_args(self):
        args: FlowLogParserArgs = FlowLogParserArgs(
            flow_log_file=FLOW_LOG_FILE,
            lookup_table_file=LOOKUP_TABLE_FILE,
            tag_counts_output_file=TAG_COUNTS_OUTPUT_FILE,
            column_counts_output_file=COLUMN_COUNTS_OUTPUT_FILE
        )

        flow_log_parser: FlowLogParser = FlowLogParser(args)

        assert flow_log_parser.flow_log_file == FLOW_LOG_FILE
        assert flow_log_parser.lookup_table_file == LOOKUP_TABLE_FILE
        assert flow_log_parser.tag_counts_output_file == TAG_COUNTS_OUTPUT_FILE
        assert flow_log_parser.column_counts_output_file == COLUMN_COUNTS_OUTPUT_FILE

    def test_init_invalid_args(self):
        with self.assertRaises(AttributeError):
            FlowLogParser("")

    def test_flow_log_file_property_readonly(self):
        args: FlowLogParserArgs = FlowLogParserArgs(
            flow_log_file=FLOW_LOG_FILE,
            lookup_table_file=LOOKUP_TABLE_FILE,
            tag_counts_output_file=TAG_COUNTS_OUTPUT_FILE,
            column_counts_output_file=COLUMN_COUNTS_OUTPUT_FILE
        )

        flow_log_parser: FlowLogParser = FlowLogParser(args)

        with self.assertRaises(AttributeError):
            flow_log_parser.flow_log_file = "new-vpc-flow.log"

    def test_lookup_table_file_property_readonly(self):
        args: FlowLogParserArgs = FlowLogParserArgs(
            flow_log_file=FLOW_LOG_FILE,
            lookup_table_file=LOOKUP_TABLE_FILE,
            tag_counts_output_file=TAG_COUNTS_OUTPUT_FILE,
            column_counts_output_file=COLUMN_COUNTS_OUTPUT_FILE
        )

        flow_log_parser: FlowLogParser = FlowLogParser(args)

        with self.assertRaises(AttributeError):
            flow_log_parser.lookup_table_file = "new-lookup.csv"

    def test_tag_counts_output_file_property_readonly(self):
        args: FlowLogParserArgs = FlowLogParserArgs(
            flow_log_file=FLOW_LOG_FILE,
            lookup_table_file=LOOKUP_TABLE_FILE,
            tag_counts_output_file=TAG_COUNTS_OUTPUT_FILE,
            column_counts_output_file=COLUMN_COUNTS_OUTPUT_FILE
        )

        flow_log_parser: FlowLogParser = FlowLogParser(args)

        with self.assertRaises(AttributeError):
            flow_log_parser.tag_counts_output_file = "new-tag-counts.csv"

    def test_column_counts_output_file_property_readonly(self):
        args: FlowLogParserArgs = FlowLogParserArgs(
            flow_log_file=FLOW_LOG_FILE,
            lookup_table_file=LOOKUP_TABLE_FILE,
            tag_counts_output_file=TAG_COUNTS_OUTPUT_FILE,
            column_counts_output_file=COLUMN_COUNTS_OUTPUT_FILE
        )

        flow_log_parser: FlowLogParser = FlowLogParser(args)

        with self.assertRaises(AttributeError):
            flow_log_parser.column_counts_output_file = "new-column-counts.csv"
        

if __name__ == "__main__":
    unittest.main()
