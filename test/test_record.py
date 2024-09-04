#!/usr/bin/env python3
import copy
from typing import List
import unittest
from flow_log_parser.record import Version, Action, LogStatus, FlowLogRecord

TEST_RECORD_VALUES: List[str] = ["2", "123456789012", "eni-0a1b2c3d", "10.0.1.201", "198.51.100.2", "443", "49153", "6", "25", "20000", "1620140761", "1620140821", "ACCEPT", "OK"]


class TestVersion(unittest.TestCase):
    def test_valid_values(self):
        assert 2 == Version._2
        assert 3 == Version._3
        assert 4 == Version._4

        assert 2 == Version(2)
        assert 3 == Version(3)
        assert 4 == Version(4)

        assert Version(2) == Version._2
        assert Version(3) == Version._3
        assert Version(4) == Version._4
    
    def test_invalid_values(self):
        with self.assertRaises(ValueError):
            Version(5)
        
        with self.assertRaises(ValueError):
            Version("2")

        with self.assertRaises(ValueError):
            Version(int)


class TestAction(unittest.TestCase):
    def test_valid_values(self):
        assert "ACCEPT" == Action.ACCEPT
        assert "REJECT" == Action.REJECT

        assert "ACCEPT" == Action("ACCEPT")
        assert "REJECT" == Action("REJECT")

        assert Action("ACCEPT") == Action.ACCEPT
        assert Action("REJECT") == Action.REJECT

    def test_invalid_values(self):
        with self.assertRaises(ValueError):
            Action("accept")
        
        with self.assertRaises(ValueError):
            Action("reject")

        with self.assertRaises(ValueError):
            Action("XCCEPT")
        
        with self.assertRaises(ValueError):
            Action(str)


class TestLogStatus(unittest.TestCase):
    def test_valid_values(self):
        assert "OK" == LogStatus.OK
        assert "SKIPDATA" == LogStatus.SKIPDATA
        assert "NODATA" == LogStatus.NODATA

        assert "OK" == LogStatus("OK")
        assert "SKIPDATA" == LogStatus("SKIPDATA")
        assert "NODATA" == LogStatus("NODATA")

        assert LogStatus("OK") == LogStatus.OK
        assert LogStatus("SKIPDATA") == LogStatus.SKIPDATA
        assert LogStatus("NODATA") == LogStatus.NODATA

    def test_invalid_values(self):
        with self.assertRaises(ValueError):
            LogStatus("ok")
        
        with self.assertRaises(ValueError):
            LogStatus("skipdata")

        with self.assertRaises(ValueError):
            LogStatus("nodata")

        with self.assertRaises(ValueError):
            LogStatus("XK")

        with self.assertRaises(ValueError):
            LogStatus(str)


class TestFlowLogRecord(unittest.TestCase):
    def test_valid_values(self):
        columns: List[str] = copy.deepcopy(TEST_RECORD_VALUES)

        flow_log_record: FlowLogRecord = FlowLogRecord(
            version=int(columns[0]),
            account_id=columns[1],
            interface_id=columns[2],
            srcaddr=columns[3],
            dstaddr=columns[4],
            srcport=int(columns[5]),
            dstport=int(columns[6]),
            protocol_number=int(columns[7]),
            packets=int(columns[8]),
            bytes=int(columns[9]),
            start=int(columns[10]),
            end=int(columns[11]),
            action=columns[12],
            log_status=columns[13]
        )

        assert Version(flow_log_record.version) == 2
        assert flow_log_record.account_id == "123456789012"
        assert flow_log_record.interface_id == "eni-0a1b2c3d"
        assert flow_log_record.srcaddr == "10.0.1.201"
        assert flow_log_record.dstaddr == "198.51.100.2"
        assert flow_log_record.srcport == 443
        assert flow_log_record.dstport == 49153
        assert flow_log_record.protocol_number == 6
        assert flow_log_record.protocol == "tcp"
        assert flow_log_record.packets == 25
        assert flow_log_record.bytes == 20000
        assert flow_log_record.start == 1620140761
        assert flow_log_record.end == 1620140821
        assert Action(flow_log_record.action) == "ACCEPT"
        assert LogStatus(flow_log_record.log_status) == "OK"

    def test_invalid_iana_protocol(self):
        columns: List[str] = copy.deepcopy(TEST_RECORD_VALUES)
        columns[7] = "-1"

        with self.assertRaises(ValueError):
            FlowLogRecord(
                version=int(columns[0]),
                account_id=columns[1],
                interface_id=columns[2],
                srcaddr=columns[3],
                dstaddr=columns[4],
                srcport=int(columns[5]),
                dstport=int(columns[6]),
                protocol_number=int(columns[7]),
                packets=int(columns[8]),
                bytes=int(columns[9]),
                start=int(columns[10]),
                end=int(columns[11]),
                action=columns[12],
                log_status=columns[13]
            )

    def test_invalid_version(self):
        columns: List[str] = copy.deepcopy(TEST_RECORD_VALUES)
        columns[0] = "5"

        with self.assertRaises(ValueError):
            FlowLogRecord(
                version=int(columns[0]),
                account_id=columns[1],
                interface_id=columns[2],
                srcaddr=columns[3],
                dstaddr=columns[4],
                srcport=int(columns[5]),
                dstport=int(columns[6]),
                protocol_number=int(columns[7]),
                packets=int(columns[8]),
                bytes=int(columns[9]),
                start=int(columns[10]),
                end=int(columns[11]),
                action=columns[12],
                log_status=columns[13]
            )

    def test_invalid_action(self):
        columns: List[str] = copy.deepcopy(TEST_RECORD_VALUES)
        columns[12] = "EXCEPT"

        with self.assertRaises(ValueError):
            FlowLogRecord(
                version=int(columns[0]),
                account_id=columns[1],
                interface_id=columns[2],
                srcaddr=columns[3],
                dstaddr=columns[4],
                srcport=int(columns[5]),
                dstport=int(columns[6]),
                protocol_number=int(columns[7]),
                packets=int(columns[8]),
                bytes=int(columns[9]),
                start=int(columns[10]),
                end=int(columns[11]),
                action=columns[12],
                log_status=columns[13]
            )

    def test_invalid_log_status(self):
        columns: List[str] = copy.deepcopy(TEST_RECORD_VALUES)
        columns[13] = "OKAY"

        with self.assertRaises(ValueError):
            FlowLogRecord(
                version=int(columns[0]),
                account_id=columns[1],
                interface_id=columns[2],
                srcaddr=columns[3],
                dstaddr=columns[4],
                srcport=int(columns[5]),
                dstport=int(columns[6]),
                protocol_number=int(columns[7]),
                packets=int(columns[8]),
                bytes=int(columns[9]),
                start=int(columns[10]),
                end=int(columns[11]),
                action=columns[12],
                log_status=columns[13]
            )


if __name__ == "__main__":
    unittest.main()
