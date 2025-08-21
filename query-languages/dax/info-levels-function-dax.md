---
description: "Learn more about: INFO.LEVELS"
title: "INFO.LEVELS function (DAX)"
author: jeroenterheerdt
---
# INFO.LEVELS

[!INCLUDE[applies-to-measures-columns-tables-visual-calculations-discouraged](includes/applies-to-measures-columns-tables-visual-calculations-discouraged.md)]

Returns a table with information about each level in the semantic model. This function provides metadata about hierarchy levels and their properties.

## Syntax

```dax
INFO.LEVELS()
```

## Return value

A table whose columns match the schema rowset for levels in the current semantic model.

## Remarks

- Typically used in DAX queries to inspect and document model metadata.
- Permissions required depend on the host. Querying full metadata may require model admin permissions.

## Example 1 - DAX query

```dax
EVALUATE
    INFO.LEVELS()
```

## Example 2 - DAX query with SELECTCOLUMNS

```dax
EVALUATE
    SELECTCOLUMNS(
        INFO.LEVELS(),
        "Name", [Name],
        "Description", [Description],
        "Ordinal", [Ordinal]
    )
```

## Example 3 - Calculated table

```dax
Levels =
SELECTCOLUMNS(
    INFO.LEVELS(),
    "Name", [Name],
    "Ordinal", [Ordinal]
)
```

## Example 4 - Measure

```dax
Number of Levels =
COUNTROWS(INFO.LEVELS())
```