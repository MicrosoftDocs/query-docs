---
description: "Learn more about: INFO.MEASURES"
title: "INFO.MEASURES function (DAX)"
author: jeroenterheerdt
---
# INFO.MEASURES

[!INCLUDE[applies-to-measures-columns-tables-visual-calculations-discouraged](includes/applies-to-measures-columns-tables-visual-calculations-discouraged.md)]

Returns a table with information about each measure in the semantic model, with columns that match the schema rowset for measure objects (for example, name, expression, and state).

## Syntax

```dax
INFO.MEASURES()
```

## Return value

A table whose columns match the schema rowset for measure objects in the current semantic model.

## Remarks

- Typically used in DAX queries to inspect and document model metadata.
- Permissions required depend on the host. Querying full metadata may require model admin permissions.

## Example 1 - DAX query

```dax
EVALUATE
    INFO.MEASURES()
```

## Example 2 - DAX query with SELECTCOLUMNS

```dax
EVALUATE
    SELECTCOLUMNS(
        INFO.MEASURES(),
        "Name", [Name],
        "Expression", [Expression],
        "State", [State]
    )
```

## Example 3 - Calculated table

```dax
Measures in this semantic model =
SELECTCOLUMNS(
    INFO.MEASURES(),
    "Name", [Name],
    "Expression", [Expression]
)
```

## Example 4 - Measure

```dax
Number of measures =
COUNTROWS(INFO.MEASURES())
```