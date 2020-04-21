# -*- coding: utf-8 -*-
"""
Created on Thu Oct  4 23:04:10 2018

@author: Krisag
"""


with open("C:/Users/Krisag/Documents/CourseMaterial/data/names.csv", "r") as file:
    names = {}
    count = 0
    for line in file:
        if count == 0:
            count += 1
            continue
        keys = line.strip().split(",")
        #print(keys)
        if keys[1] in names:
            names[keys[1]] += int(keys[5])
        else:
            names[keys[1]] = int(keys[5])
        #break
        #count += 1
        #if count == 50:
        #    break
    print(names)
    print(names["James"])
bigger = 0
common_name = ""
for name, number in names.items():
    if bigger < number:
        bigger = number
        common_name = name
    
print ("The most common name is " + common_name + " with the value: " + str(bigger))