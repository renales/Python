#!/bin/python3
# coding: utf-8
# Ejemplo de funciones matematicas
# Raul Renales 7/5/2020

#Variables a utilizar en el ejemplo
a=1
b=10.468
c={10,23,14,15,23,11,159}

#Uso de las funciones

print("El valor absoluto de: ", b, " es: ", abs(b))
print("La parte entera de: ", b, " es: ", int(b))
print("El valor mas alto de la coleccion: ", c, " es: ", max(c))
print("El valor mas pequeño de la coleccion: ", c, " es: ", min(c))
print("El valor redondeado de: ", b, " es: ", round(b))
print("El valor de elevar ", int(b), " a ", a, " es: ", pow(int(b),a))
print("El valor de la suma de todos los valores de: ", c, " es: ", sum(c))