import pyodbc

# conn = pyodbc.connect('driver={sql server};' 
#                       'server=server_name;'
#                       'database=database_name;'
#                       'trusted_connection=yes;')

# cursor = conn.cursor()
# cursor.execute('select * from table_name')

# for i in cursor:
#     print(i)


#select @@servername

conn = pyodbc.connect('driver={sql server};' 
                      'server=gvx0wcopd08p;'
                      'database=logixrt;'
                      'uid="copient_logix";'
                      'pwd="app0mattox";'
                      'trusted_connection=yes;')

cursor = conn.cursor()
cursor.execute('select @@servername')

for i in cursor:
    print(i)

cursor.execute('select name from sys.sysdatabases')

for i in cursor:
    print(i)

cursor.execute('SELECT object_id, name FROM sys.Tables')

for i in cursor:
    print(i)

cursor.execute('SELECT name FROM sys.Tables WHERE name = \'SystemOptions\'')

for i in cursor:
    print(i)

cursor.execute('SELECT c.name FROM sys.columns c, sys.Tables t WHERE t.name = \'SystemOptions\' and c.object_id = t.object_id')

for i in cursor:
    print(i)

cursor.execute('SELECT * FROM systemoptions')

for i in cursor:
    print(i)

