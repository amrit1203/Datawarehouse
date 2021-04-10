from connection import connection

def dw_insert():
    cursor = connection("DataSource1")
    inputdir = '.\DW_insert.sql' 

    with open(inputdir,'r') as dbc:
        dbs = dbc.readlines()
        for db in dbs:
            db = db.split('\n')
            if db[0]:
                print(db[0])
                cursor.execute(db[0])
