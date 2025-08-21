---
description: "Learn more about: INFO.GROUPBYCOLUMNS"
title: "INFO.GROUPBYCOLUMNS function (DAX)"
author: jeroenterheerdt
---
# INFO.GROUPBYCOLUMNS

[!INCLUDE[applies-to-measures-columns-tables-visual-calculations-discouraged](includes/applies-to-measures-columns-tables-visual-calculations-discouraged.md)]

Returns a table with information about each group by column in the semantic model. This function provides metadata about columns used in group by operations.

## Syntax

```dax
INFO.GROUPBYCOLUMNS()
```

## Return value

A table whose columns match the schema rowset for group by columns in the current semantic model.

## Remarks

- Typically used in DAX queries to inspect and document model metadata.
- Permissions required depend on the host. Querying full metadata may require model admin permissions.

## Example 1 - DAX query

```dax
EVALUATE
    INFO.GROUPBYCOLUMNS()
```

## Example 2 - DAX query with SELECTCOLUMNS

```dax
EVALUATE
    SELECTCOLUMNS(
        INFO.GROUPBYCOLUMNS(),
        "Name", [Name],
        "ExplicitName", [ExplicitName],
        "ColumnID", [ColumnID]
    )
```

## Example 3 - Calculated table

```dax
Group By Columns =
SELECTCOLUMNS(
    INFO.GROUPBYCOLUMNS(),
    "Name", [Name],
    "ExplicitName", [ExplicitName]
)
```

## Example 4 - Measure

```dax
Number of Group By Columns =
COUNTROWS(INFO.GROUPBYCOLUMNS())
```