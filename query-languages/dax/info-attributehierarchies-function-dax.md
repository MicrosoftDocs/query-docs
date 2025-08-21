---
description: "Learn more about: INFO.ATTRIBUTEHIERARCHIES"
title: "INFO.ATTRIBUTEHIERARCHIES function (DAX)"
author: jeroenterheerdt
---
# INFO.ATTRIBUTEHIERARCHIES

[!INCLUDE[applies-to-measures-columns-tables-visual-calculations-discouraged](includes/applies-to-measures-columns-tables-visual-calculations-discouraged.md)]

Returns a table with information about each attribute hierarchy in the semantic model. This function provides metadata about the attribute hierarchies defined in the model.

## Syntax

```dax
INFO.ATTRIBUTEHIERARCHIES()
```

## Return value

A table whose columns match the schema rowset for attribute hierarchies in the current semantic model.

## Remarks

- Typically used in DAX queries to inspect and document model metadata.
- Permissions required depend on the host. Querying full metadata may require model admin permissions.

## Example 1 - DAX query

```dax
EVALUATE
    INFO.ATTRIBUTEHIERARCHIES()
```

## Example 2 - DAX query with SELECTCOLUMNS

```dax
EVALUATE
    SELECTCOLUMNS(
        INFO.ATTRIBUTEHIERARCHIES(),
        "Name", [Name],
        "IsVisible", [IsVisible],
        "State", [State]
    )
```

## Example 3 - Calculated table

```dax
Attribute Hierarchies =
SELECTCOLUMNS(
    INFO.ATTRIBUTEHIERARCHIES(),
    "Name", [Name],
    "IsVisible", [IsVisible]
)
```

## Example 4 - Measure

```dax
Number of Attribute Hierarchies =
COUNTROWS(INFO.ATTRIBUTEHIERARCHIES())
```