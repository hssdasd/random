 import pyodbc
     cnxn = pyodbc.connect('DRIVER={FileMaker 

ODBC};SERVER=192.168.1.1:2399;DATABASE=TBS3;UID=USER;PWD=PASSWORD')
     pyodbc.connect
     cursor = cnxn.cursor()
     cursor.execute("select some-column from some-table")
     row = cursor.fetchall()
