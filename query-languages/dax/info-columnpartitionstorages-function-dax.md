---
description: "Learn more about: INFO.COLUMNPARTITIONSTORAGES"
title: "INFO.COLUMNPARTITIONSTORAGES function (DAX)"
author: jeroenterheerdt
---
# INFO.COLUMNPARTITIONSTORAGES

[!INCLUDE[applies-to-measures-columns-tables-visual-calculations-discouraged](includes/applies-to-measures-columns-tables-visual-calculations-discouraged.md)]

Returns a table with information about each column partition storage in the semantic model. This function provides metadata about how column partitions are stored.

## Syntax

```dax
INFO.COLUMNPARTITIONSTORAGES()
```

## Return value

A table whose columns match the schema rowset for column partition storages in the current semantic model.

## Remarks

- Typically used in DAX queries to inspect and document model metadata.
- Permissions required depend on the host. Querying full metadata may require model admin permissions.

## Example 1 - DAX query

```dax
EVALUATE
    INFO.COLUMNPARTITIONSTORAGES()
```

## Example 2 - DAX query with SELECTCOLUMNS

```dax
EVALUATE
    SELECTCOLUMNS(
        INFO.COLUMNPARTITIONSTORAGES(),
        "PartitionID", [PartitionID],
        "ColumnID", [ColumnID],
        "State", [State]
    )
```

## Example 3 - Calculated table

```dax
Column Partition Storages =
SELECTCOLUMNS(
    INFO.COLUMNPARTITIONSTORAGES(),
    "PartitionID", [PartitionID],
    "ColumnID", [ColumnID]
)
```

## Example 4 - Measure

```dax
Number of Column Partition Storages =
COUNTROWS(INFO.COLUMNPARTITIONSTORAGES())
```