import tempfile
import os
import pandas as pd
tempdir = tempfile.gettempdir()
filename = os.path.join(tempdir,'user.cv')
filename_salary = os.path.join(tempdir,'salary.csv')
excel_filename = os.path.join(tempdir,'salary.xlsx')

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

users = pd.concat([user1,user2,user3])
users.to_csv(filename, index = False)
other = pd.read_csv(filename)
url = 'https://raw.github.com/neurospin/pystatsml/master/datasets/salary_table.csv'
salary = pd.read_csv(url)
salary.to_csv(filename_salary,index = False)
read_salary = pd.read_csv(filename_salary)

salary.to_excel(excel_filename, sheet_name='salary', index = False)
read_excel = pd.read_excel(excel_filename, sheet_name ='salary')
print(read_excel)

# xls_filename = os.path.join(tempdir, "users.xlsx")
# users.to_excel(xls_filename, sheet_name='users', index=False)
# print(pd.read_excel(xls_filename, sheet_name='users'))