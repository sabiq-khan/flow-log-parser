from logging import Logger
import sys
from dataclasses import dataclass, fields
from typing import Dict, List, ClassVar, Any
from flow_log_parser.constants import HELP_MESSAGE
from flow_log_parser.logger_factory import LoggerFactory
from flow_log_parser.flow_log_record import FlowLogRecord
from flow_log_parser.lookup_table import LookupTable


@dataclass
class FlowLogParserArgs:
    """
    Represents arguments passed to FlowLogParser
    """
    flow_log_file: str
    lookup_table_file: str
    tag_counts_output_file: str
    column_counts_output_file: str


    argc: ClassVar[int] = 4

    def __post_init__(self):
        for field in fields(self):
            field_value: Any = getattr(self, field.name)
            if not isinstance(field_value, str):
                raise TypeError(f"Invalid argument: {field_value}. Expected string.")


class FlowLogParser:
    @staticmethod
    def read_args(args: List[str]) -> FlowLogParserArgs:
        """
        Reads command line arguments into a FlowLogParserArgs object
        """
        raw_args: List[str] = args
        args_read: Dict[str, str] = {}

        if (len(raw_args) == 0) or (("--help" in raw_args) or ("-h" in raw_args)):
            print(HELP_MESSAGE)
            sys.exit(0)
        elif (len(raw_args) == 1) and (raw_args[0] != "--help") and (raw_args[0] != "-h"):
            raise ValueError(
                "Invalid arguments. "
                "Run this script with '--help' to see usage."
            )
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
        self.logger: Logger = LoggerFactory.get_logger("flow_log_parser")
        self._flow_log_file: str = args.flow_log_file
        self._lookup_table_file: str = args.lookup_table_file
        self._tag_counts_output_file: str = args.tag_counts_output_file
        self._column_counts_output_file: str = args.column_counts_output_file

    @property
    def flow_log_file(self) -> str:
        return self._flow_log_file
    
    @property
    def lookup_table_file(self) -> str:
        return self._lookup_table_file
    
    @property
    def tag_counts_output_file(self) -> str:
        return self._tag_counts_output_file

    @property
    def column_counts_output_file(self) -> str:
        return self._column_counts_output_file

    def _read_flow_log_file(self, flow_log_file: str) -> List[FlowLogRecord]:
        """
        Reads records from flow log file into a list of FlowLogRecord objects
        """
        flow_log_records: List[FlowLogRecord] = []

        with open(file=flow_log_file, mode="r") as file:
            for line in file:
                stripped_line: str = line.strip()
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
        Reads lookup table file into a LookupTable object
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

    def _tag_records(self, flow_log_records: List[FlowLogRecord], lookup_table: LookupTable) -> Dict[str, List[FlowLogRecord]]:
        """
        Groups flow log records based on which tag from lookup table they match
        """
        tagged_records: Dict[str, List[FlowLogRecord]] = {}
        for flow_log_record in flow_log_records:
            for row in lookup_table.rows:
                is_match: bool = True
                for column in lookup_table.columns[:-1]:
                    if str(getattr(flow_log_record, column)) != row[column]:
                        is_match = False
            
                if is_match:
                    tag: str = row["tag"]
                    if tag in tagged_records.keys():
                        tagged_records[tag].append(flow_log_record)
                    else:
                        tagged_records[tag] = [flow_log_record]

        return tagged_records
    
    def _write_tag_counts_to_csv(self, tagged_records: Dict[str, List[FlowLogRecord]], tag_count_output_file: str):
        """
        Writes counts of how many times records matching each tag occured in flow log file
        Greater control over CSV output than csv.DictWriter
        """
        with open(file=tag_count_output_file, mode="w") as file:
            file.write("Tag,Count\n")
            for tag, records in tagged_records.items():
                file.write("\n")
                count: int = len(records)
                file.write(f"{tag},{count}\n")

    def _write_column_counts_to_csv(self, lookup_table: LookupTable, tagged_records: Dict[str, List[FlowLogRecord]], column_count_output_file: str):
        """
        Writes counts of how many times each column combo from lookup table occurred in flow log file
        Greater control over CSV output than csv.DictWriter
        """
        with open(file=column_count_output_file, mode="w") as file:
            columns: List[str] = [column.title() for column in lookup_table.columns]
            # Replacing `Tag` column heading with `Count`
            columns.pop(-1)
            columns.append("Count")
            file.write(f"{','.join(columns)}\n")
            for row in lookup_table.rows:
                tag: str = row["tag"]
                if tag not in tagged_records.keys():
                    continue
                count: int = len(tagged_records[tag])
                values: List[str] = []
                for value in row.values():
                    values.append(value)
                # Replacing the actual tag with its count
                values.pop(-1)
                values.append(str(count))
                file.write("\n")
                file.write(f"{','.join(values)}\n")

    def parse_flow_logs(self):
        """
        Parses a flow log file based on a lookup table file
        Writes results to a `tag-counts.csv` and `column-counts.csv` file
        """
        self.logger.info(f"Reading flow log records from '{self.flow_log_file}'...")
        flow_log_records: List[FlowLogRecord] = self._read_flow_log_file(self.flow_log_file)

        self.logger.info(f"Reading CSV lookup table from '{self.lookup_table_file}'...")
        lookup_table: LookupTable = self._read_lookup_table_file(self.lookup_table_file)

        self.logger.info("Tagging flow log records by lookup table...")
        tagged_records: Dict[str, List[FlowLogRecord]] = self._tag_records(flow_log_records, lookup_table)

        self.logger.info(f"Writing tag counts to '{self.tag_counts_output_file}'...")
        self._write_tag_counts_to_csv(tagged_records, self.tag_counts_output_file)

        self.logger.info(f"Writing column combination counts to '{self.column_counts_output_file}'...")
        self._write_column_counts_to_csv(lookup_table, tagged_records, self.column_counts_output_file)

        self.logger.info("Complete!")
