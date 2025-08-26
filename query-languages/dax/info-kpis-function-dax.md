---
description: "Learn more about: INFO.KPIS"
title: "INFO.KPIS function (DAX)"
author: jeroenterheerdt
---
# INFO.KPIS

[!INCLUDE[applies-to-query-only](includes/applies-to-query-only.md)]

Returns a table with information about each KPI in the semantic model. This function provides metadata about Key Performance Indicators defined in the model.

## Syntax

```dax
INFO.KPIS ( [<Restriction name>, <Restriction value>], ... )
```

[!INCLUDE[parameters-for-info-dax-functions](includes/parameters-for-info-dax-functions.md)]

## Return value

A table whose columns match the schema rowset for KPIs in the current semantic model.

## Remarks

- Typically used in DAX queries to inspect and document model metadata.
- Permissions required depend on the host. Querying full metadata may require model admin permissions.

## Example

The following DAX query can be run in [DAX query view](/power-bi/transform-model/dax-query-view):

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
## See also

[INFO.CALCULATIONGROUPS](info-calculationgroups-function-dax.md)
[INFO.CALCULATIONITEMS](info-calculationitems-function-dax.md)
[INFO.MEASURES](info-measures-function-dax.md)
[INFO.TABLES](info-tables-function-dax.md)
[INFO.COLUMNS](info-columns-function-dax.md)
