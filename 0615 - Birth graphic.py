# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal
"""

import matplotlib.pyplot as plt 

xs = []
ys = []

name = "Max"
gender = "M"
state = "CA"
year1 = 1950
year2 = 2000

with open("C:/Users/Krisag/Documents/CourseMaterial/data/names.csv", "r") as file:
    counter = 0
    people = 0
    for line in file:
        counter = counter + 1
        line_split = line.strip().split(",")
        if line_split[1] == name and int(line_split[2]) >= year1 and int(line_split[2]) <= year2 and line_split[3] == gender and line_split[4] == state:
            people = people + int(line_split[5])
            xs.append(int(line_split[2]))
            ys.append(int(line_split[5]))
            #break
        
    print(people)
plt.plot(xs,ys)
plt.show