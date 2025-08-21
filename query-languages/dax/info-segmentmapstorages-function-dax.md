---
description: "Learn more about: INFO.SEGMENTMAPSTORAGES"
title: "INFO.SEGMENTMAPSTORAGES function (DAX)"
author: jeroenterheerdt
---
# INFO.SEGMENTMAPSTORAGES

[!INCLUDE[applies-to-measures-columns-tables-visual-calculations-discouraged](includes/applies-to-measures-columns-tables-visual-calculations-discouraged.md)]

Returns a table with information about each segment map storage in the semantic model. This function provides metadata about segment map storage characteristics.

## Syntax

```dax
INFO.SEGMENTMAPSTORAGES()
```

## Return value

A table whose columns match the schema rowset for segment map storages in the current semantic model.

## Remarks

- Typically used in DAX queries to inspect and document model metadata.
- Permissions required depend on the host. Querying full metadata may require model admin permissions.

## Example 1 - DAX query

```dax
EVALUATE
    INFO.SEGMENTMAPSTORAGES()
```

## Example 2 - DAX query with SELECTCOLUMNS

```dax
EVALUATE
    SELECTCOLUMNS(
        INFO.SEGMENTMAPSTORAGES(),
        "SegmentMapID", [SegmentMapID],
        "State", [State],
        "LastUpdateTime", [LastUpdateTime]
    )
```

## Example 3 - Calculated table

```dax
Segment Map Storages =
SELECTCOLUMNS(
    INFO.SEGMENTMAPSTORAGES(),
    "SegmentMapID", [SegmentMapID],
    "State", [State]
)
```

## Example 4 - Measure

```dax
Number of Segment Map Storages =
COUNTROWS(INFO.SEGMENTMAPSTORAGES())
```