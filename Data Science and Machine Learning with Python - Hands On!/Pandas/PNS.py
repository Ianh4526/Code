# Pandas
#Data Frames and Series

#NumPy
#Arrays

#Scikit_learn
#Machine learning library

#%matplotlib inline
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv("PastHires.csv")
print df.head()
#Print the first 5 rows

print df.head(10)
#Print the first 10 rows

print df.tail(4)
#print last 4 rows

print "\nthe dimensions of the data frame rows *columns"
print df.shape

print "\n#Number of cells"
print df.size

print "\n#number of rows"
print len(df)

print "\n#array of columns names"
print df.columns

print "\nSingle column HIRED"
print df['Hired']

print "\n5 rows of the Hired Columns a given range == a Serie"
print df['Hired'][:5]

print "\nSingle value of especific column"
print df['Hired'][5]

print "\nExtrat more than one column"
print df[['Years Experience','Hired']]

print "\nExtrat specific range"
print df[['Years Experience','Hired']][:5]

print "\nSorting by specific Column"
print df.sort_values(['Years Experience'])

print "\nValue count Series"
degree_counts = df['Level of Education'].value_counts()
print degree_counts

degree_counts.plot(kind='bar')

#plt.grid(1)
plt.show()
