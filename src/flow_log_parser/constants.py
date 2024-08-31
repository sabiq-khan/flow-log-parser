from typing import Literal, Tuple


HELP_MESSAGE: str = \
"""
Usage: ./main.py [--flow-log-file FLOW_LOG_FILE] [--lookup-table-file LOOKUP_TABLE_FILE] [--help/-h]

Parses a given VPC flow log file based on a given lookup table CSV file. 
Writes parsed flow log output to a `tag-count.csv` and `columns-count.csv` file in the current working directory.
The lookup table can use any combination of columns from the flow log file. Last column must always be `tag`.

Options:
	--flow_log_file       Path to file containing VPC flow logs.

	--lookup_table_file   Path to CSV file containing lookup table.

Example:
    ./main.py --flow_log_file vpc-flow.log --lookup_table_file lookup.csv
"""


"""
For reference, see: https://www.iana.org/assignments/protocol-numbers/protocol-numbers.xhtml
"""
IANA_PROTOCOLS: Tuple[
    Literal[
        "hopopt", "icmp", "igmp", "ggp", "ipv4", "st", "tcp", "cbt", "egp", "igp",
		"bbn-rcc-mon", "nvp-ii", "pup", "argus", "emcon", "xnet", "chaos", "udp", "mux", "dcn-meas",
		"hmp", "prm", "xns-idp", "trunk-1", "trunk-2", "leaf-1", "leaf-2", "rdp", "irtp", "iso-tp4",
		"netblt", "mfe-nsp", "merit-inp", "dccp", "3pc", "idpr", "xtp", "ddp", "idpr-cmtp", "tp++",
		"il", "ipv6", "sdrp", "ipv6-route", "ipv6-frag", "idrp", "rsvp", "gre", "dsr", "bna",
		"esp", "ah", "i-nlsp", "swipe", "narp", "min-ipv4", "tlsp", "skip", "ipv6-icmp", "ipv6-nonxt",
		"ipv6-opts", "any-host-internal", "cftp", "any-local-network", "sat-expak", "kryptolan", "rvd", "ippc", "any-distributed-file-system", "sat-mon",
		"visa", "ipcv", "cpnx", "cphb", "wsn", "pvp", "br-sat-mon", "sun-nd", "wb-mon", "wb-expak",
		"iso-ip", "vmtp", "secure-vmtp", "vines", "iptm", "nsfnet-igp", "dgp", "tcf", "eigrp", "ospfigp",
		"sprite-rpc", "larp", "mtp", "ax.25", "ipip", "micp", "scc-sp", "etherip", "encap", "any-private-encryption-scheme",
		"gmtp", "ifmp", "pnni", "pim", "aris", "scps", "qnx", "a/n", "ipcomp", "snp",
		"compaq-peer", "ipx-in-ip", "vrrp", "pgm", "any-0-hop", "l2tp", "ddx", "iatp", "stp", "srp",
		"uti", "smp", "sm", "ptp", "isis-over-ipv4", "fire", "crtp", "crudp", "sscopmce", "iplt",
		"sps", "pipe", "sctp", "fc", "rsvp-e2e-ignore", "mobility-header", "udplite", "mpls-in-ip", "manet", "hip",
		"shim6", "wesp", "rohc", "ethernet", "aggfrag", "nsh"
	]
] = (
    "hopopt", "icmp", "igmp", "ggp", "ipv4", "st", "tcp", "cbt", "egp", "igp",
    "bbn-rcc-mon", "nvp-ii", "pup", "argus", "emcon", "xnet", "chaos", "udp", "mux", "dcn-meas",
    "hmp", "prm", "xns-idp", "trunk-1", "trunk-2", "leaf-1", "leaf-2", "rdp", "irtp", "iso-tp4",
    "netblt", "mfe-nsp", "merit-inp", "dccp", "3pc", "idpr", "xtp", "ddp", "idpr-cmtp", "tp++",
    "il", "ipv6", "sdrp", "ipv6-route", "ipv6-frag", "idrp", "rsvp", "gre", "dsr", "bna",
    "esp", "ah", "i-nlsp", "swipe", "narp", "min-ipv4", "tlsp", "skip", "ipv6-icmp", "ipv6-nonxt",
    "ipv6-opts", "any-host-internal", "cftp", "any-local-network", "sat-expak", "kryptolan", "rvd", "ippc", "any-distributed-file-system", "sat-mon",
    "visa", "ipcv", "cpnx", "cphb", "wsn", "pvp", "br-sat-mon", "sun-nd", "wb-mon", "wb-expak",
    "iso-ip", "vmtp", "secure-vmtp", "vines", "iptm", "nsfnet-igp", "dgp", "tcf", "eigrp", "ospfigp",
    "sprite-rpc", "larp", "mtp", "ax.25", "ipip", "micp", "scc-sp", "etherip", "encap", "any-private-encryption-scheme",
    "gmtp", "ifmp", "pnni", "pim", "aris", "scps", "qnx", "a/n", "ipcomp", "snp",
    "compaq-peer", "ipx-in-ip", "vrrp", "pgm", "any-0-hop", "l2tp", "ddx", "iatp", "stp", "srp",
    "uti", "smp", "sm", "ptp", "isis-over-ipv4", "fire", "crtp", "crudp", "sscopmce", "iplt",
    "sps", "pipe", "sctp", "fc", "rsvp-e2e-ignore", "mobility-header", "udplite", "mpls-in-ip", "manet", "hip",
    "shim6", "wesp", "rohc", "ethernet", "aggfrag", "nsh"
)

TAG_COUNT_FILE: str = "tag-counts.csv"
COLUMN_COUNT_FILE: str = "column-counts.csv"
