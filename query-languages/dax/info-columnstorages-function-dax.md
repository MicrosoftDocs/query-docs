---
description: "Learn more about: INFO.COLUMNSTORAGES"
title: "INFO.COLUMNSTORAGES function (DAX)"
author: jeroenterheerdt
---
# INFO.COLUMNSTORAGES

[!INCLUDE[applies-to-query-only](includes/applies-to-query-only.md)]

Returns a table with information about each column storage in the semantic model. This function provides metadata about how columns are stored and their storage characteristics.

## Syntax

```dax
INFO.COLUMNSTORAGES ( [<Restriction name>, <Restriction value>], ... )
```

[!INCLUDE[parameters-for-info-dax-functions](includes/parameters-for-info-dax-functions.md)]

## Return value

A table whose columns match the schema rowset for column storages in the current semantic model.

## Remarks

- Typically used in DAX queries to inspect and document model metadata.
- Permissions required depend on the host. Querying full metadata may require model admin permissions.

## Example

The following DAX query can be run in [DAX query view](/power-bi/transform-model/dax-query-view):

```dax
EVALUATE
	INFO.COLUMNSTORAGES()
```

## Example 2 - DAX query with SELECTCOLUMNS

```dax
EVALUATE
    SELECTCOLUMNS(
        INFO.COLUMNSTORAGES(),
        "ColumnID", [ColumnID],
        "State", [State],
        "CompressionType", [CompressionType]
    )
```

## Example 3 - Calculated table

```dax
Column Storages =
SELECTCOLUMNS(
    INFO.COLUMNSTORAGES(),
    "ColumnID", [ColumnID],
    "State", [State]
)
```

## Example 4 - Measure

```dax
Number of Column Storages =
COUNTROWS(INFO.COLUMNSTORAGES())
```