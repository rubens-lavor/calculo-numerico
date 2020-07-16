#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 21:01:43 2019

@author: rubens
"""

"""

(1) Dê o código em Python:

(a) da substituição regressiva e da 
substituição progressiva de 
sistemas lineares.

(b) do método de jacobi.

(c) do método de gauss-seidel.

(d) da spline linear.

(e) para plotar o gráfico da spline linear.

(f) do método da regra do trapézio composta
(integração fechada).

(g) do método regra de 1/3 de simpson composta 
(integração fechada).

(h) do método regra de 3/8 de simpson composta 
(integração fechada).

"""
import numpy as np 
import matplotlib.pylab as plt
from numpy.linalg import norm


def subreg (A,b):
    N,M=A.shape
    assert(N == M), " a matriz A não é quadrada."
    assert(N == len(b)), " os tamanhos de A e b são incompatíveis."
    x=np.zeros(N,dtype=np.float32)
    for i in range(N-1,-1,-1): #como é decrescentre ele inicia em n-1 e vai até -1, dai ele para no zero. o outro -1
                                #é pra ele seguir de 1 em 1 mas no sentido contrário (regressívo)
        soma=0.0
        for j in range(i+1,N): #atenção onde para!!! qnd é crescente ele vai até o numero consecutivo mas sem ler o 
                                #numero, nesse exemplo j vai até N-1, porém para ler o N-1 ele tem que ir até N-1 +1
                                #o sucessor. no range recressivo acontece da mesma forma só que no outro sentido
            soma = soma + A[i,j]*x[j]
        
        x[i]=(b[i]-soma)/A[i,i]
    
    return x

def subpro (A,b):
    N,M=A.shape
    assert(N == M), " a matriz A não é quadrada."
    assert(N == len(b)), " os tamanhos de A e b são incompatíveis."
    y=np.zeros(N,dtype=np.float32)
    for i in range(0,N):
        soma=0.0
        for j in range(0,i-1): #nao posso colocar N-1, tem que ser i-1, senoa dá erro pq ele acaba entrando no for 
                                #quando nao deve
            soma = soma + A[i,j]*y[j]
        
        y[i]=(b[i]-soma)/A[i,i]
    
    return y



def jacobi(A,b,x0,TOL=1e-3,NMAX=50,output=False):
    N=len(b)
    x1=np.zeros(N,dtype=np.float64)
    n=0
    EA=TOL+1
    while (EA>TOL) and (n<NMAX):
        n=n+1
        for i in range (0,N):
            soma=0.0
            for j in range (0,N):
                if (j!=i):
                    soma=soma+A[i,j]*x0[j]
            x1[i]=(b[i]-soma)/A[i,i]
        EA=norm(x1-x0)
        if(output):
            print("x na iteração",n,"é:",x1,"e o erro é:",EA)
        x0=np.copy(x1)
    return x1,EA
A=np.array([[10,2,1],
            [3,5,1],
            [2,3,10]],dtype=np.float64)
    
b=np.array([7,-8,6],dtype=np.float64)

jacobi(A,b,(0,0,0),output=True)






def gausseidel(A,b,x0,TOL=1e-3,NMAX=50,output=False):
    N=len(b)
    x1=np.zeros(N,dtype=np.float64)
    n=0
    EA=TOL+1
    while (EA>TOL) and (n<NMAX):
        n=n+1
        for i in range (0,N):
            soma1=0.0
            soma2=0.0
            for j in range (0,i):
                    soma1 = soma1 + A[i,j]*x1[j]
            for j in range(i+1,N):
                soma2 = soma2 + A[i,j]*x0[j]
            x1[i]=(b[i]-soma1+soma2)/A[i,i]
        EA=norm(x1-x0)
        if(output):
            print("x na iteração",n,"é:",x1,"e o erro é:",EA)
        x0=np.copy(x1)
    return x1,EA



A=np.array([[10,2,1],
            [3,5,1],
            [2,3,10]],dtype=np.float64)
    
b=np.array([7,-8,6],dtype=np.float64)

gausseidel(A,b,(0,0,0),output=True)

def splinelin(x,y,z):
    assert(z>x[0] and z<x[-1]), "z deve estar no intervalo entre x0 e xn"
    i = 0
    while(z > x[i+1]):
        i = i + 1
    return  y[i] + (y[i+1] - y[i])/(x[i+1] - x[i])*(z - x[i])

splinelin((3,4.5,7,9), (2.5,1,2.5,0.5), 5)
plt.plot((3,4.5,7,9), (2.5,1,2.5,0.5))
plt.plot((3,4.5,7,9), (2.5,1,2.5,0.5), 'ro')
plt.plot(5,splinelin((3,4.5,7,9), (2.5,1,2.5,0.5), 5), 'g*')
plt.grid()
plt.show()


def trapezioc(a,b,f,n):
    assert (b>a), "b deve se maior que a"
    h=(b-a)/n
    soma=0.0
    for i in range (1,n-1+1):
        soma = soma + 2*f(a+i*h)
    I=h*0.5*(f(a) + soma + f(b))
    return I