---
description: "Learn more about: INFO.COLUMNS"
title: "INFO.COLUMNS function (DAX)"
author: jeroenterheerdt
---
# INFO.COLUMNS

[!INCLUDE[applies-to-measures-columns-tables-visual-calculations-discouraged](includes/applies-to-measures-columns-tables-visual-calculations-discouraged.md)]

Returns a table with information about each column in the semantic model. This function provides metadata about all columns including their properties and characteristics.

## Syntax

```dax
INFO.COLUMNS()
```

## Return value

A table whose columns match the schema rowset for columns in the current semantic model.

## Remarks

- Typically used in DAX queries to inspect and document model metadata.
- Permissions required depend on the host. Querying full metadata may require model admin permissions.

## Example 1 - DAX query

```dax
EVALUATE
    INFO.COLUMNS()
```

## Example 2 - DAX query with SELECTCOLUMNS

```dax
EVALUATE
    SELECTCOLUMNS(
        INFO.COLUMNS(),
        "ExplicitName", [ExplicitName],
        "DataType", [DataType],
        "IsHidden", [IsHidden]
    )
```

## Example 3 - Calculated table

```dax
Columns =
SELECTCOLUMNS(
    INFO.COLUMNS(),
    "Name", [ExplicitName],
    "DataType", [DataType]
)
```

## Example 4 - Measure

```dax
Number of Columns =
COUNTROWS(INFO.COLUMNS())
```