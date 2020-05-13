#!/bin/python3
# coding: utf-8
# Ejemplo de funciones propias con parametro diccionario
# Raul Renales 8/5/2020

def tasa_prod(trabajadores, **seccion):
    #Funcion que evalua el % de trabajadores por encima de la productividad
    #Exigida por la empresa
 
    total=0
    for trab in seccion.values():
        total += trab
 
    return trabajadores * 100 / total

porcentaje_produ = tasa_prod(78, taller = 44, admin = 25, logistica = 31)
print("El porcentaje de trabajadores que estan por encima del nivel exigido de produccion es: ", porcentaje_produ)