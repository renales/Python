#!/bin/python3
# coding: utf-8
# Ejemplo de while
# Raul Renales 7/5/2020

#Generamos las variables
suma, numero = 0, 1

#Creamos un ciclo que se ejecutara mientras
#numero sea menor o igual que 10
while numero <= 10:
    suma = numero + suma
    numero = numero + 1
    print(numero)
print ("La suma es ", suma)