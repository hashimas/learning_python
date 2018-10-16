from __future__ import print_function
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

columns = ['Name','Age','Gender','Job']

user1 = pd.DataFrame([['Hashim',26,'Male','Student'],
                    ['Ashir',26,'Male','Student']],
                    columns=columns)
user2 = pd.DataFrame([['Yusuf',26,'Male','Businessman'],
                    ['Ibrahim',25,'Male','Businessman']],
                    columns = columns)
user3 = pd.DataFrame([['Aliyu',25,'Male','Student'],
                    ['Abdul',22,'Male','Businessman']],
                    columns = columns)
# user1.append(user2)
user = pd.concat([user1,user2,user3])
dictionary = dict(Name=['Hashim','Ibrahim','Yusuf','Ashir'],height =[179,167,175,170])
user4 = pd.DataFrame(dictionary)
merge_intersection = pd.merge(user,user4, on='Name')
merge_union = pd.merge(user,user4, on='Name', how='outer')
print(merge_intersection)
print()
print(merge_union)
print()

# n = np.linspace(0, 1, 5)
# n2 = np.logspace(0,3,4)
# a = np.array([0,1])
# b = np.array([2,3])
# ab = np.stack((a,b)).T

stacked = pd.melt(merge_union,id_vars= 'Name',var_name='variable',value_name='value')
print(stacked)
print()
print(stacked.pivot(index ='Name',columns='variable',values='value'))
print()

df = user.copy();
print(df.groupby('Job').describe(include='all'))