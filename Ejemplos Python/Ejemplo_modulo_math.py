#!/bin/python3
# coding: utf-8
# Ejemplo de uso del modulo math
# Raul Renales 13/5/2020

import math

#Ejemplo de redondeo hacia abajo
print(math.floor(3.99))  # Redondeo a la baja (suelo)

#Ejemplo de redondeo hacia arriba
print(math.ceil(3.01))   # Redondeo al alta (techo)
 
#Ejemplo de sumatorio
numeros = [0.9999999, 1, 2, 3]
print(math.fsum(numeros)) 

#Ejemplo de truncamiento o quedarnos con la parte entera
print(math.trunc(123.45))

#Ejemplo de potencias y raices
print(math.pow(2, 3))  #Potencia 
print(math.sqrt(9))    # Raíz cuadrada

#Ejemplo de constantes
print(math.pi)  # Constante pi
print(math.e)   # Constante e