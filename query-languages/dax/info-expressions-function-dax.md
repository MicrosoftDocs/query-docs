---
description: "Learn more about: INFO.EXPRESSIONS"
title: "INFO.EXPRESSIONS function (DAX)"
author: jeroenterheerdt
---
# INFO.EXPRESSIONS

[!INCLUDE[applies-to-measures-columns-tables-visual-calculations-discouraged](includes/applies-to-measures-columns-tables-visual-calculations-discouraged.md)]

Returns a table with information about each expression in the semantic model. This function provides metadata about expressions defined in the model.

## Syntax

```dax
INFO.EXPRESSIONS()
```

## Return value

A table whose columns match the schema rowset for expressions in the current semantic model.

## Remarks

- Typically used in DAX queries to inspect and document model metadata.
- Permissions required depend on the host. Querying full metadata may require model admin permissions.

## Example 1 - DAX query

```dax
EVALUATE
    INFO.EXPRESSIONS()
```

## Example 2 - DAX query with SELECTCOLUMNS

```dax
EVALUATE
    SELECTCOLUMNS(
        INFO.EXPRESSIONS(),
        "Name", [Name],
        "Expression", [Expression],
        "Kind", [Kind]
    )
```

## Example 3 - Calculated table

```dax
Expressions =
SELECTCOLUMNS(
    INFO.EXPRESSIONS(),
    "Name", [Name],
    "Expression", [Expression]
)
```

## Example 4 - Measure

```dax
Number of Expressions =
COUNTROWS(INFO.EXPRESSIONS())
```