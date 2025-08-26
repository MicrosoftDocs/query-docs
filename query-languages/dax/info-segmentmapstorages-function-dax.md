---
description: "Learn more about: INFO.SEGMENTMAPSTORAGES"
title: "INFO.SEGMENTMAPSTORAGES function (DAX)"
author: jeroenterheerdt
---
# INFO.SEGMENTMAPSTORAGES

[!INCLUDE[applies-to-query-only](includes/applies-to-query-only.md)]

Returns a table with information about each segment map storage in the semantic model. This function provides metadata about segment map storage characteristics.

## Syntax

```dax
INFO.SEGMENTMAPSTORAGES ( [<Restriction name>, <Restriction value>], ... )
```

[!INCLUDE[parameters-for-info-dax-functions](includes/parameters-for-info-dax-functions.md)]

## Return value

A table whose columns match the schema rowset for segment map storages in the current semantic model.

## Remarks

- Typically used in DAX queries to inspect and document model metadata.
- Permissions required depend on the host. Querying full metadata may require model admin permissions.

## Example

The following DAX query can be run in [DAX query view](/power-bi/transform-model/dax-query-view):

```dax
EVALUATE
	INFO.SEGMENTMAPSTORAGES()
```

## See also

[INFO.TABLES](info-tables-function-dax.md)
[INFO.COLUMNS](info-columns-function-dax.md)
[INFO.MEASURES](info-measures-function-dax.md)
[INFO functions overview](info-functions-dax.md)
