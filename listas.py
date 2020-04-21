# -*- coding: utf-8 -*-
"""
Created on Thu Oct  4 21:21:11 2018

@author: Krisag
"""
import matplotlib.pyplot as plt

gente = ["Pepe","Pecas","Pica","Papas"]
print (gente.pop())
print (gente.append("Papas"))
print (gente[-1])
print (gente[-2])
print (gente[-3:])
################################################
xs = [0,1,2,3,4,5,6,7,8,9]
#ys = []
#for x in xs:
#    ys.append(x*x)
ys = [x * x for x in xs]

print(xs)
print(ys)
plt.plot(xs, ys)
#mas preciso
xs = [x / 10 for x in range(0,100)]
ys = [x * x for x in xs]

plt.plot(xs, ys)
plt.show