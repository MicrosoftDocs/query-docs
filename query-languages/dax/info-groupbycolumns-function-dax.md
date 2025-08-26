---
description: "Learn more about: INFO.GROUPBYCOLUMNS"
title: "INFO.GROUPBYCOLUMNS function (DAX)"
author: jeroenterheerdt
---
# INFO.GROUPBYCOLUMNS

[!INCLUDE[applies-to-query-only](includes/applies-to-query-only.md)]

Returns a table with information about each group by column in the semantic model. This function provides metadata about columns used in group by operations.

## Syntax

```dax
INFO.GROUPBYCOLUMNS ( [<Restriction name>, <Restriction value>], ... )
```

[!INCLUDE[parameters-for-info-dax-functions](includes/parameters-for-info-dax-functions.md)]

## Return value

A table with the following columns:

| Column | Description |
|--------|-------------|
| [ID] | Unique identifier for the group by column |
| [RelatedColumnDetailsID] | Identifier linking to related column details |
| [GroupingColumnID] | Identifier of the column used for grouping operations |
| [ModifiedTime] | Timestamp of when the group by column was last modified |

## Remarks

- Typically used in DAX queries to inspect and document model metadata.
- Permissions required depend on the host. Querying full metadata may require model admin permissions.

## Example

The following DAX query can be run in [DAX query view](/power-bi/transform-model/dax-query-view):

```dax
EVALUATE
	INFO.GROUPBYCOLUMNS()
```

## Example 2 - DAX query with joins

The following DAX query can be run in [DAX query view](/power-bi/transform-model/dax-query-view):

```dax
EVALUATE
	VAR _GroupByColumns =
		SELECTCOLUMNS(
			INFO.GROUPBYCOLUMNS(),
			"GroupByColumnID", [ID],
			"GroupingColumnID", [GroupingColumnID],
			"RelatedColumnDetailsID", [RelatedColumnDetailsID]
		)
	VAR _Columns = 
		SELECTCOLUMNS(
			INFO.COLUMNS(),
			"ColumnID", [ID],
			"Column Name", [ExplicitName]
		)
	VAR _CombinedTable =
		NATURALLEFTOUTERJOIN(
			_GroupByColumns,
			ADDCOLUMNS(
				_Columns,
				"GroupingColumnID", [ColumnID]
			)
		)
	RETURN
		SELECTCOLUMNS(
			_CombinedTable,
			"Column Name", [Column Name],
			"Modified Time", [ModifiedTime]
		)
	ORDER BY [Column Name]
```

## See also

[INFO.TABLES](info-tables-function-dax.md)
[INFO.COLUMNS](info-columns-function-dax.md)
[INFO.MEASURES](info-measures-function-dax.md)
[INFO functions overview](info-functions-dax.md)
