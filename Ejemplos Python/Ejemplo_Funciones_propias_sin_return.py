#!/bin/python3
# coding: utf-8
# Ejemplo de funciones propias sin return
# Raul Renales 11/5/2020

def repite_saludos(saludo, nombre, repite=3):
    
    frase = saludo + nombre
    print(frase * repite)

repite_saludos('Bienvenido', 'Raul', 5)