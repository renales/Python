#!/bin/python3
# coding: utf-8
# Ejemplo de uso de raise
# Raul Renales 13/5/2020

try:
    x = int(input("Ingresa un n�mero: "))
    y = 1 / x
    print(y)
except Exception as e:  # almacenamos la excepci�n en e
    print("Ha ocurrido un error =>", type(e).__name__)


