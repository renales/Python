#!/bin/python3
# coding: utf-8
# Ejemplo de funciones propias
# Raul Renales 8/5/2020

def mensaje():
    print("Aqui se imprime un mensaje")

def mensaje2(men):
    print("Este es el mensaje: ", men)

def areaTriangulo(base,altura):
    return base * altura / 2

def precioRetal(*metros):  
    total = 0
    for cantidad in metros:
        total= total + (cantidad * 15)
    return total


mensaje()
mensaje2("Texto para el mensaje")
print("el area del triangulo: ", areaTriangulo(10,8))
print("El precio total de los retales es: ", precioRetal(11,10,11))
