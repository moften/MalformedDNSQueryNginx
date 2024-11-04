from scapy.all import *
dns_query = IP(dst="8.8.8.8")/UDP(dport=53)/DNS(rd=1,qd=DNSQR(qname="A" * 300))
send(dns_query)
