#!/bin/python3
# coding: utf-8
# Ejemplo de condicional if
# Raul Renales 7/5/2020

#Recogemos un valor por pantalla y almacenamos en numero
#Recordar que eval sirve para evaluar el dato que recibimos
#Recordar que int() lo usamos para pasar una cadena a numero entero
numero = int(eval(input("\nIngresa un número entero, por favor: ")))

#Bloque condicional
if numero < 0:
    numero = 0
    print ('El número ingresado es negativo cambiado a cero.\n')
elif numero == 0:
    print ('El número ingresado es 0.\n')
elif numero == 1:
    print ('El número ingresado es 1.\n')
else:
    print ('El número ingresado es mayor que uno.\n')