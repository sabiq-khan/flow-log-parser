from enum import Enum
from dataclasses import dataclass

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
class FlowLog:
    """
    For reference: https://docs.aws.amazon.com/vpc/latest/userguide/flow-log-records.html#flow-logs-fields
    """
    version: Version
    account_id: str
    interface_id: str
    src_addr: str
    dst_addr: str
    src_port: int
    dst_port: int
    protocol: int
    packets: int
    bytes: int
    start: int
    end: int
    action: Action
    log_status: LogStatus