#!/usr/bin/env python

'''
Read the 'show_ip_bgp_summ.txt' file into your program. From this BGP output obtain the first and last lines of the output.

From the first line use the string .split() method to obtain the local AS number.

From the last line use the string .split() method to obtain the BGP peer IP address.

Print both local AS number and the BGP peer IP address to the screen.
'''

with open("show_ip_bgp_summ.txt") as f:
    ip_bgp_summ = f.readlines()

first_line = ip_bgp_summ[0]
last_line = ip_bgp_summ[-1]

print(first_line)
print(last_line)

_, _, _, _, _, _, _, as_number = first_line.split() # better is as_number = first_line.split()[-1]
bgp_peer, _, _, _, _, _, _, _, _, _ = last_line.split() # better is bgp_peer = last_line.split()[0]

print(f"AS Number: {as_number}\nBGP Peer IP: {bgp_peer}")
