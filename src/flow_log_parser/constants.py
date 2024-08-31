TAG_COUNT_FILE: str = "tag-counts.csv"
COLUMN_COUNT_FILE: str = "column-counts.csv"

HELP_MESSAGE: str = \
"""
Usage: flow-log-parser [--flow-log-file FLOW_LOG_FILE] [--lookup-table-file LOOKUP_TABLE_FILE] [--help/-h]

Parses a given VPC flow log file based on a given lookup table CSV file. 
Writes parsed flow log output to a `tag-count.csv` and `columns-count.csv` file in the current working directory.
The lookup table can use any combination of columns from the flow log file. Last column must always be `tag`.

Options:
    --flow-log-file       Path to file containing VPC flow logs.

    --lookup-table-file   Path to CSV file containing lookup table.

    --help/-h/[NO_ARGS]   Prints this help message

Example:
    flow-log-parser --flow-log-file vpc-flow.log --lookup-table-file lookup.csv
"""