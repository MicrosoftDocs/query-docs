---
description: "Learn more about: INFO.COLUMNSTORAGES"
title: "INFO.COLUMNSTORAGES function (DAX)"
author: jeroenterheerdt
---
# INFO.COLUMNSTORAGES

[!INCLUDE[applies-to-measures-columns-tables-visual-calculations-discouraged](includes/applies-to-measures-columns-tables-visual-calculations-discouraged.md)]

Returns a table with information about each column storage in the semantic model. This function provides metadata about how columns are stored and their storage characteristics.

## Syntax

```dax
INFO.COLUMNSTORAGES()
```

## Return value

A table whose columns match the schema rowset for column storages in the current semantic model.

## Remarks

- Typically used in DAX queries to inspect and document model metadata.
- Permissions required depend on the host. Querying full metadata may require model admin permissions.

## Example 1 - DAX query

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