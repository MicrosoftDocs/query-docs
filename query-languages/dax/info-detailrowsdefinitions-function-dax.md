---
description: "Learn more about: INFO.DETAILROWSDEFINITIONS"
title: "INFO.DETAILROWSDEFINITIONS function (DAX)"
author: jeroenterheerdt
---
# INFO.DETAILROWSDEFINITIONS

[!INCLUDE[applies-to-measures-columns-tables-visual-calculations-discouraged](includes/applies-to-measures-columns-tables-visual-calculations-discouraged.md)]

Returns a table with information about each detail rows definition in the semantic model. This function provides metadata about detail rows definitions for measures.

## Syntax

```dax
INFO.DETAILROWSDEFINITIONS()
```

## Return value

A table whose columns match the schema rowset for detail rows definitions in the current semantic model.

## Remarks

- Typically used in DAX queries to inspect and document model metadata.
- Permissions required depend on the host. Querying full metadata may require model admin permissions.

## Example 1 - DAX query

```dax
EVALUATE
    INFO.DETAILROWSDEFINITIONS()
```

## Example 2 - DAX query with SELECTCOLUMNS

```dax
EVALUATE
    SELECTCOLUMNS(
        INFO.DETAILROWSDEFINITIONS(),
        "Name", [Name],
        "Expression", [Expression],
        "State", [State]
    )
```

## Example 3 - Calculated table

```dax
Detail Rows Definitions =
SELECTCOLUMNS(
    INFO.DETAILROWSDEFINITIONS(),
    "Name", [Name],
    "Expression", [Expression]
)
```

## Example 4 - Measure

```dax
Number of Detail Rows Definitions =
COUNTROWS(INFO.DETAILROWSDEFINITIONS())
```