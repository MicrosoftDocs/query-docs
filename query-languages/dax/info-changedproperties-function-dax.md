---
description: "Learn more about: INFO.CHANGEDPROPERTIES"
title: "INFO.CHANGEDPROPERTIES function (DAX)"
author: jeroenterheerdt
---
# INFO.CHANGEDPROPERTIES

[!INCLUDE[applies-to-query-only](includes/applies-to-query-only.md)]

Returns a table with information about each changed property in the semantic model. This function provides metadata about properties that have been modified in the model.

## Syntax

```dax
INFO.CHANGEDPROPERTIES ( [<Restriction name>, <Restriction value>], ... )
```

[!INCLUDE[parameters-for-info-dax-functions](includes/parameters-for-info-dax-functions.md)]

## Return value

A table with the following columns:

| Column name | Data type | Description |
|-------------|-----------|-------------|
| [ID] | Integer | The unique identifier of the changed property |
| [ObjectID] | Integer | The identifier of the object that has the changed property |
| [ObjectType] | Integer | The type of object that has the changed property |
| [Property] | String | The name of the property that was changed |

## Remarks

- Typically used in DAX queries to inspect and document model metadata.
- Permissions required depend on the host. Querying full metadata may require model admin permissions.

## Example

The following DAX query can be run in [DAX query view](/power-bi/transform-model/dax-query-view):

```dax
EVALUATE
	INFO.CHANGEDPROPERTIES()
```

## Example 2 - DAX query with joins

The following DAX query can be run in [DAX query view](/power-bi/transform-model/dax-query-view):

```dax
EVALUATE
	VAR _ChangedProperties =
		INFO.CHANGEDPROPERTIES()

	VAR _Tables = 
		SELECTCOLUMNS(
			INFO.TABLES(),
			"ObjectID", [ID],
			"Object Name", [Name],
			"Object Type Number", 1  -- Tables are typically object type 1
		)

	VAR _Columns = 
		SELECTCOLUMNS(
			INFO.COLUMNS(),
			"ObjectID", [ID],
			"Object Name", [ExplicitName],
			"Object Type Number", 2  -- Columns are typically object type 2
		)

	VAR _AllObjects = 
		UNION(_Tables, _Columns)

	VAR _CombinedTable =
		NATURALLEFTOUTERJOIN(
			_ChangedProperties,
			_AllObjects
		)

	RETURN
		SELECTCOLUMNS(
			_CombinedTable,
			"Object Name", [Object Name],
			"Object Type", [ObjectType],
			"Changed Property", [Property]
		)
	ORDER BY [Object Name], [Changed Property]
```