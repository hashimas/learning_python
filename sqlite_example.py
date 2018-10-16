import pandas as pd
import sqlite3
import tempfile
import os

tempdir = tempfile.gettempdir()
user_folder = os.path.join(tempdir,'user')
if not os.path.exists(user_folder):
    os.mkdir(user_folder)
database_name = os.path.join(user_folder,'users.db')

conn = sqlite3.connect(database_name)

# url = 'https://raw.github.com/neurospin/pystatsml/master/datasets/salary_table.csv'
# read_salary = pd.read_csv(url)
# read_salary.to_sql('salary',conn,if_exists='replace')

cur = conn.cursor();
values = (100, 1400, 5, 'Bachelor', 'N')
cur.execute('insert into salary values (?, ?, ?, ?, ?)', values)
conn.commit()

read_salary = pd.read_sql_query('select *from salary',conn)
print(read_salary)


