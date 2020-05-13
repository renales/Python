#!/bin/python3
# coding: utf-8
# Ejemplo de uso de raise
# Raul Renales 13/5/2020

try:
    print("Vamos a provocar un error")
    raise ZeroDivisionError("No utilizar cero en esta operaicon")
except ZeroDivisionError:
    print("No se puede poner cero")

