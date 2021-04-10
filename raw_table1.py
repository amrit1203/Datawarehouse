from connection import connection

def ds1_create():
    cursor = connection("DataSource1")
    inputdir = '.\WDS1.sql' 

    with open(inputdir,'r') as dbc:
        dbs = dbc.readlines()
        dbs = dbs[0].split('\n')
        cursor.execute(dbs[0])
