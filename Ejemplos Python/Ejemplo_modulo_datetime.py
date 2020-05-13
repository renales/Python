#!/bin/python3
# coding: utf-8
# Ejemplo de uso del modulo datetime
# Raul Renales 13/5/2020

from datetime import datetime


#Fecha actual
dt = datetime.now()    # Fecha y hora actual

print(dt)
print(dt.year)         # año
print(dt.month)        # mes
print(dt.day)          # día

print(dt.hour)         # hora
print(dt.minute)       # minutos
print(dt.second)       # segundos
print(dt.microsecond)  # microsegundos

print("{}:{}:{}".format(dt.hour, dt.minute, dt.second))
print("{}/{}/{}".format(dt.day, dt.month, dt.year))

#Fecha definida por el usuario
dt = datetime(2000,1,21)
print(dt)