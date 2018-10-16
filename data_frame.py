import pandas as pd
import numpy as py

columns = ['name', 'age', 'gender', 'job']

user1 = pd.DataFrame([['Hashim',26,'Male','Developer']],columns = columns)
user2 = pd.DataFrame([['Ashir',26,'Male','Student']],columns = columns)
user3 = pd.DataFrame([['Aliyu',25,'Male','Student']],columns = columns)
user4 = pd.DataFrame([['Yusuf',26,'Male','Business']],columns = columns)
user5 = pd.DataFrame([['Ibrahim',25,'Male','Business']],columns = columns)
user6 = pd.DataFrame([['Abdul',22,'Male','Student']],columns = columns)
user7 = pd.DataFrame([['Umar',22,'Male','Student']],columns = columns)
#concatenation  operation
users = pd.concat([user1,user2,user3,user4,user5,user6,user7])

users_height = pd.DataFrame(dict(name=['Hashim','Ashir','Ibrahim','Yusuf','Aliyu'],height=[189,179,175,180,172]))

#intersection operation
user_intersection = pd.merge(users,users_height,on='name')

#union operation
user_union = pd.merge(users,users_height, on='name',how='outer')

#Row selection
df = user_union.copy()
user = df.iloc[0] #first row
item = df.iloc[0,0] #first item on first row

#sorting
sort_by_age = df.sort_values('age')
#descending order
sort_by_name = df.sort_values('name', ascending= False)

#descriptive statistics
df.describe()
df.describe(include = 'all')
df.describe(include = ['object'])

df.groupby('job').mean()
df.groupby('age')['height'].mean()
df.groupby('job').describe(include='all')

#remove duplicate
df.append(df.iloc[0], ignore_index = True)
#True if a row is identical to a previous one
df.duplicated()     
#count of duplicates
df.duplicated().sum()
#check a single column for duplicates
df.age.duplicated()
#specify columns for finding duplicate
df.duplicated(['age','gender']).sum()

#drop duplicates row
df.drop_duplicates()

#File I/O
import tempfile
import os

tempdir = tempfile.gettempdir()
folder_name = os.path.join(tempdir,'dataframe')
if not os.path.exists(folder_name):
    os.mkdir(folder_name)
file_name = os.path.join(folder_name,'users.csv')
users.to_csv(file_name,index = False)
read = pd.read_csv(file_name)

#Excel
excel_file = os.path.join(folder_name,'user.xlsx')
users.to_excel(excel_file,sheet_name = 'user',index = False)

pd.read_excel(excel_file, sheet_name='user')


#SQLite
import sqlite3
database_name = os.path.join(folder_name,'user.db')

conn = sqlite3.connect(database_name)

users.to_sql('users',conn,if_exists='replace')

cur = conn.cursor();
values = [100,'Ismail',21,'Male','Student']
cur.execute('INSERT INTO users VALUES(?,?,?,?,?) ',values)
conn.commit()

users_from_db = pd.read_sql_query('SELECT *FROM users',conn)
print(users_from_db)