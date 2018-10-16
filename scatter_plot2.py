import pandas as pd
import matplotlib.pyplot as plt
import os
import tempfile

tempdir = tempfile.gettempdir()
tempfolder = os.path.join(tempdir, 'dataframe')
filename = os.path.join(tempfolder,'salary.csv')

try:
    salary = pd.read_csv(filename)
except:
    print('Fail to read from source file')
df = salary
plt.figure(figsize=(6,5))
symbol_manag = dict(Y = '*', N = '.')
colors_edu = {'Bachelor':'r', 'Master':'g','Ph.D':'b'}
for values, d in salary.groupby(['education','management']):
    edu, manager = values
    plt.scatter(d['experience'], d['salary'],marker= symbol_manag[manager],color = colors_edu[edu], s = 150, label = manager+'/'+edu)
plt.xlabel('Experience')
plt.ylabel('Salary')
plt.title('A graph of lecturers salaries against experience')
plt.legend(loc = 4)
plt.savefig('scatter.svg')
plt.show()
