# -*- coding: utf-8 -*-
"""
Spyder Editor

Este é um arquivo de script temporário.
"""

#----------------------------------------------------------------

"""
(1) Dê o código em python para plotar o gráfico da função f(x) = x² + xcos(x) − x − 2
com x ∈ [−3, 4].

"""

#----------------------------------------------------------------


import numpy as np
import matplotlib.pylab as plt


x = np.linspace(-3,4,100)
#y = np.linspace(-3,4,100)
y=(x**2+x*np.cos(x)-x-2)
plt.plot(x,y,"g-", label="$f(x)=x²+x.cos(x)-x-2$")
plt.grid() 
plt.legend()
#plt.margins(0.1)
plt.show()