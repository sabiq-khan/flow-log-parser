import sys
from dataclasses import dataclass
from typing import Dict, List, ClassVar
from constants import HELP_MESSAGE
from flow_log import FlowLog


@dataclass
class FlowLogParserArgs:
    flow_log_file: str
    lookup_table_file: str

    argc: ClassVar[int] = 2


class FlowLogParser:
    @staticmethod
    def read_args() -> FlowLogParserArgs:
        raw_args: List[str] = sys.argv[1:]
        args_read: Dict[str, str] = {}

        if (len(raw_args) == 0) or (("--help" in raw_args) or ("-h" in raw_args)):
            print(HELP_MESSAGE)
            sys.exit(0)
        elif (len(raw_args) != 2*(FlowLogParserArgs.argc)):
            raise ValueError("Invalid number of arguments. Run this script with '--help' to see usage.")

        while len(raw_args) > 0:
            option: str = raw_args.pop(0).lstrip("--")
            key: str = option.replace("-", "_")
            value: str = raw_args.pop(0)
            args_read[key] = value

        try:
            validated_args: FlowLogParserArgs = FlowLogParserArgs(**args_read)
        except TypeError:
            raise ValueError("Invalid arguments. Run this script with '--help' to see usage.")
            
        return validated_args

    def __init__(self, args: FlowLogParserArgs):
        self.args: FlowLogParserArgs = args

    def _read_flow_log_file(self, flow_log_file: str) -> List[FlowLog]:
        flow_logs: List[FlowLog] = []

        with open(file=flow_log_file, mode="r") as file:
            for line in file:
                line = line.strip()
                if line == "":
                    continue
                columns: List[str] = line.split(" ")
                
                try:
                    flow_log: FlowLog = FlowLog(
                        version=int(columns[0]),
                        account_id=columns[1],
                        interface_id=columns[2],
                        src_addr=columns[3],
                        dst_addr=columns[4],
                        src_port=int(columns[5]),
                        dst_port=int(columns[6]),
                        protocol=int(columns[7]),
                        packets=int(columns[8]),
                        bytes=int(columns[9]),
                        start=int(columns[10]),
                        end=int(columns[11]),
                        action=columns[12],
                        log_status=columns[13]
                    )
                except (IndexError, TypeError) as e:
                    raise ValueError("Invalid flow log format.\nExpected 'version account-id interface-id srcaddr dstaddr srcport dstport protocol packets bytes start end action log-status'.")
        
                flow_logs.append(flow_log)

        return flow_logs

    def parse_flow_logs(self):
        flow_log_file: str = self.args.flow_log_file
        lookup_table_file: str = self.args.lookup_table_file

        flow_logs: List[FlowLog] = self._read_flow_log_file(flow_log_file)
        print(flow_logs)
        print(lookup_table_file)
