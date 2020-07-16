#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 22:15:29 2019

@author: rubens
"""

"""

(6) Dê o código em python para plotar os gráficos das funções f(x) = x^3 + x^2 − x,

x ∈ [−2, 2] e g(x) = sin(x^2) com x ∈ [−2, 2]

"""

import numpy as np
import matplotlib.pylab as plt


x=np.linspace(-2,2,50)
f=x**3 + x**2 - x
g=np.sin(x**2)

plt.plot(x,f,"r", label="$f(x)=x^3 + x^2 − x$")
plt.plot(x,g,"y", label="$g(x)=sin(x^2)$")
plt.grid() 
plt.legend() #para aparecer a legenda
#plt.margins(0.1)
plt.show()

