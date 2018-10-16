import pandas as pd
import tempfile
import os
import matplotlib.pyplot as plt

tempdir = tempfile.gettempdir()
tempfolder = os.path.join(tempdir,'dataframe')
filename = os.path.join(tempfolder,'salary.csv')
try:
    salary  = pd.read_csv(filename)
except:
    url = 'https://raw.github.com/duchesnay/pylearn-doc/master/datasets/salary_table.csv'
    salary = pd.read_csv(url)
df = salary
colors = colors_edu = {'Bachelor':'r', 'Master':'g', 'Ph.D':'b'}
plt.scatter(df['experience'],df['salary'],c= df['education'].apply(lambda x: colors[x]),s = 100)
plt.xlabel('Experience')
plt.ylabel('Salary')
plt.show()
