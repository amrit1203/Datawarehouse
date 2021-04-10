import requests
import csv
import json
import pandas as pd

def filter():
    col_list1 = ["STATION","NAME","LATITUDE","LONGITUDE","ELEVATION","DATE","PRCP","TAVG","TMAX","TMIN"]
    col_list11 = ["STATION","NAME","LATITUDE","LONGITUDE","ELEVATION","DATE", "SNOW", "SNWD","PRCP","TAVG","TMAX","TMIN"]
    col_list2 = ["STATION ID","STATION NAME", "LATITUDE","LONGITUDE","ELEVATION","DATE","PRCP","TAVG","TMAX","TMIN"]
    col_list3 = ["STATIONID","STATIONNAME", "ST_LATITUDE","ST_LONGITUDE","ST_ELEVATION","DATE", "SNOW", "SNWD", "PRCP_VAL","TEMP_AVG","TEMP_MAX","TEMP_MIN"]
   
    df1 = pd.read_csv("NZ2.csv",usecols=col_list1)
    df2 = pd.read_csv("NZ1.csv",usecols=col_list11)

    df1[['STATION NAME','COUNTRY']]= df1['NAME'].str.split(',',expand=True)
    df2[['STATIONNAME','COUNTRY']]= df2['NAME'].str.split(',',expand=True) 


    df1=df1.rename(columns={"STATION": "STATION ID"}) #renaming columns
    df1=df1.filter(col_list2)
    df1.to_csv(r'd1.csv')

    df2=df2.rename(columns={"STATION": "STATIONID", 
        "LATITUDE": "ST_LATITUDE",
        "LONGITUDE": "ST_LONGITUDE",
        "ELEVATION": "ST_ELEVATION",
        "DATE": "DATE",
        "PRCP": "PRCP_VAL",
        "TAVG": "TEMP_AVG",
        "TMAX": "TEMP_MAX",
        "TMIN": "TEMP_MIN"}) #renaming columns
    df2=df2.filter(col_list3)
    df2.to_csv(r'd2.txt')
    
    
filter()
