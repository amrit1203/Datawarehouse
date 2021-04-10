import requests
import csv
import json
import pandas as pd
import math
from connection import connection

def result(query):
    cursor=connection("Datawarehouse")
    cursor.execute(query)
    result_set = cursor.fetchall()
    L=[]
    for row in result_set:
        L.append(list(row))
    return L

