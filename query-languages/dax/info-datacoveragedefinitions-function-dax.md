---
description: "Learn more about: INFO.DATACOVERAGEDEFINITIONS"
title: "INFO.DATACOVERAGEDEFINITIONS function (DAX)"
author: jeroenterheerdt
---
# INFO.DATACOVERAGEDEFINITIONS

[!INCLUDE[applies-to-query-only](includes/applies-to-query-only.md)]

Returns a table with information about each data coverage definition in the semantic model. This function provides metadata about data coverage settings and definitions.

## Syntax

```dax
INFO.DATACOVERAGEDEFINITIONS ( [<Restriction name>, <Restriction value>], ... )
```

[!INCLUDE[parameters-for-info-dax-functions](includes/parameters-for-info-dax-functions.md)]

## Return value

A table with the following columns:

| Column | Description |
|--------|-------------|
| [ID] | Unique identifier for the data coverage definition |
| [PartitionID] | Identifier of the partition associated with the data coverage definition |
| [Description] | Description of the data coverage definition |
| [Expression] | DAX expression that is evaluated for the data coverage definition. |
| [ModifiedTime] | Timestamp of when the data coverage definition was last modified |
| [State] | Current state of the data coverage definition (e.g., Ready, Error) |
| [ErrorMessage] | Error message if the data coverage definition is in an error state |

## Remarks

- Typically used in DAX queries to inspect and document model metadata.
- Permissions required depend on the host. Querying full metadata may require model admin permissions.

## Example

The following DAX query can be run in [DAX query view](/power-bi/transform-model/dax-query-view):

```dax
EVALUATE
	INFO.DATACOVERAGEDEFINITIONS()
```

## See also

- [INFO.TABLES](info-tables-function-dax.md)
- [INFO.COLUMNS](info-columns-function-dax.md)
- [INFO.MEASURES](info-measures-function-dax.md)
- [INFO functions overview](info-functions-dax.md)
