#!/usr/bin/env python

'''
Create three different variables the first variable should use all lower case characters with underscore ( _ ) as the word separator. The second variable should use all upper case characters with underscore as the word separator. The third variable should use numbers, letters, and underscore, but still be a valid variable Python variable name.

Make all three variables be strings that refer to IPv6 addresses.

Use the from future technique so that any string literals in Python2 are unicode.

compare if variable1 equals variable2
compare if variable1 is not equal to variable3
'''

from __future__ import unicode_literals

this_is_variable_one = '2001:0db8:85a3:0000:0000:8a2e:0370:7334'
THIS_IS_VARIABLE_TWO = '2001:0db8:85a3:0000:0000:8a3e:0370:7334'
this_is_variable_3 = '2001:0db8:85a3:0000:0000:8a2d:0370:7335'

if this_is_variable_one == THIS_IS_VARIABLE_TWO:
    print("variable1 equals variable2")

if this_is_variable_one != this_is_variable_3:
   print("variable1 is not equal to variable3")