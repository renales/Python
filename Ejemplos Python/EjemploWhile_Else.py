#!/bin/python3
# coding: utf-8
# Ejemplo de else en while
# Raul Renales 7/5/2020

promedio, total, contar = 0.0, 0, 0
mensaje = "Introduzca la nota de un estudiante (-1 para salir): "

grado = int(input(mensaje))
while grado != -1:
    total = total + grado
    contar += 1
    grado = int(input(mensaje))
else:
    promedio = total / contar
    print ("Promedio de notas del grado escolar: ", str(promedio))
