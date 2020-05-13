#!/bin/python3
# coding: utf-8
# Ejemplo de condicional if
# Raul Renales 7/5/2020

#Definir variables
dato1, dato2, dato3, dato4 = 21, 10, 5, 20
coleccion = [10,20,30,40,50,60,70,80,90,100] 

#Ejemplo de operador de comparación Igual
if (dato1 == dato2):
    print ("'dato1' y 'dato2' son iguales.")
else:
    print ("'dato1' y 'dato2' no son iguales.")

#Ejemplo de operador de comparación Distinto
if (dato1 != dato2):
    print ("'dato1' y 'dato2' son distintas.")
else:
    print ("'dato1' y 'dato2' no son distintas.")

#Ejemplo de operador de comparación Diferente
if (dato1 != dato2):
    print ("'dato1' y 'dato2' son diferentes.")
else:
    print ("'dato1' y 'dato2' no son diferentes.")

#Ejemplo de operador de comparación Menor que
if (dato1 < dato2):
    print ("'dato1' es menor que 'dato2'.")
else:
    print ("'dato1' no es menor que 'dato2'.")

#Ejemplo de operador de comparación Mayor que
if (dato1 > dato2):
    print ("'dato1' es mayor que 'dato2'.")
else:
    print ("'dato1' no es mayor que 'dato2'.")

#Ejemplo de operador in
if (dato2 in coleccion):
    print ("'dato2' esta en la coleccion.")
else:
    print ("No esta en la coleccion.")

#Ejemplo de operador is
if (dato2 is dato3):
    print ("Son objetos identicos.")
else:
    print ("No son objetos identicos.")