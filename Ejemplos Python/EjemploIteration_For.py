#!/bin/python3
# coding: utf-8
# Ejemplo de bucle for con else
# Raul Renales 7/5/2020

frase = 'Hola'
letra = iter(frase)
cantidad = len(frase)

try:
    while cantidad >= 0:
        print(letra.__next__())
except StopIteration:
    print("Se acabaron las letras")