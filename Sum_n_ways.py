# -*- coding: utf-8 -*-
"""
Created on Sat Feb 11 09:32:02 2023

@author: ramli
"""

def sum1 (val1, val2 = 20):
    total = val1 + val2
    return total

def sum2 (val1, val2):
    return val1 + val2

"""
print (sum1(1,2))

try:
    print (sum1())
# default Err. Msg:
#TypeError: sum1() missing 1 required positional argument: 'val1'
except TypeError:
    print ("Not enough Arguments in sum1 function call. sum1 (val1, val2 = 20)")
"""

"""
try:
    print (sum2(10,30,40))
except TypeError as err_handler:
    #print ("More than enough Arguments in sum2 function call. sum1 (val1, val2 = 20)")
    for i in err_handler.args:
        print (err_handler.args[0])
        print (err_handler.args[0][13])
"""