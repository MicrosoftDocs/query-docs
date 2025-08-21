---
description: "Learn more about: INFO.SEGMENTSTORAGES"
title: "INFO.SEGMENTSTORAGES function (DAX)"
author: jeroenterheerdt
---
# INFO.SEGMENTSTORAGES

[!INCLUDE[applies-to-measures-columns-tables-visual-calculations-discouraged](includes/applies-to-measures-columns-tables-visual-calculations-discouraged.md)]

Returns a table with information about each segment storage in the semantic model. This function provides metadata about segment storage characteristics.

## Syntax

```dax
INFO.SEGMENTSTORAGES()
```

## Return value

A table whose columns match the schema rowset for segment storages in the current semantic model.

## Remarks

- Typically used in DAX queries to inspect and document model metadata.
- Permissions required depend on the host. Querying full metadata may require model admin permissions.

## Example 1 - DAX query

```dax
EVALUATE
    INFO.SEGMENTSTORAGES()
```

## Example 2 - DAX query with SELECTCOLUMNS

```dax
EVALUATE
    SELECTCOLUMNS(
        INFO.SEGMENTSTORAGES(),
        "SegmentID", [SegmentID],
        "State", [State],
        "LastUpdateTime", [LastUpdateTime]
    )
```

## Example 3 - Calculated table

```dax
Segment Storages =
SELECTCOLUMNS(
    INFO.SEGMENTSTORAGES(),
    "SegmentID", [SegmentID],
    "State", [State]
)
```

## Example 4 - Measure

```dax
Number of Segment Storages =
COUNTROWS(INFO.SEGMENTSTORAGES())
```