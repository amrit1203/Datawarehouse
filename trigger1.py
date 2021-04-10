from connection import connection

def ds_trigger1():
    cursor = connection("DataSource1")
    inputdir = 'trigger.sql' 

    with open(inputdir,'r') as dbc:
        dbs = dbc.read()
        cursor.execute(dbs)

    inputdir = 'trigger_s1.sql'
    with open(inputdir,'r') as dbc:
        dbs = dbc.read()
        cursor.execute(dbs)


