HELP_MESSAGE: str = \
"""
Usage: flow-log-parser [
                        --flow-log-file FLOW_LOG_FILE \\
                        --lookup-table-file LOOKUP_TABLE_FILE \\
                        --tag-counts-output-file TAG_COUNTS_OUTPUT_FILE \\
                        --column-counts-output-file COLUMN_COUNTS_OUTPUT_FILE
                        ]  
                        [--help/-h]

- Parses a given VPC flow log file based on a given lookup table CSV file.
- The lookup table can use any combination of columns from the flow log file.
- Last column must always be `tag`.
- The counts of how many records fit each tag are written to the specified tag counts output file in the current working directory.
- The counts of how many times a certain column combination occurred are written to the specified column counts output file in the current working directory.

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