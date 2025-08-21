---
description: "Learn more about: INFO.PARTITIONSTORAGES"
title: "INFO.PARTITIONSTORAGES function (DAX)"
author: jeroenterheerdt
---
# INFO.PARTITIONSTORAGES

[!INCLUDE[applies-to-measures-columns-tables-visual-calculations-discouraged](includes/applies-to-measures-columns-tables-visual-calculations-discouraged.md)]

Returns a table with information about each partition storage in the semantic model. This function provides metadata about how partitions are stored.

## Syntax

```dax
INFO.PARTITIONSTORAGES()
```

## Return value

A table whose columns match the schema rowset for partition storages in the current semantic model.

## Remarks

- Typically used in DAX queries to inspect and document model metadata.
- Permissions required depend on the host. Querying full metadata may require model admin permissions.

## Example 1 - DAX query

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