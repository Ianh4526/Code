#write some code that creates a list of integers, loops throuh each element of
#list, and only prints out the even numbers

import numpy as np
print "\n   LIST \n "
listofintegers = np.random.random_integers(0,100,100)

print listofintegers

print "\n   Sorting the list "
listofintegers.sort()
print listofintegers

print "\n   Selecting only the Even Numbers "
a=0
for x in listofintegers:
    if x % 2 == 0:
         a +=1
         print x,

print "\n\n Total of numbers is: ", a
print "\n   Done..."
