---
description: "Learn more about: INFO.HIERARCHIES"
title: "INFO.HIERARCHIES function (DAX)"
author: jeroenterheerdt
---
# INFO.HIERARCHIES

[!INCLUDE[applies-to-measures-columns-tables-visual-calculations-discouraged](includes/applies-to-measures-columns-tables-visual-calculations-discouraged.md)]

Returns a table with information about each hierarchy in the semantic model. This function provides metadata about hierarchies and their properties.

## Syntax

```dax
INFO.HIERARCHIES()
```

## Return value

A table whose columns match the schema rowset for hierarchies in the current semantic model.

## Remarks

- Typically used in DAX queries to inspect and document model metadata.
- Permissions required depend on the host. Querying full metadata may require model admin permissions.

## Example 1 - DAX query

```dax
EVALUATE
    INFO.HIERARCHIES()
```

## Example 2 - DAX query with SELECTCOLUMNS

```dax
EVALUATE
    SELECTCOLUMNS(
        INFO.HIERARCHIES(),
        "Name", [Name],
        "Description", [Description],
        "IsHidden", [IsHidden]
    )
```

## Example 3 - Calculated table

```dax
Hierarchies =
SELECTCOLUMNS(
    INFO.HIERARCHIES(),
    "Name", [Name],
    "Description", [Description]
)
```

## Example 4 - Measure

```dax
Number of Hierarchies =
COUNTROWS(INFO.HIERARCHIES())
```