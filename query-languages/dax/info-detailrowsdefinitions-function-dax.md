---
description: "Learn more about: INFO.DETAILROWSDEFINITIONS"
title: "INFO.DETAILROWSDEFINITIONS function (DAX)"
author: jeroenterheerdt
---
# INFO.DETAILROWSDEFINITIONS

[!INCLUDE[applies-to-query-only](includes/applies-to-query-only.md)]

Returns a table with information about each detail rows definition in the semantic model. This function provides metadata about detail rows definitions for measures.

## Syntax

```dax
INFO.DETAILROWSDEFINITIONS ( [<Restriction name>, <Restriction value>], ... )
```

[!INCLUDE[parameters-for-info-dax-functions](includes/parameters-for-info-dax-functions.md)]

## Return value

A table with the following columns:

| Column name | Data type | Description |
| --- | --- | --- |
| [ID] | Integer | Unique identifier for the detail rows definition |
| [ObjectID] | Integer | Identifier of the object this detail rows definition belongs to |
| [ObjectType] | String | Type of the object (e.g., measure, table) |
| [Expression] | String | DAX expression for the detail rows definition |
| [ModifiedTime] | DateTime | Date and time when the detail rows definition was last modified |
| [State] | Integer | State of the detail rows definition |
| [ErrorMessage] | String | Error message if the detail rows definition has an error |

## Remarks

- Typically used in DAX queries to inspect and document model metadata.
- Permissions required depend on the host. Querying full metadata may require model admin permissions.

## Example

The following DAX query can be run in [DAX query view](/power-bi/transform-model/dax-query-view):

```dax
EVALUATE
	INFO.DETAILROWSDEFINITIONS()
```
## See also

- [INFO.TABLES](info-tables-function-dax.md)
- [INFO.COLUMNS](info-columns-function-dax.md)
- [INFO.MEASURES](info-measures-function-dax.md)
- [INFO functions overview](info-functions-dax.md)
