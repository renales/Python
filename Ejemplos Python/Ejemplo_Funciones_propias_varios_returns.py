#!/bin/python3
# coding: utf-8
# Ejemplo de funciones propias con varios valores en return
# Raul Renales 8/5/2020

def desguazar(dividendo, divisor):
     cociente = dividendo//divisor
     resto = dividendo%divisor
     return cociente,resto

#Imprimiendo los valores del return conjuntamente
print (desguazar(20,6))

#utilizando los valores del return por separado
valores = desguazar(45,6)
print(valores[0])
print(valores[1])
