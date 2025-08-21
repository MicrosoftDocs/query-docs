---
description: "Learn more about: INFO.QUERYGROUPS"
title: "INFO.QUERYGROUPS function (DAX)"
author: jeroenterheerdt
---
# INFO.QUERYGROUPS

[!INCLUDE[applies-to-measures-columns-tables-visual-calculations-discouraged](includes/applies-to-measures-columns-tables-visual-calculations-discouraged.md)]

Returns a table with information about each query group in the semantic model. This function provides metadata about query groups defined in the model.

## Syntax

```dax
INFO.QUERYGROUPS()
```

## Return value

A table whose columns match the schema rowset for query groups in the current semantic model.

## Remarks

- Typically used in DAX queries to inspect and document model metadata.
- Permissions required depend on the host. Querying full metadata may require model admin permissions.

## Example 1 - DAX query

```dax
EVALUATE
    INFO.QUERYGROUPS()
```

## Example 2 - DAX query with SELECTCOLUMNS

```dax
EVALUATE
    SELECTCOLUMNS(
        INFO.QUERYGROUPS(),
        "Name", [Name],
        "Description", [Description],
        "FolderName", [FolderName]
    )
```

## Example 3 - Calculated table

```dax
Query Groups =
SELECTCOLUMNS(
    INFO.QUERYGROUPS(),
    "Name", [Name],
    "Description", [Description]
)
```

## Example 4 - Measure

```dax
Number of Query Groups =
COUNTROWS(INFO.QUERYGROUPS())
```