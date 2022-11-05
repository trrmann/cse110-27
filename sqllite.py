#!python
import os
import pyodbc
import sqlite3
import pandas as pd

server = "gvx0wcopd08p.us.royalahold.net"
db = "LogixRT"
table = "Integrations"
table = "UE_SystemOptions"
table = "LocalServers"
table = "CPE_SystemOptions"
table = "SystemOptions"
uid = "copient_logix"
pwd = "app0mattox"

conn = pyodbc.connect('driver={sql server};' 
                      f'server={server};'  
                      f'database={db};'
                      f'uid="{uid}";'
                      f'pwd="{pwd}";'
                      'trusted_connection=yes;')

tables = {}
table_list = ["Integrations", "UE_SystemOptions", "LocalServers", "CPE_SystemOptions", "SystemOptions"]

cursor = conn.cursor()
cursor.execute('select @@servername')
for table in table_list:
  cursor.execute(f'SELECT c.name, y.name, (c.max_length/2) max_length FROM sys.columns c, sys.Tables t, sys.types y WHERE t.name = \'{table}\' and c.object_id = t.object_id and c.user_type_id = y.user_type_id')  
  columns = []
  types = []
  for i in cursor:
    columns.append(i[0])
    match i[1]:
      case "bit":
        types.append(f"{i[1]}")
      case "int":
        types.append(f"{i[1]}")
      case "bigint":
        types.append(f"{i[1]}")
      case "datetime":
        types.append(f"{i[1]}")
      case "nvarchar":
        types.append(f"{i[1]}({i[2]})")
      case _:
        types.append(f"{i[1]}({i[2]})")
  tables[table] = {}
  tables[table]["columns"] = columns
  tables[table]["types"] = types
  sql_columns = ""
  create_sql_columns = ""
  for index, column in enumerate(tables[table]["columns"]):
    match tables[table]["types"][index]:
      case "int":
        type = "INTEGER"
      case _:
        type = "TEXT"
    if index < len(tables[table]["columns"]) - 1:
      sql_columns = f"{sql_columns}{column}, "
      create_sql_columns = f"{create_sql_columns}[{column}] {type}, "
    else:
      sql_columns = f"{sql_columns}{column}"
      create_sql_columns = f"{create_sql_columns}[{column}] {type}"
  tables[table]["sql_columns"] = sql_columns
  tables[table]["create_sql_columns"] = create_sql_columns
  cursor.execute(f'SELECT {sql_columns} FROM {table}')
  data = {}
  for index, element_data in enumerate(cursor):
    data[index] = {}
    for id, element in enumerate(element_data):
      data[index][tables[table]["columns"][id]]=element
  tables[table]["data"] = data

for table in table_list:
  print("\n\n")
  print(table)
  print(tables[table]["columns"])
  print(tables[table]["types"])
  print(tables[table]["sql_columns"])
  print(tables[table]["create_sql_columns"])
print("\n\n")

conn = sqlite3.connect('test_database') 
c = conn.cursor()
for table in tables.keys():
  c.execute(f'CREATE TABLE IF NOT EXISTS {table} ({tables[table]["create_sql_columns"]})')
  print(f"create {table}")
conn.commit()
print("\n")

conn = sqlite3.connect('test_database')
for table in tables.keys():
  print(f"\nread {table}")
  sql_query = pd.read_sql_query(f'''
            SELECT * FROM {table}
          ''', conn)
#  df = pd.DataFrame(sql_query, columns = ['',''])
  df = pd.DataFrame(sql_query, columns = tables[table]["columns"])

  print(f"1 - {df}")
print("\n")

conn = sqlite3.connect('test_database') 
c = conn.cursor()
for table in tables.keys():
  sql_insert = f"INSERT INTO {table} ({tables[table]['sql_columns']}) VALUES "
  print(sql_insert)
  for id, key in enumerate(tables[table]["data"].keys()):
    #print(f"{tables[table]['data'][id]}")
    record = "("
    for index, column in enumerate(tables[table]["columns"]):
      if index < len(tables[table]["columns"]) - 1: separator=", "
      else: separator=""
      match tables[table]["types"][index]:
        case "int":
#          print(f"{column} {tables[table]['types'][index]} {tables[table]['data'][id][column]}{separator} ", end="")
          if tables[table]['data'][id][column] == None:
            record = f"{record}NULL{separator}"
          else:
            record = f"{record}{tables[table]['data'][id][column]}{separator}"
        case _:
#          print(f"{column} {tables[table]['types'][index]} \'{tables[table]['data'][id][column]}\'{separator} ", end="")
          if tables[table]['data'][id][column] == None:
            record = f"{record}NULL{separator}"
          else:
            record = f"{record}\'{tables[table]['data'][id][column]}\'{separator}"
    record = f"{record})"
#    print()
    if id == len(tables[table]["data"].keys()) - 1:
      sql_insert = f"{sql_insert} {record}"
    else:
      sql_insert = f"{sql_insert} {record},"
      pass
  try:
    c.execute(sql_insert)
  except sqlite3.OperationalError as err:
    print(err)
    print(sql_insert)
  print(f"load {table}")
conn.commit()
print("\n")

conn = sqlite3.connect('test_database')
for table in tables.keys():
  print(f"\nread {table}")
  sql_query = pd.read_sql_query(f'''
            SELECT * FROM {table}
          ''', conn)
#  df = pd.DataFrame(sql_query, columns = ['',''])
  df = pd.DataFrame(sql_query, columns = tables[table]["columns"])
  print(f"1 - {df}")
print("\n")

conn = sqlite3.connect('test_database') 
c = conn.cursor()
for table in tables.keys():
  c.execute(f'DROP TABLE {table}')
  print(f"drop {table}")
conn.commit()
print("\n")

conn = sqlite3.connect('test_database')
for table in tables.keys():
  try:
    sql_query = pd.read_sql_query(f'''
              SELECT * FROM {table}
            ''', conn)
  #  df = pd.DataFrame(sql_query, columns = ['',''])
    df = pd.DataFrame(sql_query, columns = tables[table]["columns"])
    print(f"2 - {df}")
  except pd.errors.DatabaseError as err:
    print(f"{err.strerror} --> ", end="")
  finally:
    print(f"{table}")
print("\n")
