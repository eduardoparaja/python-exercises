# -*- coding: utf-8 -*-
"""
Created on Fri Oct 26 14:36:29 2018

@author: edup_
"""

def linear(elem, lst):
    for i in range(len(lst)):
        if elem == lst[i]:
            return i
    
    return None