---
description: "Learn more about: INFO.MODEL"
title: "INFO.MODEL function (DAX)"
author: jeroenterheerdt
---
# INFO.MODEL

[!INCLUDE[applies-to-measures-columns-tables-visual-calculations-discouraged](includes/applies-to-measures-columns-tables-visual-calculations-discouraged.md)]

Returns a table with information about the model in the semantic model. This function provides metadata about the model itself and its properties.

## Syntax

```dax
INFO.MODEL()
```

## Return value

A table whose columns match the schema rowset for the model in the current semantic model.

## Remarks

- Typically used in DAX queries to inspect and document model metadata.
- Permissions required depend on the host. Querying full metadata may require model admin permissions.

## Example 1 - DAX query

```dax
EVALUATE
    INFO.MODEL()
```

## Example 2 - DAX query with SELECTCOLUMNS

```dax
EVALUATE
    SELECTCOLUMNS(
        INFO.MODEL(),
        "Name", [Name],
        "Description", [Description],
        "Version", [Version]
    )
```

## Example 3 - Calculated table

```dax
Model Info =
SELECTCOLUMNS(
    INFO.MODEL(),
    "Name", [Name],
    "Description", [Description]
)
```

## Example 4 - Measure

```dax
Model Count =
COUNTROWS(INFO.MODEL())
```