---
description: "Learn more about: INFO.EXTENDEDPROPERTIES"
title: "INFO.EXTENDEDPROPERTIES function (DAX)"
author: jeroenterheerdt
---
# INFO.EXTENDEDPROPERTIES

[!INCLUDE[applies-to-query-only](includes/applies-to-query-only.md)]

Returns a table with information about each extended property in the semantic model. This function provides metadata about extended properties defined for model objects.

## Syntax

```dax
INFO.EXTENDEDPROPERTIES ( [<Restriction name>, <Restriction value>], ... )
```

[!INCLUDE[parameters-for-info-dax-functions](includes/parameters-for-info-dax-functions.md)]

## Return value

A table with the following columns:

| Column name | Data type | Description |
|--|--|--|
| [ID] | Integer | Unique identifier for the extended property |
| [ObjectID] | Integer | Identifier of the object that has this extended property |
| [ObjectType] | Integer | Type of object (table, column, measure, etc.) |
| [Name] | String | Name of the extended property |
| [Type] | Integer | Data type of the property value |
| [Value] | String | Value of the extended property |
| [ModifiedTime] | DateTime | When the extended property was last modified |

## Remarks

- Typically used in DAX queries to inspect and document model metadata.
- Permissions required depend on the host. Querying full metadata may require model admin permissions.

## Example

The following DAX query can be run in [DAX query view](/power-bi/transform-model/dax-query-view):

```dax
EVALUATE
	INFO.EXTENDEDPROPERTIES()
```

## See also

[INFO.TABLES](info-tables-function-dax.md)
[INFO.COLUMNS](info-columns-function-dax.md)
[INFO.MEASURES](info-measures-function-dax.md)
[INFO functions overview](info-functions-dax.md)
