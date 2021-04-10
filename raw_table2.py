from connection import connection

def ds2_create():
    cursor = connection("DataSource2")
    inputdir = '.\WDS2.sql' 

    with open(inputdir,'r') as dbc:
        dbs = dbc.readlines()
        dbs = dbs[0].split('\n')
        cursor.execute(dbs[0])
