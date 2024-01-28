#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 27 22:23:38 2024

@author: thiago
"""

import numpy as np

entradas = np.array([[0,0], [0,1], [1,0], [1,1]])
saidas = np.array([0,0,0,1])
pesos = np.array([0.0,0.0])
taxa_aprendizagem = 0.1

def step_function(soma):
    if soma >= 1:
        return 1
    return 0

def calcula_saida(registro):
    soma = registro.dot(pesos)
    return step_function(soma)

def treinar():
    erroTotal = 1
    while erroTotal != 0:
        erroTotal = 0
        for i in range(len(saidas)):
            saidaCalculada = calcula_saida(np.array(entradas[i]))
            erro = abs(saidas[i]-saidaCalculada)
            erroTotal += erro
            for j in range(len(pesos)):
                pesos[j] = pesos[j] + (taxa_aprendizagem * entradas[i][j] * erro)
                print(f"Peso atualizado: {pesos[j]}")
                
        print(f"Total de erros: {erroTotal}")
        
treinar()
print('Rede Neural Treinada')
print(calcula_saida(entradas[0]))
print(calcula_saida(entradas[1]))
print(calcula_saida(entradas[2]))
print(calcula_saida(entradas[3]))
                
            
            