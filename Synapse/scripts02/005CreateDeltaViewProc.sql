CREATE PROCEDURE Operation.CreateDeltaView
(
    @QualifiedName NVARCHAR(300),
    @Location NVARCHAR(200)
)
AS 
DECLARE @DropStatement NVARCHAR(MAX) = 'DROP VIEW IF EXISTS '+ @QualifiedName +';'
PRINT (@DropStatement)

EXEC sp_executesql @DropStatement

DECLARE @CreateStatement NVARCHAR(MAX) = 'CREATE VIEW ' + @QualifiedName + ' AS
                                            SELECT * FROM
                                            OPENROWSET(
                                                BULK ''' + @Location + ''',
                                                DATA_SOURCE = ''DataLakeMI'',
                                                FORMAT = ''DELTA''
                                            ) AS [result]'
PRINT (@CreateStatement)

EXEC sp_executesql @CreateStatement
