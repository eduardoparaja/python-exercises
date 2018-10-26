# -*- coding: utf-8 -*-
"""
Created on Fri Oct 26 14:36:29 2018

@author: edup_
"""

def linear(num, lst):
    for i in range(len(lst)):
        if num == lst[i]:
            return i
    
    return None