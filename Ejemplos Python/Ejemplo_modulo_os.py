#!/bin/python3
# coding: utf-8
# Ejemplo de uso del modulo OS
# Raul Renales 13/5/2020

import sys 

print("El ejecutable del interprete esta en: ", sys.executable)
print("Plataforma: ",sys.platform)
print("Version: ",sys.version)
print("Encoding",sys.getdefaultencoding())
print("Encodign del filesystem: ",sys.getfilesystemencoding())
