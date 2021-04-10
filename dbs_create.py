from connection import connection

def db_create():

    cursor = connection("Master")
    inputdir = '.\DB_Creation.sql' 

    with open(inputdir,'r') as dbc:
        statement = dbc.readlines()
        for db in statement:
            db = db.strip('\n')
            cursor.execute(db)
        
        