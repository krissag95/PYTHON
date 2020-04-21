# -*- coding: utf-8 -*-
"""
Created on Thu Oct  4 22:19:27 2018

@author: Krisag
"""

tup = ("Cristopher",23)
print (tup)
print(tup[0])
#Tuplas son inmutables
#tup[0] = "Rogelio"
###############################################

nombre, edad = tup
print(nombre)
print(edad)

lis = [("Carlos", 15),
       ("Pepe",20),
       ("Cecilia",23)]

for nombre, edad in lis:
    print(nombre)
    print(edad)