#import pyodbc 
#conn = pyodbc.connect('Driver={SQL Server};'
#                      'Server=192.168.0.2;'
#                      'Database=TestDB;'
#                      'username = sa;' 
#                      'password = Simon123;'
#                      'Trusted_Connection=yes;')
#
#cursor = conn.cursor()
#cursor.execute('SELECT * FROM TestDB.Inventory')
#
#for row in cursor:
#    print(row)
#
import pyodbc 
# Some other example server values are
# server = 'localhost\sqlexpress' # for a named instance
# server = 'myserver,port' # to specify an alternate port
server = '192.168.0.2' 
database = 'TestDB'
username = 'sa' 
password = 'Simon123' 
cnxn = pyodbc.connect('DRIVER={SQL SERVER};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()

#Sample select query
cursor.execute("SELECT name from inventory;") 
row = cursor.fetchone() 
while row: 
    print(row[0])
    row = cursor.fetchone()


  