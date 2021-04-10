CREATE TABLE [Datawarehouse].[dbo].[Station]([Station id] [varchar](50) NOT NULL,[Station Name] [varchar](MAX) NOT NULL,[Latitude] [real] NOT NULL,[Longitude] [real] NOT NULL,[Elevation] [real] NOT NULL) 

alter table [Datawarehouse].[dbo].[Station] add constraint pk_dw_station_id primary key clustered([Station id])

CREATE TABLE [Datawarehouse].[dbo].[Date_dim]([Date] [date] NOT NULL,[Date_num] [int] NOT NULL,[month_num] [int] NULL,[year_num] [int] NULL) 

alter table [Datawarehouse].[dbo].[Date_dim] add constraint pk_dw_date primary key clustered([Date])

CREATE TABLE [Datawarehouse].[dbo].[FactWeather]([Station id] [varchar](50) NOT NULL,[Date] [date] NOT NULL,[Country] [varchar](50) NOT NULL,[PRCP] [real],[TAVG] [int],[TMIN] [int],[TMAX] [int]) 

alter table [Datawarehouse].[dbo].[FactWeather] add constraint fk_dw_station_id foreign key([Station id]) REFERENCES dbo.[Station]([Station id]) ON DELETE CASCADE ON UPDATE CASCADE

alter table [Datawarehouse].[dbo].[FactWeather] add constraint fk_dw_date foreign key([Date]) REFERENCES dbo.[Date_dim]([Date]) ON DELETE CASCADE ON UPDATE CASCADE

