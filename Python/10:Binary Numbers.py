#!/bin/python3

import sys


def convert_2binary_maxlen(n):
    max_len = 0
    len=0
    while( n > 0 ):
        temp = n%2
        #print(temp)
        if(temp == 1):
            #print(n)
            len = len + 1
            if(len > max_len):
                max_len = len
                #print("current_max_len",max_len)
        else:
            len = 0
        n=int(n/2)
    return max_len
    
n = int(input().strip())
print(convert_2binary_maxlen(n))
