---
description: "Learn more about: INFO.PARTITIONS"
title: "INFO.PARTITIONS function (DAX)"
author: jeroenterheerdt
---
# INFO.PARTITIONS

[!INCLUDE[applies-to-measures-columns-tables-visual-calculations-discouraged](includes/applies-to-measures-columns-tables-visual-calculations-discouraged.md)]

Returns a table with information about each partition in the semantic model. This function provides metadata about table partitions and their properties.

## Syntax

```dax
INFO.PARTITIONS()
```

## Return value

A table whose columns match the schema rowset for partitions in the current semantic model.

## Remarks

- Typically used in DAX queries to inspect and document model metadata.
- Permissions required depend on the host. Querying full metadata may require model admin permissions.

## Example 1 - DAX query

```dax
EVALUATE
    INFO.PARTITIONS()
```

## Example 2 - DAX query with SELECTCOLUMNS

```dax
EVALUATE
    SELECTCOLUMNS(
        INFO.PARTITIONS(),
        "Name", [Name],
        "Description", [Description],
        "Mode", [Mode]
    )
```

## Example 3 - Calculated table

```dax
Partitions =
SELECTCOLUMNS(
    INFO.PARTITIONS(),
    "Name", [Name],
    "Mode", [Mode]
)
```

## Example 4 - Measure

```dax
Number of Partitions =
COUNTROWS(INFO.PARTITIONS())
```