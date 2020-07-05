#!/usr/bin/env python

'''
Read the 'show_lldp_neighbors_detail.txt' file. Loop over the lines of this file. Keep reading the lines until you have encountered the remote "System Name" and remote "Port id". Save these two items into variables and print them to the screen. You should extract only the system name and port id from the lines (i.e. your variables should only have 'twb-sf-hpsw1' and '15'). Break out of your loop once you have retrieved these two items.
'''

with open("show_lldp_neighbors_detail.txt") as f:
    contents = f.read()

system_name = None
port_id = None

for line in contents.splitlines():

    if 'System Name:' in line:
        system_name = line.split()[2]

    if 'Port id:' in line:
        port_id = line.split()[2]

    if system_name and port_id:
        print("Exit from loop\n")
        break

print()
print(f"System Name: {system_name}\nPort id: {port_id}")
print()
