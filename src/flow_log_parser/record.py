from enum import Enum
from dataclasses import dataclass, fields
from typing import Any, get_args
from flow_log_parser.iana import IANA_PROTOCOLS, IanaProtocol


class Version(int, Enum):
    _2 = 2
    _3 = 3
    _4 = 4


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
    Represents a VPC flow log record
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
    def protocol(self) -> IanaProtocol:
        try:
            protocol: IanaProtocol = IANA_PROTOCOLS[self.protocol_number]
            return protocol
        except IndexError:
            raise ValueError(f"'{self.protocol_number}' is not a valid IANA protocol number.")
    
    def __post_init__(self):
        for field in fields(self):
            field_value: Any = getattr(self, field.name)
            if not isinstance(field.type(field_value), field.type):
                field_type: str = field.type.__name__
                raise ValueError(f"'{field_value}' is not a valid {field_type}.")
        
        if (self.protocol_number < 0) or (self.protocol_number >= len(IANA_PROTOCOLS)):
            raise ValueError(f"'{self.protocol_number}' is not a valid IANA protocol number.")

        if not self.protocol in get_args(IanaProtocol):
            raise ValueError(f"'{self.protocol}' is not a valid IanaProtocol.")
