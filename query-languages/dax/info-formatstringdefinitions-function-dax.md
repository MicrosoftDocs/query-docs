---
description: "Learn more about: INFO.FORMATSTRINGDEFINITIONS"
title: "INFO.FORMATSTRINGDEFINITIONS function (DAX)"
author: jeroenterheerdt
---
# INFO.FORMATSTRINGDEFINITIONS

[!INCLUDE[applies-to-query-only](includes/applies-to-query-only.md)]

Returns a table with information about each format string definition in the semantic model. This function provides metadata about format string definitions for measures and columns.

## Syntax

```dax
INFO.FORMATSTRINGDEFINITIONS ( [<Restriction name>, <Restriction value>], ... )
```

[!INCLUDE[parameters-for-info-dax-functions](includes/parameters-for-info-dax-functions.md)]

## Return value

A table with the following columns:

| Column name | Data type | Description |
|--|--|--|
| [ID] | Integer | Unique identifier for the format string definition |
| [ObjectID] | Integer | Identifier of the object (measure or column) that uses this format string |
| [ObjectType] | Integer | Type of object (measure, column, etc.) |
| [Expression] | String | DAX expression that defines the format string |
| [ModifiedTime] | DateTime | When the format string definition was last modified |
| [State] | Integer | Current state of the format string definition |
| [ErrorMessage] | String | Error message if the format string definition is in an error state |

## Remarks

- Typically used in DAX queries to inspect and document model metadata.
- Permissions required depend on the host. Querying full metadata may require model admin permissions.

## Example

The following DAX query can be run in [DAX query view](/power-bi/transform-model/dax-query-view):

```dax
EVALUATE
	INFO.FORMATSTRINGDEFINITIONS()
```

## See also

- [INFO.TABLES](info-tables-function-dax.md)
- [INFO.COLUMNS](info-columns-function-dax.md)
- [INFO.MEASURES](info-measures-function-dax.md)
- [INFO functions overview](info-functions-dax.md)
