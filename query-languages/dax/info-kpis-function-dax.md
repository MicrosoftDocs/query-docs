---
description: "Learn more about: INFO.KPIS"
title: "INFO.KPIS function (DAX)"
author: jeroenterheerdt
---
# INFO.KPIS

[!INCLUDE[applies-to-measures-columns-tables-visual-calculations-discouraged](includes/applies-to-measures-columns-tables-visual-calculations-discouraged.md)]

Returns a table with information about each KPI in the semantic model. This function provides metadata about Key Performance Indicators defined in the model.

## Syntax

```dax
INFO.KPIS()
```

## Return value

A table whose columns match the schema rowset for KPIs in the current semantic model.

## Remarks

- Typically used in DAX queries to inspect and document model metadata.
- Permissions required depend on the host. Querying full metadata may require model admin permissions.

## Example 1 - DAX query

```dax
EVALUATE
    INFO.KPIS()
```

## Example 2 - DAX query with SELECTCOLUMNS

```dax
EVALUATE
    SELECTCOLUMNS(
        INFO.KPIS(),
        "Name", [Name],
        "Description", [Description],
        "TargetExpression", [TargetExpression]
    )
```

## Example 3 - Calculated table

```dax
KPIs =
SELECTCOLUMNS(
    INFO.KPIS(),
    "Name", [Name],
    "Description", [Description]
)
```

## Example 4 - Measure

```dax
Number of KPIs =
COUNTROWS(INFO.KPIS())
```