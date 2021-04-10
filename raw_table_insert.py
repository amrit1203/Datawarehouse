import requests
import csv
import json
import pandas as pd
import math
from connection import connection

def ds1_insert():
    col_list = ["STATIONID","STATIONNAME", "ST_LATITUDE","ST_LONGITUDE","ST_ELEVATION","DATE", "SNOW", "SNWD", "PRCP_VAL","TEMP_AVG","TEMP_MAX","TEMP_MIN"]
    cursor = connection("DataSource1")
    df = pd.read_csv("d1.txt")
    df['SNWD'] = df['SNWD'].fillna(0.0).astype(float)
    df['SNOW'] = df['SNOW'].fillna(0.0).astype(float)
    df['PRCP_VAL'] = df['PRCP_VAL'].fillna(0.0).astype(float)
    df['TEMP_AVG'] = df['TEMP_AVG'].fillna(0).astype(int)
    df['TEMP_MAX'] = df['TEMP_MAX'].fillna(0).astype(int)
    df['TEMP_MIN'] = df['TEMP_MIN'].fillna(0).astype(int)
    for row in df.itertuples(index=True, name='Pandas'):
        STATIONID = str(row.STATIONID)
        STATIONNAME = str(row.STATIONNAME)
        ST_LATITUDE = str(row.ST_LATITUDE)
        ST_LONGITUDE = str(row.ST_LONGITUDE)
        ST_ELEVATION = str(row.ST_ELEVATION)
        DATE = str(row.DATE)
        SNOW = row.SNOW if row.SNOW else None
        SNWD = row.SNWD if row.SNWD else None
        PRCP_VAL = row.PRCP_VAL if row.PRCP_VAL else None
        TEMP_AVG = row.TEMP_AVG if row.TEMP_AVG else None
        TEMP_MAX = row.TEMP_MAX if row.TEMP_MAX else None
        TEMP_MIN = row.TEMP_MIN if row.TEMP_MIN else None
        cursor.execute("INSERT INTO DataSource1.dbo.Data_Source1 VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                STATIONID, STATIONNAME, ST_LATITUDE, ST_LONGITUDE, ST_ELEVATION, DATE, SNOW, SNWD, PRCP_VAL, TEMP_AVG, TEMP_MAX, TEMP_MIN )
