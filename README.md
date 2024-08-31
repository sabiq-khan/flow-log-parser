## flow-log-parser
This program parses a file containing VPC flow logs based on a lookup table, tags records based on the lookup table, and then writes counts of the number of records with each tag to CSV files.

## Requirements
This program just requires that Python 3.10+ is [installed](https://www.python.org/downloads/) on the system. No dependencies outside of the [Python standard library](https://docs.python.org/3.10/library/index.html) are used.

## Installation
### pip
A distribution of this program has been uploaded to http://test.pypi.org at https://test.pypi.org/project/flow-log-parser/0.1.0/.

It can be installed with `pip` as follows:
```
$ pip install -i https://test.pypi.org/simple/ flow-log-parser==0.1.0
```

No further build or configuration steps are required. Typing `flow-log-parser` into the shell will run the program.
```
$ flow-log-parser

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
$ pip install dist/flow_log_parser-0.1.0-py3-none-any.whl 
```

3. After this, you can run the program just by typing `flow-log-parser` into the shell.
```
$ flow-log-parser

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
```

Feel free to move on to the `Usage` section.

## Usage
If the program is run with no options, or with `--help` or `-h`, it prints a help message explaining its usage.
```
$ flow-log-parser

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
```

The program should be run with the `--flow-log-file` and `--lookup-table-file` options.

`--flow-log-file` should be the path to a file containing VPC flow logs following the standard Parquet-based [VPC flow log format](https://docs.aws.amazon.com/vpc/latest/userguide/flow-log-records.html#flow-logs-fields).
`--lookup-table-file` should be the path to a file containing a lookup table in CSV format. The columns in this lookup table can be any combination of columns present in the VPC flow log file. However, always ensure that the last column is `tag` and its values are the tags you wish to records with specific combinations of values.

The program outputs 2 files in its current working directory. One is a `tag-counts.csv` file containing the number of records from the VPC flow log file were tagged with a specific tag. The other is a `column-counts.csv` file showing how many times a particular combination of columns was present in the VPC flow log file; these counts should match the ones in `tag-counts.csv`. 

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

When I run `flow-log-parser` with the options pointing to these files, I get a `tag-counts.csv` and `column-counts.csv` file in my current working directory as follows.
```
$ flow-log-parser --flow-log-file vpc-flow.log --lookup-table-file lookup.csv 

$ cat tag-counts.csv 
Tag,Count

sv_P2,1

sv_P1,2

email,3

$ cat column-counts.csv 
Dstport,Protocol,Tag

25,tcp,2

68,udp,1

23,tcp,2

443,tcp,1

110,tcp,3

993,tcp,3

143,tcp,3
```
