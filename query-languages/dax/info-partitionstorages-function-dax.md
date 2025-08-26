---
description: "Learn more about: INFO.PARTITIONSTORAGES"
title: "INFO.PARTITIONSTORAGES function (DAX)"
author: jeroenterheerdt
---
# INFO.PARTITIONSTORAGES

[!INCLUDE[applies-to-query-only](includes/applies-to-query-only.md)]

Returns a table with information about each partition storage in the semantic model. This function provides metadata about how partitions are stored.

## Syntax

```dax
INFO.PARTITIONSTORAGES ( [<Restriction name>, <Restriction value>], ... )
```

[!INCLUDE[parameters-for-info-dax-functions](includes/parameters-for-info-dax-functions.md)]

## Return value

A table whose columns match the schema rowset for partition storages in the current semantic model.

## Remarks

- Typically used in DAX queries to inspect and document model metadata.
- Permissions required depend on the host. Querying full metadata may require model admin permissions.

## Example

The following DAX query can be run in [DAX query view](/power-bi/transform-model/dax-query-view):

```dax
EVALUATE
	INFO.PARTITIONSTORAGES()
```

## Example 2 - DAX query with SELECTCOLUMNS

```dax
EVALUATE
    SELECTCOLUMNS(
        INFO.PARTITIONSTORAGES(),
        "PartitionID", [PartitionID],
        "State", [State],
        "LastUpdateTime", [LastUpdateTime]
    )
```

## Example 3 - Calculated table

```dax
Partition Storages =
SELECTCOLUMNS(
    INFO.PARTITIONSTORAGES(),
    "PartitionID", [PartitionID],
    "State", [State]
)
```

## Example 4 - Measure

```dax
Number of Partition Storages =
COUNTROWS(INFO.PARTITIONSTORAGES())
```
## See also

[INFO.TABLES](info-tables-function-dax.md)
[INFO.COLUMNS](info-columns-function-dax.md)
[INFO.MEASURES](info-measures-function-dax.md)
[INFO functions overview](info-functions-dax.md)
