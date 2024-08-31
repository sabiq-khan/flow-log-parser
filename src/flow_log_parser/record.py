from enum import Enum
from dataclasses import dataclass
from flow_log_parser.constants import IANA_PROTOCOLS


class Version(int, Enum):
    _2: 2
    _3: 3
    _4: 4


class Action(str, Enum):
    ACCEPT = "ACCEPT"
    REJECT = "REJECT"


class LogStatus(str, Enum):
    OK = "OK"
    NODATA = "NODATA"
    SKIPDATA = "SKIPDATA"


@dataclass
class FlowLogRecord:
    """
    For reference, see: https://docs.aws.amazon.com/vpc/latest/userguide/flow-log-records.html#flow-logs-fields
    """
    version: Version
    account_id: str
    interface_id: str
    srcaddr: str
    dstaddr: str
    srcport: int
    dstport: int
    protocol_number: int
    packets: int
    bytes: int
    start: int
    end: int
    action: Action
    log_status: LogStatus


    @property
    def protocol(self):
        return IANA_PROTOCOLS[self.protocol_number]
