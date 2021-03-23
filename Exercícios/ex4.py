#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 21:33:03 2019

@author: rubens
"""

"""
(4) Dê o código em python para gerar π com precisão EA < 0.00001, usando essa relação

de recorrência. (PI)n = (PI)n−1 +(4(−1)^n)/(2n + 1)

"""
import numpy as np


x=np.pi
#ref=3.14159265359

pi=4.0
EA=1.0
i=1

while EA > 0.00001:
    pi = pi + (4*(-1)**i) / (2*i +1)
    i=i+1
    EA=np.abs(pi-x)

print(EA,i)
    