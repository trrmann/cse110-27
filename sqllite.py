import sqlite3
import pandas as pd

conn = sqlite3.connect('test_database') 
c = conn.cursor()

c.execute('''
          CREATE TABLE IF NOT EXISTS products
          ([product_id] INTEGER PRIMARY KEY, [product_name] TEXT)
          ''')
          
c.execute('''
          CREATE TABLE IF NOT EXISTS prices
          ([product_id] INTEGER PRIMARY KEY, [price] INTEGER)
          ''')
                     
conn.commit()

conn = sqlite3.connect('test_database')

sql_query = pd.read_sql_query('''
            SELECT * FROM system_options
          ''', conn)

df = pd.DataFrame(sql_query, columns = ['',''])
print(df)