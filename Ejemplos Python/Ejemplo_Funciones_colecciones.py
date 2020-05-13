#!/bin/python3
# coding: utf-8
# Ejemplo de funciones colecciones
# Raul Renales 7/5/2020

#Variables a utilizar en el ejemplo

a={1,3,4,6,7,44,32}
b={"Raul","Pepe","Lucas","Juan"}
c={True, True, False, True}


#Uso de las funciones

print("El resultado de evaluar con All la coleccion ", c, " es: ", all(c))
print("El resultado de evaluar con ANY la coleccion ", c, " es: ", any(c))
print("El tamaño de la coleccion ", b, " es: ", len(b))
print("La nueva coleccion resultante de ", c, " y ", a, " es: ", zip(c,a))