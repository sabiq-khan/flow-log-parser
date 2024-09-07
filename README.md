## flow-log-parser
This program parses a file containing VPC flow logs based on a lookup table, tags records based on the lookup table, and then writes counts of the number of records with each tag to CSV files.

The program assumes that the flow logs in the file adhere to the standard Parquet-based [VPC flow log format](https://docs.aws.amazon.com/vpc/latest/userguide/flow-log-records.html#flow-logs-fields) and contain the following columns:
```
version account-id interface-id srcaddr dstaddr srcport dstport protocol packets bytes start end action log-status
```

All of the above columns must be present, no more, no fewer. The value of the `version` column itself can be 2, 3, or 4, since these are the available VPC flow log versions.

## Requirements
If you choose to install this program with `pip` or build it from source, Python 3.10+ must be [installed](https://www.python.org/downloads/) on your system. This program does not have any dependencies outside of the [Python standard library](https://docs.python.org/3.10/library/index.html).

Alternatively, the executables on the [Releases](https://github.com/sabiq-khan/flow-log-parser/releases) page, built with [PyInstaller](https://pyinstaller.org/en/stable/), come with a copy of the Python interpreter packaged inside of them. Thus, you can simply download and run one of these executables without having to have Python installed on your system.

See the `Installation` section for further details.

## Installation
4 options for installing the program are covered in this section. You only need to pick one, and you can choose whichever is the most convenient.

### GitHub releases
This repo has a GitHub Actions pipeline that uses [PyInstaller](https://pyinstaller.org/en/stable/) to build this program into a standalone executable. The executable contains a copy of the Python interpreter, so Python does not even have to be installed on the system to run the program. Simply download an executable for your OS from the [Releases](https://github.com/sabiq-khan/flow-log-parser/releases) page and run the program.

After the executable is downloaded, you can move it from your `Downloads` directory to a directory in your `$PATH` to run it by name. You may have to run `chmod u+x` (or perform the equivalent action on your OS) to have permissions to execute the program.
```
$ ls ~/Downloads
flow-log-parser

$ mv ~/Downloads/flow-log-parser ~/bin

$ chmod u+x ~/bin/flow-log-parser

$ flow-log-parser

Usage: flow-log-parser [
                        --flow-log-file FLOW_LOG_FILE \
                        --lookup-table-file LOOKUP_TABLE_FILE \
                        --tag-counts-output-file TAG_COUNTS_OUTPUT_FILE \
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
    flow-log-parser \
    --flow-log-file vpc-flow.log \
    --lookup-table-file lookup.csv \
    --tag-counts-output-file tag-counts.csv \
    --column-counts-output-file column-counts.csv
```

Alternatively, you can use `curl` to directly download the executable to a directory of your choice.
```
$ curl -LO --output-dir ~/bin https://github.com/sabiq-khan/flow-log-parser/releases/download/v0.2.2-Linux/flow-log-parser
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100     9  100     9    0     0     19      0 --:--:-- --:--:-- --:--:--    19

$ ls ~/bin
flow-log-parser

$ chmod u+x flow-log-parser

$ flow-log-parser

Usage: flow-log-parser [
                        --flow-log-file FLOW_LOG_FILE \
                        --lookup-table-file LOOKUP_TABLE_FILE \
                        --tag-counts-output-file TAG_COUNTS_OUTPUT_FILE \
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
    flow-log-parser \
    --flow-log-file vpc-flow.log \
    --lookup-table-file lookup.csv \
    --tag-counts-output-file tag-counts.csv \
    --column-counts-output-file column-counts.csv
```
Feel free to skip to the `Usage` section.

### pip
A distribution of this program has been uploaded to http://test.pypi.org at https://test.pypi.org/project/flow-log-parser/0.2.2/.

It can be installed with `pip` as follows:
```
$ pip install -i https://test.pypi.org/simple/ flow-log-parser==0.2.2
```

No further build or configuration steps are required. Typing `flow-log-parser` into the shell will run the program.
```
$ flow-log-parser

Usage: flow-log-parser [
                        --flow-log-file FLOW_LOG_FILE \
                        --lookup-table-file LOOKUP_TABLE_FILE \
                        --tag-counts-output-file TAG_COUNTS_OUTPUT_FILE \
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
    flow-log-parser \
    --flow-log-file vpc-flow.log \
    --lookup-table-file lookup.csv \
    --tag-counts-output-file tag-counts.csv \
    --column-counts-output-file column-counts.csv
```

Feel free to skip to the `Usage` section.

### Building distribution from source
If you would like to build a distribution from source locally, follow these steps.

1. `git clone` this repo, then navigate into the `flow-log-parser/` project root directory
```
$ git clone https://github.com/sabiq-khan/flow-log-parser.git
$ cd flow-log-parser/
```

2. Run the following command to build a distribution.
```
$ python3 setup.py sdist bdist_wheel
```

The built distribution tarball and wheel will be present under the `dist/` directory. To install the wheel with `pip`, run:
```
$ pip install dist/flow_log_parser-0.2.2-py3-none-any.whl 
```

3. After this, you can run the program just by typing `flow-log-parser` into the shell.
```
$ flow-log-parser

Usage: flow-log-parser [
                        --flow-log-file FLOW_LOG_FILE \
                        --lookup-table-file LOOKUP_TABLE_FILE \
                        --tag-counts-output-file TAG_COUNTS_OUTPUT_FILE \
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
    flow-log-parser \
    --flow-log-file vpc-flow.log \
    --lookup-table-file lookup.csv \
    --tag-counts-output-file tag-counts.csv \
    --column-counts-output-file column-counts.csv
```

Feel free to skip to the `Usage` section.

### Building PyInstaller executable from source
If you would like to build the program into PyInstaller executable from source, follow these steps.

1. `git clone` this repo, then navigate into the `flow-log-parser/` project root directory
```
$ git clone https://github.com/sabiq-khan/flow-log-parser.git
$ cd flow-log-parser/
```

2. Install PyInstaller with `pip`.
```
$ pip install pyinstaller
```

3. Run the following command to build the executable.
```
$ pyinstaller --name flow-log-parser --onefile src/flow_log_parser/__main__.py
```

The built executable will be present under the `dist/` directory. It can be run by simply invoking `dist/flow-log-parser`. Alternatively, you can move it to a directory in your `$PATH` and run it by name.
```
$ mv dist/flow-log-parser ~/bin

$ flow-log-parser

Usage: flow-log-parser [
                        --flow-log-file FLOW_LOG_FILE \
                        --lookup-table-file LOOKUP_TABLE_FILE \
                        --tag-counts-output-file TAG_COUNTS_OUTPUT_FILE \
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
    flow-log-parser \
    --flow-log-file vpc-flow.log \
    --lookup-table-file lookup.csv \
    --tag-counts-output-file tag-counts.csv \
    --column-counts-output-file column-counts.csv
```

Feel free to move on to the `Usage` section.

## Usage
If the program is run with no options, or with `--help` or `-h`, it prints a help message explaining its usage.
```
$ flow-log-parser

Usage: flow-log-parser [
                        --flow-log-file FLOW_LOG_FILE \
                        --lookup-table-file LOOKUP_TABLE_FILE \
                        --tag-counts-output-file TAG_COUNTS_OUTPUT_FILE \
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
    flow-log-parser \
    --flow-log-file vpc-flow.log \
    --lookup-table-file lookup.csv \
    --tag-counts-output-file tag-counts.csv \
    --column-counts-output-file column-counts.csv
```

The program should be run with the `--flow-log-file`, `--lookup-table-file`, `--tag-counts-output-file`, and `--column-counts-output-file` options.

`--flow-log-file` should be the path to a file containing VPC flow logs following the standard Parquet-based [VPC flow log format](https://docs.aws.amazon.com/vpc/latest/userguide/flow-log-records.html#flow-logs-fields). These logs must contain the following columns, no more, no fewer:
```
version account-id interface-id srcaddr dstaddr srcport dstport protocol packets bytes start end action log-status
```

`--lookup-table-file` should be the path to a file containing a lookup table in CSV format. The columns in this lookup table can be any combination of columns present in the VPC flow log file. However, always ensure that the last column is `tag` and that its values are the tags you wish to apply to records with specific combinations of values.

The program tags records from the VPC flow log file with the tags from the lookup table, counts how many records there are with each tag, and then writes those counts to the file specified in the `--tag-counts-output-file` option. 

It also counts how many times a particular combination of columns from the lookup table was present in the VPC flow log file, and then writes those counts to the file specified in the `--column-counts-output-file` option. The counts in the column counts output file should match those in the tag counts output file since both are based on the same lookup table.

The output files whose names are specified with the `--tag-counts-output-file` and `--column-counts-output-file` options will be created in the current working directory.

## Example
Suppose I create a VPC flow log file called `vpc-flow.log` in my current working directory as follows.
```
$ cat <<-"EOF" > vpc-flow.log
2 123456789012 eni-0a1b2c3d 10.0.1.201 198.51.100.2 443 49153 6 25 20000 1620140761 1620140821 ACCEPT OK 

2 123456789012 eni-4d3c2b1a 192.168.1.100 203.0.113.101 23 49154 6 15 12000 1620140761 1620140821 REJECT OK 

2 123456789012 eni-5e6f7g8h 192.168.1.101 198.51.100.3 25 49155 6 10 8000 1620140761 1620140821 ACCEPT OK 

2 123456789012 eni-9h8g7f6e 172.16.0.100 203.0.113.102 110 49156 6 12 9000 1620140761 1620140821 ACCEPT OK 

2 123456789012 eni-7i8j9k0l 172.16.0.101 192.0.2.203 993 49157 6 8 5000 1620140761 1620140821 ACCEPT OK 

2 123456789012 eni-6m7n8o9p 10.0.2.200 198.51.100.4 143 49158 6 18 14000 1620140761 1620140821 ACCEPT OK 

2 123456789012 eni-1a2b3c4d 192.168.0.1 203.0.113.12 1024 80 6 10 5000 1620140661 1620140721 ACCEPT OK 

2 123456789012 eni-1a2b3c4d 203.0.113.12 192.168.0.1 80 1024 6 12 6000 1620140661 1620140721 ACCEPT OK 

2 123456789012 eni-1a2b3c4d 10.0.1.102 172.217.7.228 1030 443 6 8 4000 1620140661 1620140721 ACCEPT OK 

2 123456789012 eni-5f6g7h8i 10.0.2.103 52.26.198.183 56000 23 6 15 7500 1620140661 1620140721 REJECT OK 

2 123456789012 eni-9k10l11m 192.168.1.5 51.15.99.115 49321 25 6 20 10000 1620140661 1620140721 ACCEPT OK 

2 123456789012 eni-1a2b3c4d 192.168.1.6 87.250.250.242 49152 110 6 5 2500 1620140661 1620140721 ACCEPT OK 

2 123456789012 eni-2d2e2f3g 192.168.2.7 77.88.55.80 49153 993 6 7 3500 1620140661 1620140721 ACCEPT OK 

2 123456789012 eni-4h5i6j7k 172.16.0.2 192.0.2.146 49154 143 6 9 4500 1620140661 1620140721 ACCEPT OK 
EOF
```

Suppose I create a lookup table in a CSV file called `lookup.csv` in my current working directory as follows.
```
$ cat <<-"EOF" >
dstport,protocol,tag 

25,tcp,sv_P1 

68,udp,sv_P2 

23,tcp,sv_P1 

31,udp,SV_P3 

443,tcp,sv_P2 

22,tcp,sv_P4 

3389,tcp,sv_P5 

0,icmp,sv_P5 

110,tcp,email 

993,tcp,email 

143,tcp,email
EOF
```

Suppose I then run `flow-log-parser`, passing the above files as arguments and specifying the names of the output files as `tag-counts.csv` and `column-counts.csv`. The program will run, logging its actions and writing output to `tag-counts.csv` and `column-counts.csv` in the current working directory.
```
$ flow-log-parser \
    --flow-log-file vpc-flow.log \
    --lookup-table-file lookup.csv \
    --tag-counts-output-file tag-counts.csv \
    --column-counts-output-file column-counts.csv
[2024-09-07 16:27:36,364][flow_log_parser][__main__.py:13][main][INFO]: Read the following arguments: FlowLogParserArgs(flow_log_file='vpc-flow.log', lookup_table_file='lookup.csv', tag_counts_output_file='tag-counts.csv', column_counts_output_file='column-counts.csv')
[2024-09-07 16:27:36,364][flow_log_parser][flow_log_parser.py:223][parse_flow_logs][INFO]: Reading flow log records from 'vpc-flow.log'...
[2024-09-07 16:27:36,365][flow_log_parser][flow_log_parser.py:226][parse_flow_logs][INFO]: Reading CSV lookup table from 'lookup.csv'...
[2024-09-07 16:27:36,365][flow_log_parser][flow_log_parser.py:229][parse_flow_logs][INFO]: Tagging flow log records by lookup table...
[2024-09-07 16:27:36,365][flow_log_parser][flow_log_parser.py:232][parse_flow_logs][INFO]: Writing tag counts to 'tag-counts.csv'...
[2024-09-07 16:27:36,365][flow_log_parser][flow_log_parser.py:235][parse_flow_logs][INFO]: Writing column combination counts to 'column-counts.csv'...
[2024-09-07 16:27:36,365][flow_log_parser][flow_log_parser.py:238][parse_flow_logs][INFO]: Complete!

$ cat tag-counts.csv 
Tag,Count

sv_P2,1

sv_P1,2

email,3

$ cat column-counts.csv 
Dstport,Protocol,Count

25,tcp,2

68,udp,1

23,tcp,2

443,tcp,1

110,tcp,3

993,tcp,3

143,tcp,3
```

## Testing
Each of the unit tests under the `test` directory can be run individually from the shell. For example:
```
$ PYTHONPATH=src ./test/test_logger_factory.py 
..
----------------------------------------------------------------------
Ran 2 tests in 0.000s

OK
```

The unit tests under the `test` directory can be run from the shell with the following command:
```
$ PYTHONPATH=src python3 -m unittest discover -s test -p "*.py" -v
test_column_counts_output_file_property_readonly (test_flow_log_parser.TestFlowLogParser) ... ok
test_flow_log_file_property_readonly (test_flow_log_parser.TestFlowLogParser) ... ok
test_init_invalid_args (test_flow_log_parser.TestFlowLogParser) ... ok
test_init_valid_args (test_flow_log_parser.TestFlowLogParser) ... ok
test_lookup_table_file_property_readonly (test_flow_log_parser.TestFlowLogParser) ... ok
test_read_args_invalid_number (test_flow_log_parser.TestFlowLogParser) ... ok
test_read_args_invalid_values (test_flow_log_parser.TestFlowLogParser) ... ok
test_read_args_valid (test_flow_log_parser.TestFlowLogParser) ... ok
test_tag_counts_output_file_property_readonly (test_flow_log_parser.TestFlowLogParser) ... ok
test_argc (test_flow_log_parser.TestFlowLogParserArgs) ... ok
test_invalid_column_counts_output_file (test_flow_log_parser.TestFlowLogParserArgs) ... ok
test_invalid_flow_log_file (test_flow_log_parser.TestFlowLogParserArgs) ... ok
test_invalid_lookup_table_file (test_flow_log_parser.TestFlowLogParserArgs) ... ok
test_invalid_tag_counts_output_file (test_flow_log_parser.TestFlowLogParserArgs) ... ok
test_valid_values (test_flow_log_parser.TestFlowLogParserArgs) ... ok
test_invalid_values (test_flow_log_record.TestAction) ... ok
test_valid_values (test_flow_log_record.TestAction) ... ok
test_invalid_action (test_flow_log_record.TestFlowLogRecord) ... ok
test_invalid_iana_protocol (test_flow_log_record.TestFlowLogRecord) ... ok
test_invalid_log_status (test_flow_log_record.TestFlowLogRecord) ... ok
test_invalid_version (test_flow_log_record.TestFlowLogRecord) ... ok
test_valid_values (test_flow_log_record.TestFlowLogRecord) ... ok
test_invalid_values (test_flow_log_record.TestLogStatus) ... ok
test_valid_values (test_flow_log_record.TestLogStatus) ... ok
test_invalid_values (test_flow_log_record.TestVersion) ... ok
test_valid_values (test_flow_log_record.TestVersion) ... ok
test_invalid_protocol (test_iana.TestIanaProtocols) ... ok
test_valid_protocols (test_iana.TestIanaProtocols) ... ok
test_get_logger_already_exists (test_logger_factory.TestLoggerFactory) ... ok
test_get_logger_new_logger (test_logger_factory.TestLoggerFactory) ... ok
test_invalid_columns (test_lookup_table.TestLookupTable) ... ok
test_invalid_rows (test_lookup_table.TestLookupTable) ... ok
test_valid_values (test_lookup_table.TestLookupTable) ... ok

----------------------------------------------------------------------
Ran 33 tests in 0.003s

OK
```

The above commands must be run from the root directory of the project, i.e. `flow-log-parser`, in order for the unit tests to succeed.

There is also a `.vscode/settings.json` file that defines a configuration for running these tests in VS Code. Simply navigate to the [Testing](https://code.visualstudio.com/docs/editor/testing) tab in VS Code and click the play button to run the tests.
