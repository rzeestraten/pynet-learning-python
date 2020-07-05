#!/usr/bin/env python

import re
from pprint import pprint

'''
Read the "show_vlan.txt" file into your program. Loop through the lines in this file and extract all of the VLAN_ID, VLAN_NAME combinations.
From these VLAN_ID and VLAN_NAME construct a new list where each element in the list is a tuple consisting of (VLAN_ID, VLAN_NAME).
Print this data structure to the screen. Your output should look as follows:

[('1', 'default'),
 ('400', 'blue400'),
 ('401', 'blue401'),
 ('402', 'blue402'),
 ('403', 'blue403')]
 '''

with open("show_vlan.txt") as f:
    contents = f.readlines()

vlan_list = []

for line in contents:
    vlan_id = line.split()[0]
    vlan_name = line.split()[1]

    # use regular expression to check if variable is numeric
    pattern = re.compile("^[0-9]+$")
    if pattern.match(vlan_id):
        vlan_list += [(vlan_id, vlan_name)]
        
pprint(vlan_list)
