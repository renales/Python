#!/bin/python3
# coding: utf-8
# Ejemplo de operaciones aritmeticas
# Raul Renales 6/5/2020


print ("\nHablando con tu PC")
print ("=====================")

print ("\nHola, bienvenido a tu ordenador")
print ("------------------------------\n")

print ('PC: ¿Cómo se llama usted?: ') 
nombre = input('Yo: ')
print ('PC: Hola', nombre, ', encantado de conocerte')

print ('PC: ¿Que edad tiene usted?: ')
edad = input('Yo: ')
print ('Usted tiene', edad, ', y yo ya no digo mi edad')

print ('PC: ¿Tienes WebCam?, ingrese "si" o "no", por favor!: ')
tiene_WebCam = input('Yo: ')

if tiene_WebCam in ('s', 'S', 'si', 'Si', 'SI'):
	print ("Ponga la WebCam para verle")
elif tiene_WebCam in ('n', 'no', 'No', 'NO'):
	print ("Lastima por usted, Adiós")