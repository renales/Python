#!/bin/python3
# coding: utf-8
# Ejemplo de uso del modulo datetime y operaciones con fechas
# Raul Renales 13/5/2020

from datetime import datetime, timedelta

dt = datetime.now()
print(dt.strftime("%A %d de %B del %Y - %H:%M"))

# Generamos 20 días con 8 horas y 300 segundos de tiempo
t = timedelta(days=20, hours=8, seconds=300)
print("Fecha creada por mi: ", t)


# Lo operamos con el datetime de la fecha y hora actual
dentro_de_dos_semanas = dt + t
print(dentro_de_dos_semanas.strftime("%A %d de %B del %Y - %H:%M"))
hace_dos_semanas = dt - t
print(hace_dos_semanas.strftime("%A %d de %B del %Y - %H:%M"))
 