CREATE TABLE [DataSource1].[dbo].[Station_Data]([Station id] [varchar](50) NOT NULL,[Station name] [varchar](max) NOT NULL,[Latitude] [real] NOT NULL,[Longitude] [real] NOT NULL,[Elevation] [real] NOT NULL) 

alter table [DataSource1].[dbo].[Station_Data] add constraint pk_station_id primary key clustered([Station id])

INSERT INTO [DataSource1].[dbo].[Station_Data] SELECT distinct [Station id], [Station name], [Latitude], [Longitude], [Elevation] FROM [DataSource1].[dbo].[Data_Source1]

CREATE TABLE [DataSource1].[dbo].[Weather_data]([Station id] [varchar](50) NOT NULL, [Date] [date] NOT NULL, [prcp] [real] NULL, [T_Avg] [int] NULL, [T_Min] [int] NULL, [T_Max] [int] NULL) 

alter table [DataSource1].[dbo].[Weather_data] add constraint fk_station_id foreign key([Station id]) REFERENCES dbo.[Station_data]([Station id]) ON DELETE CASCADE ON UPDATE CASCADE

INSERT INTO [DataSource1].[dbo].[Weather_Data]([Station id],[Date],[prcp],[T_Avg],[T_Min],[T_Max]) SELECT [Station id],[Date],[PRCP],[TAVG],[TMIN],[TMAX] FROM [DataSource1].[dbo].[Data_Source1]

