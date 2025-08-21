---
description: "Learn more about: INFO.CALCULATIONITEMS"
title: "INFO.CALCULATIONITEMS function (DAX)"
author: jeroenterheerdt
---
# INFO.CALCULATIONITEMS

[!INCLUDE[applies-to-measures-columns-tables-visual-calculations-discouraged](includes/applies-to-measures-columns-tables-visual-calculations-discouraged.md)]

Returns a table with information about each calculation item in the semantic model. This function provides metadata about calculation items within calculation groups.

## Syntax

```dax
INFO.CALCULATIONITEMS()
```

## Return value

A table whose columns match the schema rowset for calculation items in the current semantic model.

## Remarks

- Typically used in DAX queries to inspect and document model metadata.
- Permissions required depend on the host. Querying full metadata may require model admin permissions.

## Example 1 - DAX query

```dax
EVALUATE
    INFO.CALCULATIONITEMS()
```

## Example 2 - DAX query with SELECTCOLUMNS

```dax
EVALUATE
    SELECTCOLUMNS(
        INFO.CALCULATIONITEMS(),
        "Name", [Name],
        "Expression", [Expression],
        "Ordinal", [Ordinal]
    )
```

## Example 3 - Calculated table

```dax
Calculation Items =
SELECTCOLUMNS(
    INFO.CALCULATIONITEMS(),
    "Name", [Name],
    "Expression", [Expression]
)
```

## Example 4 - Measure

```dax
Number of Calculation Items =
COUNTROWS(INFO.CALCULATIONITEMS())
```