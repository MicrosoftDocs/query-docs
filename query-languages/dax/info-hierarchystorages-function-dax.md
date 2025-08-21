---
description: "Learn more about: INFO.HIERARCHYSTORAGES"
title: "INFO.HIERARCHYSTORAGES function (DAX)"
author: jeroenterheerdt
---
# INFO.HIERARCHYSTORAGES

[!INCLUDE[applies-to-measures-columns-tables-visual-calculations-discouraged](includes/applies-to-measures-columns-tables-visual-calculations-discouraged.md)]

Returns a table with information about each hierarchy storage in the semantic model. This function provides metadata about how hierarchies are stored.

## Syntax

```dax
INFO.HIERARCHYSTORAGES()
```

## Return value

A table whose columns match the schema rowset for hierarchy storages in the current semantic model.

## Remarks

- Typically used in DAX queries to inspect and document model metadata.
- Permissions required depend on the host. Querying full metadata may require model admin permissions.

## Example 1 - DAX query

```dax
EVALUATE
    INFO.HIERARCHYSTORAGES()
```

## Example 2 - DAX query with SELECTCOLUMNS

```dax
EVALUATE
    SELECTCOLUMNS(
        INFO.HIERARCHYSTORAGES(),
        "HierarchyID", [HierarchyID],
        "State", [State],
        "LastUpdateTime", [LastUpdateTime]
    )
```

## Example 3 - Calculated table

```dax
Hierarchy Storages =
SELECTCOLUMNS(
    INFO.HIERARCHYSTORAGES(),
    "HierarchyID", [HierarchyID],
    "State", [State]
)
```

## Example 4 - Measure

```dax
Number of Hierarchy Storages =
COUNTROWS(INFO.HIERARCHYSTORAGES())
```