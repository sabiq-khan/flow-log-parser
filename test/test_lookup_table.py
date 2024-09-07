from typing import Any, Dict, List
import unittest
from flow_log_parser.lookup_table import LookupTable


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