#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 21:47:38 2019

@author: rubens
"""

"""

(5) Dê o código em python para definir uma função que soma os números naturais de

1 até n > 1, e acrescente no código um erro para o computador parar caso seja

colocado números inteiros nessa soma. Lembre de escrever a mensagem avisando o

tipo de erro.

"""
#import numpy as np

def soma_naturais(n):
    soma=0.0
    assert n>0, "o valor de n deve ser positivo"
    assert type(n)==int,"o valor de n tem que ser inteiro"

    for i in range(1,n+1):
        soma=soma+i
    return soma

n=soma_naturais(3)