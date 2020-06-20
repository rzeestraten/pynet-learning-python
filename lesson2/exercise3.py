#!/usr/bin/env python

'''
Read in the "show_arp.txt" file using the readlines() method. Use a list slice to remove the header line.

Use pretty print to print out the resulting list to the screen, syntax is:

from pprint import pprint
pprint(some_var)


Use the list .sort() method to sort the list based on IP addresses.

Create a new list slice that is only the first three ARP entries.

Use the .join() method to join these first three ARP entries back together as a single string using the newline character ('\n') as the separator.

Write this string containing the three ARP entries out to a file named "arp_entries.txt".
'''

with open("show_arp.txt") as f:
    contents = f.readlines()

contents = contents[1:]

print()

from pprint import pprint
pprint(contents)

print()

contents.sort()
pprint(contents)

print()

new_list = contents[0:3]
pprint(new_list)

print()

new_string = "\n".join(new_list)

f = open("arp_entries.txt", mode="w")
f.write(new_string)
f.close()
