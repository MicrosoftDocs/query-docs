---
description: "Learn more about: INFO.COLUMNPARTITIONSTORAGES"
title: "INFO.COLUMNPARTITIONSTORAGES function (DAX)"
author: jeroenterheerdt
---
# INFO.COLUMNPARTITIONSTORAGES

[!INCLUDE[applies-to-query-only](includes/applies-to-query-only.md)]

Returns a table with information about each column partition storage in the semantic model. This function provides metadata about how column partitions are stored.

## Syntax

```dax
INFO.COLUMNPARTITIONSTORAGES ( [<Restriction name>, <Restriction value>], ... )
```

[!INCLUDE[parameters-for-info-dax-functions](includes/parameters-for-info-dax-functions.md)]

## Return value

A table whose columns match the schema rowset for column partition storages in the current semantic model.

## Remarks

- Typically used in DAX queries to inspect and document model metadata.
- Permissions required depend on the host. Querying full metadata may require model admin permissions.

## Example

The following DAX query can be run in [DAX query view](/power-bi/transform-model/dax-query-view):

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