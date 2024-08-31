from typing import Literal, Tuple

"""
Represents a protocol from IANA's list of protocols
For reference, see: https://www.iana.org/assignments/protocol-numbers/protocol-numbers.xhtml
"""
IanaProtocol = Literal[
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

"""
Maps the IANA number of each protocol to its name via index
For reference, see: https://www.iana.org/assignments/protocol-numbers/protocol-numbers.xhtml
"""
IanaProtocols = Tuple[
    Literal['hopopt'], Literal['icmp'], Literal['igmp'], Literal['ggp'], Literal['ipv4'], Literal['st'], Literal['tcp'], Literal['cbt'], Literal['egp'], Literal['igp'], Literal['bbn-rcc-mon'], Literal['nvp-ii'], Literal['pup'], Literal['argus'], Literal['emcon'], Literal['xnet'], Literal['chaos'], Literal['udp'], Literal['mux'], Literal['dcn-meas'], Literal['hmp'], Literal['prm'], Literal['xns-idp'], Literal['trunk-1'], Literal['trunk-2'], Literal['leaf-1'], Literal['leaf-2'], Literal['rdp'], Literal['irtp'], Literal['iso-tp4'], Literal['netblt'], Literal['mfe-nsp'], Literal['merit-inp'], Literal['dccp'], Literal['3pc'], Literal['idpr'], Literal['xtp'], Literal['ddp'], Literal['idpr-cmtp'], Literal['tp++'], Literal['il'], Literal['ipv6'], Literal['sdrp'], Literal['ipv6-route'], Literal['ipv6-frag'], Literal['idrp'], Literal['rsvp'], Literal['gre'], Literal['dsr'], Literal['bna'], Literal['esp'], Literal['ah'], Literal['i-nlsp'], Literal['swipe'], Literal['narp'], Literal['min-ipv4'], Literal['tlsp'], Literal['skip'], Literal['ipv6-icmp'], Literal['ipv6-nonxt'], Literal['ipv6-opts'], Literal['any-host-internal'], Literal['cftp'], Literal['any-local-network'], Literal['sat-expak'], Literal['kryptolan'], Literal['rvd'], Literal['ippc'], Literal['any-distributed-file-system'], Literal['sat-mon'], Literal['visa'], Literal['ipcv'], Literal['cpnx'], Literal['cphb'], Literal['wsn'], Literal['pvp'], Literal['br-sat-mon'], Literal['sun-nd'], Literal['wb-mon'], Literal['wb-expak'], Literal['iso-ip'], Literal['vmtp'], Literal['secure-vmtp'], Literal['vines'], Literal['iptm'], Literal['nsfnet-igp'], Literal['dgp'], Literal['tcf'], Literal['eigrp'], Literal['ospfigp'], Literal['sprite-rpc'], Literal['larp'], Literal['mtp'], Literal['ax.25'], Literal['ipip'], Literal['micp'], Literal['scc-sp'], Literal['etherip'], Literal['encap'], Literal['any-private-encryption-scheme'], Literal['gmtp'], Literal['ifmp'], Literal['pnni'], Literal['pim'], Literal['aris'], Literal['scps'], Literal['qnx'], Literal['a/n'], Literal['ipcomp'], Literal['snp'], Literal['compaq-peer'], Literal['ipx-in-ip'], Literal['vrrp'], Literal['pgm'], Literal['any-0-hop'], Literal['l2tp'], Literal['ddx'], Literal['iatp'], Literal['stp'], Literal['srp'], Literal['uti'], Literal['smp'], Literal['sm'], Literal['ptp'], Literal['isis-over-ipv4'], Literal['fire'], Literal['crtp'], Literal['crudp'], Literal['sscopmce'], Literal['iplt'], Literal['sps'], Literal['pipe'], Literal['sctp'], Literal['fc'], Literal['rsvp-e2e-ignore'], Literal['mobility-header'], Literal['udplite'], Literal['mpls-in-ip'], Literal['manet'], Literal['hip'], Literal['shim6'], Literal['wesp'], Literal['rohc'], Literal['ethernet'], Literal['aggfrag'], Literal['nsh']
]

IANA_PROTOCOLS: IanaProtocols = (
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
