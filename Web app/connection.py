import pyodbc 
def connection(Database):
    conn = pyodbc.connect('Driver={SQL Server};'
                          'Server=DESKTOP-ETNCNUD;' 
                          'Database='+Database+';'
                          'Trusted_Connection=yes;',
                          autocommit=True)
    cursor = conn.cursor()
    return cursor
