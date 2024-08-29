import sys
from dataclasses import dataclass
from typing import Dict, List, ClassVar
from constants import HELP_MESSAGE


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
            value: str = raw_args.pop(0)
            args_read[option] = value

        try:
            validated_args: FlowLogParserArgs = FlowLogParserArgs(**args_read)
        except TypeError:
            raise ValueError("Invalid arguments. Run this script with '--help' to see usage.")
            
        return validated_args

    def __init__(self, args: FlowLogParserArgs):
        self.args: FlowLogParserArgs = args

    def parse_flow_logs(self):
        print(self.args)
