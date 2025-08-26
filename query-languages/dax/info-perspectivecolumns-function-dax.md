---
description: "Learn more about: INFO.PERSPECTIVECOLUMNS"
title: "INFO.PERSPECTIVECOLUMNS function (DAX)"
author: jeroenterheerdt
---
# INFO.PERSPECTIVECOLUMNS

[!INCLUDE[applies-to-query-only](includes/applies-to-query-only.md)]

Returns a table with information about each perspective column in the semantic model. This function provides metadata about columns included in perspectives.

## Syntax

```dax
INFO.PERSPECTIVECOLUMNS ( [<Restriction name>, <Restriction value>], ... )
```

[!INCLUDE[parameters-for-info-dax-functions](includes/parameters-for-info-dax-functions.md)]

## Return value

A table with the following columns:

| Column | Description |
|--------|-------------|
| [ID] | Unique identifier for the perspective column |
| [PerspectiveTableID] | Identifier of the perspective table containing this column |
| [ColumnID] | Identifier of the column included in the perspective |
| [ModifiedTime] | Timestamp of when the perspective column was last modified |

## Remarks

- Typically used in DAX queries to inspect and document model metadata.
- Permissions required depend on the host. Querying full metadata may require model admin permissions.

## Example

The following DAX query can be run in [DAX query view](/power-bi/transform-model/dax-query-view):

```dax
EVALUATE
	INFO.PERSPECTIVECOLUMNS()
```

## Example 2 - DAX query with joins

The following DAX query can be run in [DAX query view](/power-bi/transform-model/dax-query-view):

```dax
EVALUATE
	VAR _PerspectiveColumns =
		SELECTCOLUMNS(
			INFO.PERSPECTIVECOLUMNS(),
			"PerspectiveColumnID", [ID],
			"PerspectiveTableID", [PerspectiveTableID],
			"ColumnID", [ColumnID]
		)
	VAR _Columns = 
		SELECTCOLUMNS(
			INFO.COLUMNS(),
			"ColumnID", [ID],
			"Column Name", [ExplicitName],
			"TableID", [TableID]
		)
	VAR _Tables = 
		SELECTCOLUMNS(
			INFO.TABLES(),
			"TableID", [ID],
			"Table Name", [Name]
		)
	VAR _CombinedTable1 =
		NATURALLEFTOUTERJOIN(
			_PerspectiveColumns,
			_Columns
		)
	VAR _CombinedTable2 =
		NATURALLEFTOUTERJOIN(
			_CombinedTable1,
			_Tables
		)
	RETURN
		SELECTCOLUMNS(
			_CombinedTable2,
			"Table Name", [Table Name],
			"Column Name", [Column Name],
			"Modified Time", [ModifiedTime]
		)
	ORDER BY [Table Name], [Column Name]
```

## See also

[INFO.PERSPECTIVES](info-perspectives-function-dax.md)
[INFO.PERSPECTIVEHIERARCHIES](info-perspectivehierarchies-function-dax.md)
[INFO.PERSPECTIVEMEASURES](info-perspectivemeasures-function-dax.md)
[INFO.PERSPECTIVETABLES](info-perspectivetables-function-dax.md)
[INFO.TABLES](info-tables-function-dax.md)
