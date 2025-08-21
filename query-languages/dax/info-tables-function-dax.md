---
description: "Learn more about: INFO.TABLES"
title: "INFO.TABLES function (DAX)"
author: jeroenterheerdt
---
# INFO.TABLES

[!INCLUDE[applies-to-measures-columns-tables-visual-calculations-discouraged](includes/applies-to-measures-columns-tables-visual-calculations-discouraged.md)]

Returns a table with information about each table in the semantic model, with columns that match the schema rowset for table objects (for example, name, description, and visibility).

## Syntax

```dax
INFO.TABLES()
```

## Return value

A table whose columns match the schema rowset for table objects in the current semantic model.

## Remarks

- Useful for documentation and governance scenarios.
- Permissions required depend on the host. Querying full metadata may require model admin permissions.

## Example 1 - DAX query

```dax
EVALUATE
    INFO.TABLES()
```

## Example 2 - DAX query with SELECTCOLUMNS

```dax
EVALUATE
    SELECTCOLUMNS(
        INFO.TABLES(),
        "Name", [Name],
        "IsHidden", [IsHidden]
    )
```

## Example 3 - Calculated table

```dax
Tables in this semantic model =
SELECTCOLUMNS(
    INFO.TABLES(),
    "Name", [Name],
    "IsHidden", [IsHidden]
)
```

## Example 4 - Measure

```dax
Number of tables =
COUNTROWS(INFO.TABLES())
```