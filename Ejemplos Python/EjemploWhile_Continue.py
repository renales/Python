#!/bin/python3
# coding: utf-8
# Ejemplo de continue en While
# Raul Renales 7/5/2020

variable = 10

while variable > 0:              
   variable = variable -1
   if variable == 5:
      continue
   print  ('Actual valor de variable:', variable)
