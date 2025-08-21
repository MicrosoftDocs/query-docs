---
description: "Learn more about: INFO.RELATIONSHIPS"
title: "INFO.RELATIONSHIPS function (DAX)"
author: jeroenterheerdt
---
# INFO.RELATIONSHIPS

[!INCLUDE[applies-to-measures-columns-tables-visual-calculations-discouraged](includes/applies-to-measures-columns-tables-visual-calculations-discouraged.md)]

Returns a table with information about each relationship in the semantic model. This function provides metadata about relationships between tables.

## Syntax

```dax
INFO.RELATIONSHIPS()
```

## Return value

A table whose columns match the schema rowset for relationships in the current semantic model.

## Remarks

- Typically used in DAX queries to inspect and document model metadata.
- Permissions required depend on the host. Querying full metadata may require model admin permissions.

## Example 1 - DAX query

```dax
EVALUATE
    INFO.RELATIONSHIPS()
```

## Example 2 - DAX query with SELECTCOLUMNS

```dax
EVALUATE
    SELECTCOLUMNS(
        INFO.RELATIONSHIPS(),
        "Name", [Name],
        "IsActive", [IsActive],
        "CrossFilteringBehavior", [CrossFilteringBehavior]
    )
```

## Example 3 - Calculated table

```dax
Relationships =
SELECTCOLUMNS(
    INFO.RELATIONSHIPS(),
    "Name", [Name],
    "IsActive", [IsActive]
)
```

## Example 4 - Measure

```dax
Number of Relationships =
COUNTROWS(INFO.RELATIONSHIPS())
```