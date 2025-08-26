---
description: "Learn more about: INFO.TABLES"
title: "INFO.TABLES function (DAX)"
author: jeroenterheerdt
---
# INFO.TABLES

[!INCLUDE[applies-to-query-only](includes/applies-to-query-only.md)]

Returns a table with information about each table in the semantic model, with columns that match the schema rowset for table objects (for example, name, description, and visibility).

## Syntax

```dax
INFO.TABLES ( [<Restriction name>, <Restriction value>], ... )
```

[!INCLUDE[parameters-for-info-dax-functions](includes/parameters-for-info-dax-functions.md)]

## Return value

A table whose columns match the schema rowset for table objects in the current semantic model.

## Remarks

- Useful for documentation and governance scenarios.
- Permissions required depend on the host. Querying full metadata may require model admin permissions.

## Example

The following DAX query can be run in [DAX query view](/power-bi/transform-model/dax-query-view):

```dax
EVALUATE
	INFO.TABLES()
```

## See also

[INFO.COLUMNS](info-columns-function-dax.md)
[INFO.PARTITIONS](info-partitions-function-dax.md)
[INFO.RELATIONSHIPS](info-relationships-function-dax.md)
[INFO functions overview](info-functions-dax.md)
