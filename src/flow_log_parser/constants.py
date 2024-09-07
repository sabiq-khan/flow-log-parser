LOGGER_NAME: str = "flow_log_parser"

HELP_MESSAGE: str = \
"""
Usage: flow-log-parser [
                        --flow-log-file FLOW_LOG_FILE \\
                        --lookup-table-file LOOKUP_TABLE_FILE \\
                        --tag-counts-output-file TAG_COUNTS_OUTPUT_FILE \\
                        --column-counts-output-file COLUMN_COUNTS_OUTPUT_FILE
                        ]  
                        [--help/-h]

- Parses a given VPC flow log file based on a given lookup table CSV file, mapping combinations of flow log column values to certain tags.
- The counts of how many records were tagged with each tag are recorded.
- The counts of how many records matched a combination of column values from the lookup table are also recorded.
- These counts are written to the specified output files, in the current working directory.
- For further information on usage, see: https://github.com/sabiq-khan/flow-log-parser?tab=readme-ov-file#usage

Options:
    --flow-log-file                 Path to file containing VPC flow logs.

    --lookup-table-file             Path to CSV file containing lookup table.

    --tag-counts-output-file        File name for tag counts output.

    --column-counts-output-file     File name for column counts output.

    --help/-h/[NO_ARGS]             Prints this help message

Example:
    flow-log-parser \\
    --flow-log-file vpc-flow.log \\
    --lookup-table-file lookup.csv \\
    --tag-counts-output-file tag-counts.csv \\
    --column-counts-output-file column-counts.csv
"""