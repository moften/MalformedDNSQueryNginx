# MalformedDNSQueryNginx
# m10sec@proton.me
Malformed DNS Query PoC


Explanation of PoC:

The script uses Scapy to generate and send a DNS query to specific server.
The qname field of the DNS query is filled with a string of 300 repeated “A” characters, creating a malformed request.
While this PoC does not directly exploit Nginx, it demonstrates how malformed or unexpected input can be used in a network interaction, potentially leading to misconfigurations being revealed.

