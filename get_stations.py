from connection import connection

def get_us_stations():
    cursor = connection("DataWarehouse")
    cursor.execute("SELECT [Station id] FROM [DataWarehouse].[dbo].[Station] where [Station id] like 'US%' ")
    row = cursor.fetchone()
    stations = []
    while row:
        stations.append(row[0])
        row = cursor.fetchone()

    return stations


def get_nz_stations():
    cursor = connection("DataWarehouse")
    cursor.execute("SELECT [Station id] FROM [DataWarehouse].[dbo].[Station] where [Station id] like 'NZ%' ")
    row = cursor.fetchone()
    stations = []
    while row:
        stations.append(row[0])
        row = cursor.fetchone()

    return stations