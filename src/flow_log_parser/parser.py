import sys
from dataclasses import dataclass
from typing import Dict, List, ClassVar, Any
from constants import HELP_MESSAGE
from record import FlowLogRecord


@dataclass
class LookupTable:
    columns: List[str]
    rows: List[Dict[str, Any]]


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
            raise ValueError(
                "Invalid number of arguments. "
                "Run this script with '--help' to see usage."
            )

        while len(raw_args) > 0:
            option: str = raw_args.pop(0).lstrip("--")
            key: str = option.replace("-", "_")
            value: str = raw_args.pop(0)
            args_read[key] = value

        try:
            validated_args: FlowLogParserArgs = FlowLogParserArgs(**args_read)
        except TypeError:
            raise ValueError(
                "Invalid arguments. "
                "Run this script with '--help' to see usage."
            )
            
        return validated_args

    def __init__(self, args: FlowLogParserArgs):
        self.args: FlowLogParserArgs = args
        self.tagged_records: Dict[str, FlowLogRecord] = {}

    def _read_flow_log_file(self, flow_log_file: str) -> List[FlowLogRecord]:
        flow_log_records: List[FlowLogRecord] = []

        with open(file=flow_log_file, mode="r") as file:
            for line in file:
                stripped_line = line.strip()
                if stripped_line == "":
                    continue
                columns: List[str] = stripped_line.split(" ")
                
                try:
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
                except (IndexError, ValueError, TypeError):
                    raise ValueError(
                        "Invalid flow log format. "
                        "Expected 'version account-id interface-id srcaddr dstaddr srcport dstport protocol packets bytes start end action log-status'. "
                        "For reference, see: https://docs.aws.amazon.com/vpc/latest/userguide/flow-log-records.html#flow-logs-fields"
                    )
        
                flow_log_records.append(flow_log_record)

        return flow_log_records
    
    def _read_lookup_table_file(self, lookup_table_file: str) -> LookupTable:
        """
        Greater control over CSV parsing than csv.DictReader
        """
        columns: List[str] = []
        rows: List[Dict[str, str]] = []
        with open(file=lookup_table_file, mode="r") as file:
            columns: List[str] = file.readline().strip().split(",")
            for line in file:
                row: Dict[str, str] = {}
                stripped_line: str = line.strip()
                if stripped_line == "":
                    continue
                split_line: List[str] = stripped_line.strip().split(",")
                for key, value in zip(columns, split_line):
                    row[key] = value
                rows.append(row)

        lookup_table: LookupTable = LookupTable(
            columns=columns,
            rows=rows
        )

        return lookup_table


    # TODO: Fix tagging / iterating logic
    def _tag_records(self, flow_log_records: List[FlowLogRecord], lookup_table: LookupTable) -> Dict[str, List[FlowLogRecord]]:
        tagged_records: Dict[str, List[FlowLogRecord]] = {}
        for flow_log_record in flow_log_records:
            is_match: bool = True
            for row in lookup_table.rows:
                for column in lookup_table.columns[:-1]:
                    if str(getattr(flow_log_record, column)) != row[column]:
                        is_match = False
            
                if is_match:
                    if row["tag"] in tagged_records.keys():
                        tagged_records[row["tag"]].append(flow_log_record)
                    else:
                        tagged_records[row["tag"]] = [flow_log_record]

        return tagged_records

    def parse_flow_logs(self):
        flow_log_file: str = self.args.flow_log_file
        lookup_table_file: str = self.args.lookup_table_file

        flow_log_records: List[FlowLogRecord] = self._read_flow_log_file(flow_log_file)
        print(flow_log_records)
        print(lookup_table_file)
        lookup_table: LookupTable = self._read_lookup_table_file(lookup_table_file)
        print(lookup_table)

        tagged_records: Dict[str, List[FlowLogRecord]] = self._tag_records(flow_log_records, lookup_table)
        print(tagged_records)
