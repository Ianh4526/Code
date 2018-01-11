
#Extract 5-10 rows from our dataframe
#using only Previus Employers and Hired columns
#Assign to a new DataFrame
#Create a Histogram (Bar plot) of the previus employers in this subset of data.

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv("PastHires.csv")
#print df.head(10)

newDataframe = df[['Previous employers','Hired']][5:10]
#print newDataframe

previousEmployer_distr = newDataframe['Previous employers'].value_counts()


#print previousEmployer_distr

previousEmployer_distr.plot(kind='bar')

plt.show()
