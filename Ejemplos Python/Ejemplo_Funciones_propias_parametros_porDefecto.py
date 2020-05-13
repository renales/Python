#!/bin/python3
# coding: utf-8
# Ejemplo de funciones propias con parametro por defecto
# Raul Renales 8/5/2020

def descuento(precio, descuento = 5):
    return precio - (precio * descuento / 100)

print("Calculo de descuento para 100 y parametro por defecto: ")
print(descuento(100))  # 95
print("Calculo de descuento para 100 y parametro definido a 10: ")
print(descuento(100, 10))  # 90
