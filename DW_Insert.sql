INSERT INTO [Datawarehouse].[dbo].[Station] SELECT [Station id], [Station Name], [Latitude], [Longitude], [Elevation] FROM [DataSource1].[dbo].[Station_Data] UNION SELECT [StationId], [StationName], [Lat], [Long], [Elevation] FROM [DataSource2].[dbo].[Station]

INSERT INTO [Datawarehouse].[dbo].[Date_dim] SELECT [Date],DATEPART(day, [Date]),MONTH([Date]), YEAR([Date]) FROM [DataSource1].[dbo].[Weather_Data] UNION SELECT [Date], DATEPART(day, [Date]), MONTH([Date]), YEAR([Date]) FROM [DataSource2].[dbo].[Weather]

INSERT INTO [Datawarehouse].[dbo].[FactWeather] SELECT [Station id],[Date],'US',[PRCP],[T_Avg],[T_Min],[T_Max] FROM [DataSource1].[dbo].[Weather_data] UNION SELECT [StationId],[Date],'NZ',[Pres],[TAvg],[TMin],[TMax] FROM [DataSource2].[dbo].[Weather]
