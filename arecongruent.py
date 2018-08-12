# -*- coding: utf-8 -*-
"""
Created on Mon Sep 26 02:49:39 2016

@author: 100484737
"""

import os, sys

#the following function checks if values of a and b are congurent
def congruencyCheck(a, b, n):
    a = int(a)
    b = int(b)
    n = int(n)
    
    if (a % n == b % n):
        return True
    else:
        return False

#main method   
print(congruencyCheck(sys.argv[1], sys.argv[2], sys.argv[3]))
