# Tuples son listas que no pueden ser cambiadas
import numpy as np

x = (1,2,3)
print len(x)

y = (4,5,6)
print y[2]

listofTuples = [x,y]
print listofTuples

(age,income) = "32,120000".split(',')
print age
print income
