#!/usr/bin/env python

'''
Create a list of five IP addresses.

Use the .append() method to add an IP address onto the end of the list. Use the .extend() method to add two more IP addresses to the end of the list.

Use list concatenation to add two more IP addresses to the end of the list.

Print out the entire list of ip addresses. Print out the first IP address in the list. Print out the last IP address in the list.

Using the .pop() method to remove the first IP address in the list and the last IP address in the list.

Update the new first IP address in the list to be '2.2.2.2'. Print out the new first IP address in the list.
'''

ip_list = ['192.168.0.1', '192.168.0.2', '192.168.0.3', '192.168.0.4', '192.168.0.5']

ip_list.append('192.168.0.6')

ip_list.extend(['192.168.0.7', '192.168.0.8'])

ip_list += ['192.168.0.9', '192.168.0.10']

print(ip_list)
print(ip_list[0])
print(ip_list[9])  # better would have been to use ip_list[-1]

ip_list.pop(0)
ip_list.pop()

print()

ip_list[0] = '2.2.2.2'
print(ip_list)
print(ip_list[0])