#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 28 02:52:46 2022

@author: susan
"""

# two's compliment hex converter
# expected input is HEX byte as a string e.g. 'E2' upper or lowwer case don't matter.

def twoscomp(hexbyte):
    x = hex(~ (~ (int(hexbyte, 16)) + 1))
    return x

    
print(twoscomp('E2'))
    
    