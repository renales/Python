#!/bin/python3
# coding: utf-8
# Ejemplo de uso avanzado de excepciones
# Raul Renales 13/5/2020

try:
    x = int(input("Ingresa un numero: "))
    y = 1 / x
    print(y)
except ZeroDivisionError:
    print("No puedes dividir entre cero, introduce otro numero.")
except ValueError:
    print("Por favor, ingresa un numero.")
except:
    print("Oh my god!!!, algo salio mal...")


print("THE END.")
