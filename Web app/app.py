from flask import Flask, redirect, url_for, render_template, request, session
import json 
import pymongo
import query
app = Flask(__name__)
# -------- extract data and sent to frontend ---------------------------------------------------------- #

@app.route('/', methods=['GET', 'POST'])
def mainfun():
    
    NZ=query.result("SELECT dm.[year_num] as [YEAR], SUM(fw.PRCP) as [TOTAL Precipitation] FROM [dbo].[FactWeather] as fw inner join [dbo].[Date_dim] as dm on fw.[Date] =  dm.[Date] where fw.Country='NZ' OR fw.Country='US' GROUP BY dm.[year_num] ORDER BY dm.[year_num]")
    US=query.result("SELECT dm.[year_num] as [YEAR], MAX(fw.TMAX) as [Maximum Temperature] FROM [dbo].[FactWeather] as fw inner join [dbo].[Date_dim] as dm on fw.[Date] =  dm.[Date] where fw.Country='US' GROUP BY dm.[year_num] ORDER BY dm.[year_num]")
   
    return render_template('index.html', graph1= NZ, graph2= US)
# ======== Main ============================================================== #
if __name__ == "__main__":
    app.run(debug=True, use_reloader=True, port=5001)
