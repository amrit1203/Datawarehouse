import requests
import csv
import json
import pandas as pd
import math
from connection import connection

def ds2_insert():
    col_list = ["STATION ID","STATION NAME", "LATITUDE","LONGITUDE","ELEVATION","DATE","PRCP","TAVG","TMAX","TMIN"]
    cursor = connection("DataSource2")
    df = pd.read_csv("d2.csv")
    df.columns = [c.replace(' ', '_') for c in df.columns]
    df['PRCP'] = df['PRCP'].fillna(0.0).astype(float)
    df['TAVG'] = df['TAVG'].fillna(0).astype(int)
    df['TMAX'] = df['TMAX'].fillna(0).astype(int)
    df['TMIN'] = df['TMIN'].fillna(0).astype(int)
    for row in df.itertuples(index=True, name='Pandas'):
        STATION_ID = str(row.STATION_ID)
        STATION_NAME = str(row.STATION_NAME)
        LATITUDE = str(row.LATITUDE)
        LONGITUDE = str(row.LONGITUDE)
        ELEVATION = str(row.ELEVATION)
        DATE = str(row.DATE)
        PRCP = row.PRCP if row.PRCP else None
        TAVG = row.TAVG if row.TAVG else None
        TMAX = row.TMAX if row.TMAX else None
        TMIN = row.TMIN if row.TMIN else None
        cursor.execute("INSERT INTO DataSource2.dbo.Data_Source2 VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                STATION_ID, STATION_NAME, LATITUDE, LONGITUDE, ELEVATION, DATE, PRCP, TAVG, TMAX, TMIN )
