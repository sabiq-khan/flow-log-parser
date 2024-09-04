#!/usr/bin/env python3
from typing import get_args
import unittest
from flow_log_parser.iana import IANA_PROTOCOLS, IanaProtocol


class TestIanaProtocols(unittest.TestCase):
    def test_valid_protocols(self):
        for protocol in IANA_PROTOCOLS:
            assert protocol in get_args(IanaProtocol)

    def test_invalid_protocol(self):
        invalid_protocol: str = "TransmissionControlProtocol"
        assert invalid_protocol not in IANA_PROTOCOLS
        assert invalid_protocol not in get_args(IanaProtocol)


if __name__ == "__main__":
    unittest.main()
