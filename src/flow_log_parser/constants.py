HELP_MESSAGE: str = \
"""
Usage: ./main.py [--flow-log-file FLOW_LOG_FILE] [--lookup-table-file LOOKUP_TABLE_FILE] [--help/-h]

Parses a given VPC flow log file based on a given lookup table CSV file. 
Writes parsed flow log output to a `tag-count.csv` and `port-protocol-count.csv` file

Options:
	--flow_log_file       Path to file containing VPC flow logs.

	--lookup_table_file     Path to CSV file containing lookup table.

Example:
    ./main.py --flow_log_file vpc-flow.log --lookup_table_file lookup.csv
"""
