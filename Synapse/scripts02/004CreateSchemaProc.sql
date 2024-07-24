CREATE PROCEDURE Operation.CreateSchema
(
    @SchemaName NVARCHAR(300)
)
AS 
IF NOT EXISTS (SELECT  * FROM    sys.schemas WHERE   name = @SchemaName)
    DECLARE @CreateStatement NVARCHAR(MAX) = 'CREATE SCHEMA ' + @SchemaName
    PRINT (@CreateStatement)
    EXEC sp_executesql @CreateStatement
