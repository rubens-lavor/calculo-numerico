#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 21:18:25 2019

@author: rubens
"""

"""

(3) Dê o código em python para gerar os 100 primeiros πi’s, 

usando essa relação derecorrência.

(PI)n = (PI)n−1 +(4(−1)^n)/(2n + 1)

"""

pi=4.0

for i in range(1,101):
    #print ("range ", i, "pi ",pi)
    pi = pi + (4*(-1)**i) / (2*i +1)
    
print(pi)