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
cursor.execute("SELECT name from inventory order by id;") 
row = cursor.fetchone() 
while row: 
    print(row[0])
    row = cursor.fetchone()

# cursor.execute('''
#                 INSERT INTO TestDB.dbo.Inventory (id, name, quantity)
#                 VALUES
#                 (6,' APPLE',125),
#                 (7,' PEAR',135)
#                 ''')
# cnxn.commit()