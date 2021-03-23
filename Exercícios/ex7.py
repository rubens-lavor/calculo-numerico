#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 22:37:16 2019

@author: rubens
"""

"""

(7) Dê os códigos em python para os 4 métodos de Zeros de Funções, com o erro (b−a)/2.


"""

import numpy as np


def bisseccao(f,a,b,TOL=1E-4,NMAX=50,output=False):
    
    print("Método da bissecção")
    
    """
    ----------------------------------------------------------------------
    
    Implementação do método da bissecção: método utiliza um intervalo [a,b], 
    onde a multiplicação de f(a)*f*(b) é menor que zero. 
    Sua função é encontrar zero de funções em determinado intervalo.
    
    ----------------------------------------------------------------------
    """
    
    
    assert(f(a)*f(b)<0),"O produto da imagem dos extremos deve ser menor que 0"
    assert(b>a),"b deve ser maior que a"
    i=0
    while (b-a)*0.5 > TOL and  i < NMAX:
        i=i+1
        p=(a+b)/2
        if f(p)==0:break
        if f(b)*f(p) > 0:
            b=p
        else:
            a=p
    if(output):    
        print ("iteração:", i, "ponto em x =", p,"erro",(b-a)*0.5, "f(p) =", f(p))     
    assert (i<=NMAX),"O numero maximo de iterações foi atingido"
    
    return i,p,(b-a)*0.5





def ponto_fixo(g, p0,  TOL = 1E-4, NMAX=40, output=False):
    
    print("Método do ponto fixo")
    
    """
    ------------------------------------------------------------------
    
    Se g est´a definida em [a, b] e g(p) = p para algum p ∈ [a, b],
    ent˜ao diz-se que a fun¸c˜ao g tem um ponto fixo p em [a, b].
    
    ------------------------------------------------------------------
    
    """
    
    i=0
    while(i<NMAX):
        i+=1
        p1=g(p0)
        if(output):
            print("iteração", i, ':',p1, "erro:", np.abs(p1-p0))
        if g(p1)==p1:break    
        if (np.abs(p1-p0) <TOL):break
        
        else:
            p0=p1
            assert(i <NMAX), "Numero maximo de iteracoes atingido"       
    
    return i, p1,np.abs(p1-p0)






def newton(f, df, p0,  TOL = 1E-4, NMAX=40, output=False):
    
    print("Método de Newton -- f(x)=x²-sin(x) ")
    
    """
    ---------------------------------------------------------------
    
    --------------------------------------------------------------
    
    """
    assert(df(p0) !=0),"a derivada não pode ser nula"
    i=0
    while(i<NMAX):
        i+=1
        p1=p0 -(f(p0)/df(p0))
        if(output):
            print("iteração", i, ':',p1, "erro:", np.abs(p1-p0))
        if f(p1)==0: break
        if (np.abs(p1-p0) <TOL):break
        
        else:
            p0=p1
    
    assert(i <NMAX), "Numero maximo de iteraçoes atingido"       
    
    return i, p1,np.abs(p1-p0)






def secante(f, p0,p1, TOL = 1E-4, NMAX=100, output=False):
    
    print("Método da secante -- f(x)=cos(x)-e^x")
    
    """
      Implementação do método da secante, para quando as derivadas são muito 
      trabalhosas para serem feitas na mão e etc. 
    """
    i=0
    while(i<NMAX):
        i+=1
        p2=p1-(f(p1)*(p1-p0))/(f(p1)-f(p0))
        if(output):
            print("iteração", i, ':',p1, "erro:", np.abs(p2-p1))
        if f(p2)==0: break
        if (np.abs(p2-p1)<TOL):break
        else:
            p0=p1
            p1=p2
    
    assert(i <NMAX), "Numero maximo de iteracoes atingido"
    
    return i, p2,np.abs(p2-p1)



print("")

bisseccao(lambda x: (x**2+1)*np.sin(x), 2, 4, output=True)
print("")

ponto_fixo(lambda x:np.cos(x)/2,0.5, output=True)
print("")

newton(lambda x: x**2-np.sin(x),lambda x:2*x-np.cos(x),0.8, output=True)
print("")

secante(lambda x:np.cos(x)-np.exp(x),-1.3, -1.2, TOL = 1E-5, output=True)
print("")
