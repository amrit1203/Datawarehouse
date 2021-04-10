from connection import connection

def ds2_trigger():
    cursor = connection("DataSource2")
    inputdir = 'trigger2.sql' 

    with open(inputdir,'r') as dbc:
        dbs = dbc.read()
        cursor.execute(dbs)

    inputdir = 'trigger_s2.sql' 

    with open(inputdir,'r') as dbc:
        dbs = dbc.read()
        cursor.execute(dbs)
