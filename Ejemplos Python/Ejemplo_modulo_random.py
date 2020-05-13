#!/bin/python3
# coding: utf-8
# Ejemplo de uso del modulo random
# Raul Renales 13/5/2020

import random

# Numero aleatorio entre 0 y 1
print(random.random())      

# Numero aleatorio entre 1 y 10      
print(random.uniform(1,10))

# Numero aleatorio de 0 a 9 (entero)
print(random.randrange(10))

# Numero de 0 a 100
print(random.randrange(0,101))

# Numero aleatorio de 0 a 100 con saltos de 2 números
print(random.randrange(0,101,2))

# Letra aleatoria
print(random.choice('Makauli kuki'))

# Elemento aleatorio
print(random.choice([1,2,3,4,5]))

# Dos elementos aleatorios
print(random.sample([1,2,3,4,5], 3))

# Barajar una lista
lista = [1,2,3,4,5,6,7,8,9,10]
random.shuffle(lista)
print(lista)