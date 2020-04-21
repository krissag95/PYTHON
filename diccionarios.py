# -*- coding: utf-8 -*-
"""
Created on Thu Oct  4 22:05:36 2018

@author: Krisag
"""

di = {"Colima":"Col","Jalisco":"Jal","Michoacan":"Mich"}

suma = {}
suma["numero"] += 5 
print("SUMA = "+str(suma["numero"]))
print(di)
print(di["Colima"])
di["Nayarit"] = "Nay"
print(di)

if "Colima" in di:
    print("Colima esta en el diccionario")
    
##############################################
print(di.items())

#convertir a tuplas el contenido del diccionario
for key, value in di.items():
    print(key + ": " + value)