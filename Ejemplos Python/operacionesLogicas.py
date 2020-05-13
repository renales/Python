#!/bin/python3
# coding: utf-8
# Ejemplo de operaciones Logicas
# Raul Renales 7/5/2020

#Definir variables 
a, b = 10, 20

#Ejemplo de operador lógico and

if (a and b):
   print ("Las variables 'a' y 'b' son VERDADERO.")
else:
   print ("O bien la variable 'a' no es VERDADERO o la variable 'b' no es VERDADERO.")

#Ejemplo de operador lógico or

if (a or b):
   print ("O bien la variable 'a' es VERDADERA o la variable 'b' es VERDADERA o ambas variables son VERDADERAS.")
else:
   print ("Ni la variable 'a' es VERDADERA ni la variable 'b' es VERDADERA.")

#Ejemplo de operador lógico not

if not(a and b):
   print ("Ni la variable 'a' NO es VERDADERA o la variable b NO es VERDADERA.")
else:
   print ("Las variables 'a' y 'b' son VERDADERAS.")