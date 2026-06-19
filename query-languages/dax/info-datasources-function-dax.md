---
description: "Learn more about: INFO.DATASOURCES"
title: "INFO.DATASOURCES function (DAX)"
author: jeroenterheerdt
---
# INFO.DATASOURCES

[!INCLUDE[applies-to-query-only](includes/applies-to-query-only.md)]

Returns a table with information about each data source in the semantic model. This function provides metadata about the data sources connected to the model.

## Syntax

```dax
INFO.DATASOURCES ( [<Restriction name>, <Restriction value>], ... )
```

[!INCLUDE[parameters-for-info-dax-functions](includes/parameters-for-info-dax-functions.md)]

## Return value

A table with the following columns:

| Column name | Data type | Description |
| --- | --- | --- |
| [ID] | Integer | Unique identifier for the data source |
| [ModelID] | Integer | Identifier of the semantic model |
| [Name] | String | Name of the data source |
| [Description] | String | Description of the data source |
| [Type] | String | Type of the data source |
| [ConnectionString] | String | Connection string for the data source |
| [ImpersonationMode] | String | Impersonation mode used for the data source |
| [Account] | String | Account used for impersonation |
| [Password] | String | Password for the data source (typically masked) |
| [MaxConnections] | Integer | Maximum number of connections allowed |
| [Isolation] | String | Isolation level for the data source |
| [Timeout] | Integer | Timeout value for connections |
| [Provider] | String | Data provider for the data source |
| [ModifiedTime] | DateTime | Date and time when the data source was last modified |
| [ConnectionDetails] | String | Additional connection details |
| [Options] | String | Additional options for the data source |
| [Credential] | String | Credential information |
| [ContextExpression] | String | Context expression for the data source |

## Remarks

- Typically used in DAX queries to inspect and document model metadata.
- Permissions required depend on the host. Querying full metadata may require model admin permissions.

## Example

The following DAX query can be run in [DAX query view](/power-bi/transform-model/dax-query-view):

```dax
EVALUATE
	INFO.DATASOURCES()
```

## Example 2 - DAX query with joins

The following DAX query can be run in [DAX query view](/power-bi/transform-model/dax-query-view):

```dax
EVALUATE
	VAR _DataSources =
		INFO.DATASOURCES()

	VAR _Model = 
		SELECTCOLUMNS(
			INFO.MODEL(),
			"ModelID", [ID],
			"Model Name", [Name]
		)

	VAR _CombinedTable =
		NATURALLEFTOUTERJOIN(
			_DataSources,
			_Model
		)

	RETURN
		SELECTCOLUMNS(
			_CombinedTable,
			"Model Name", [Model Name],
			"Data Source Name", [Name],
			"Data Source Type", [Type],
			"Max Connections", [MaxConnections],
			"Modified Time", [ModifiedTime]
		)
	ORDER BY [Data Source Name]
```
## See also

- [INFO.TABLES](info-tables-function-dax.md)
- [INFO.COLUMNS](info-columns-function-dax.md)
- [INFO.MEASURES](info-measures-function-dax.md)
- [INFO functions overview](info-functions-dax.md)
