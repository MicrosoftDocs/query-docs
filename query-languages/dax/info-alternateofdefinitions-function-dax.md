---
description: "Learn more about: INFO.ALTERNATEOFDEFINITIONS"
title: "INFO.ALTERNATEOFDEFINITIONS function (DAX)"
author: jeroenterheerdt
---
# INFO.ALTERNATEOFDEFINITIONS

[!INCLUDE[applies-to-query-only](includes/applies-to-query-only.md)]

Returns a table with information about each alternate of definition in the semantic model. This function provides metadata about alternate definitions for model objects.

## Syntax

```dax
INFO.ALTERNATEOFDEFINITIONS ( [<Restriction name>, <Restriction value>], ... )
```

[!INCLUDE[parameters-for-info-dax-functions](includes/parameters-for-info-dax-functions.md)]

## Return value

A table whose columns match the schema rowset for alternate of definitions in the current semantic model.

| Column | Description |
|---|---|
| [ID] | Unique identifier for the alternate of definition object. |
| [ColumnID] | Reference to the column object that has an alternate definition. |
| [BaseColumnID] | Reference to the base column that this alternate definition is derived from. |
| [BaseTableID] | Reference to the base table containing the base column. |
| [Summarization] | The summarization method applied to the alternate definition (e.g., Sum, Count, Average). |

## Remarks

* Can only be ran by users with write permission on the semantic model and not when live connected to the semantic model in Power BI Desktop.
* This function can be used in [DAX queries](/dax/dax-queries), and can't be used in calculations.

## Example

The following DAX query can be run in [DAX query view](/power-bi/transform-model/dax-query-view):

```dax
EVALUATE
	INFO.ALTERNATEOFDEFINITIONS()
```

## Example 2 - DAX query with joins

The following DAX query can be run in [DAX query view](/power-bi/transform-model/dax-query-view):

```dax
EVALUATE
	VAR _AlternateOfDefinitions =
		INFO.ALTERNATEOFDEFINITIONS()

	VAR _Columns = 
		SELECTCOLUMNS(
			INFO.COLUMNS(),
			"ColumnID", [ID],
			"Column Name", [ExplicitName],
			"TableID", [TableID]
		)

	VAR _BaseColumns = 
		SELECTCOLUMNS(
			INFO.COLUMNS(),
			"BaseColumnID", [ID],
			"Base Column Name", [ExplicitName]
		)

	VAR _BaseTables = 
		SELECTCOLUMNS(
			INFO.TABLES(),
			"BaseTableID", [ID],
			"Base Table Name", [Name]
		)

	VAR _CombinedWithColumns =
		NATURALLEFTOUTERJOIN(
			_AlternateOfDefinitions,
			_Columns
		)

	VAR _CombinedWithBaseColumns =
		NATURALLEFTOUTERJOIN(
			_CombinedWithColumns,
			_BaseColumns
		)

	VAR _CombinedWithBaseTables =
		NATURALLEFTOUTERJOIN(
			_CombinedWithBaseColumns,
			_BaseTables
		)

	RETURN
		SELECTCOLUMNS(
			_CombinedWithBaseTables,
			"Column Name", [Column Name],
			"Base Table Name", [Base Table Name],
			"Base Column Name", [Base Column Name],
			"Summarization", [Summarization]
		)
	ORDER BY [Column Name]
```

