---
description: "Learn more about: INFO.CALCULATIONITEMS"
title: "INFO.CALCULATIONITEMS function (DAX)"
author: jeroenterheerdt
---
# INFO.CALCULATIONITEMS

[!INCLUDE[applies-to-query-only](includes/applies-to-query-only.md)]

Returns a table with information about each calculation item in the semantic model. This function provides metadata about calculation items within calculation groups.

## Syntax

```dax
INFO.CALCULATIONITEMS ( [<Restriction name>, <Restriction value>], ... )
```

[!INCLUDE[parameters-for-info-dax-functions](includes/parameters-for-info-dax-functions.md)]

## Return value

A table with the following columns:

| Column name | Data type | Description |
| --- | --- | --- |
| [ID] | Integer | The unique identifier of the calculation item |
| [CalculationGroupID] | Integer | The unique identifier of the calculation group that contains this calculation item |
| [FormatStringDefinition] | String | The format string definition for the calculation item |
| [Name] | String | The name of the calculation item |
| [Description] | String | The description of the calculation item |
| [ModifiedTime] | DateTime | The date and time when the calculation item was last modified |
| [State] | String | The state of the calculation item |
| [ErrorMessage] | String | Any error message associated with the calculation item |
| [Expression] | String | The DAX expression for the calculation item |
| [Ordinal] | Integer | The ordinal position of the calculation item within its calculation group |

## Remarks

- Typically used in DAX queries to inspect and document model metadata.
- Permissions required depend on the host. Querying full metadata may require model admin permissions.

## Example

The following DAX query can be run in [DAX query view](/power-bi/transform-model/dax-query-view):

```dax
EVALUATE
	INFO.CALCULATIONITEMS()
```

## Example 2 - DAX query with joins

The following DAX query can be run in [DAX query view](/power-bi/transform-model/dax-query-view):

```dax
EVALUATE
	VAR _CalculationItems =
		INFO.CALCULATIONITEMS()

	VAR _CalculationGroups = 
		SELECTCOLUMNS(
			INFO.CALCULATIONGROUPS(),
			"CalculationGroupID", [ID],
			"Calculation Group Name", [Name]
		)

	VAR _CombinedTable =
		NATURALLEFTOUTERJOIN(
			_CalculationItems,
			_CalculationGroups
		)

	RETURN
		SELECTCOLUMNS(
			_CombinedTable,
			"Calculation Item Name", [Name],
			"Calculation Group Name", [Calculation Group Name],
			"Expression", [Expression],
			"Ordinal", [Ordinal]
		)
	ORDER BY [Calculation Group Name], [Ordinal]
```