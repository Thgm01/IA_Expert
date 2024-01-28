# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np

entradas = np.array([1, 7, 5])
pesos = np.array([0.8, 0.1, 0])

def soma(entradas, pesos):
    return entradas.dot(pesos)


def step_function(soma):
    if soma >= 1:
        return 1
    return 0


soma = soma(entradas, pesos)


resultado = step_function(soma)