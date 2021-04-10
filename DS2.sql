CREATE TABLE [DataSource2].[dbo].[Station]([StationId] [varchar](50) NOT NULL, [StationName] [varchar](max) NOT NULL, [Lat] [real] NOT NULL, [Long] [real] NOT NULL, [Elevation] [real] NOT NULL)

alter table [DataSource2].[dbo].[Station] add constraint pk_station_id primary key clustered(StationId)

INSERT INTO [DataSource2].[dbo].[Station] SELECT distinct [StationId],[StationName],[Lat],[Long], [Elevation] FROM [DataSource2].[dbo].[Data_Source2]

CREATE TABLE [dbo].[Weather]([StationId] [varchar](50) NOT NULL, [Date] [date] NOT NULL, [Pres] [real] NULL,[TAvg] [int] NULL, [TMin] [int] NULL,[TMax] [int] NULL)

alter table [DataSource2].[dbo].[Weather] add constraint fk_station_id foreign key([StationId]) REFERENCES [DataSource2].[dbo].[Station]([StationId]) ON DELETE CASCADE ON UPDATE CASCADE

INSERT INTO [DataSource2].[dbo].[Weather]([StationId],[Date],[Pres],[TAvg],[TMin],[TMax]) SELECT [StationId],[Date],[Pres],[T_Average],[T_Min],[T_Max] FROM [DataSource2].[dbo].[Data_Source2]

