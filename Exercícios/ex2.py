#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 21:01:44 2019

@author: rubens
"""

"""
(2) Dê o código em python para somar os vetores:
    
(1, 2, 3, 4, 5, · · · , 100) + (1, 1, 1, 1, 1, · · · , 1)
(1, 2, 3, 4, 5, · · · , 100) + (1, 3, 5, 7, 9, · · · , 199)

"""

import numpy as np

v=np.array(range(1,101))
v1=np.ones(100)

u=np.array(v+v1)

# u=v+v1 assim tbm dá certo

t=np.array(range(1,200,2)) # range(inicio,fim,passo)

w=v+t
