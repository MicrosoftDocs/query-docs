---
description: "Learn more about: INFO.GENERALSEGMENTMAPSEGMENTMETADATASTORAGES"
title: "INFO.GENERALSEGMENTMAPSEGMENTMETADATASTORAGES function (DAX)"
author: jeroenterheerdt
---
# INFO.GENERALSEGMENTMAPSEGMENTMETADATASTORAGES

[!INCLUDE[applies-to-measures-columns-tables-visual-calculations-discouraged](includes/applies-to-measures-columns-tables-visual-calculations-discouraged.md)]

Returns a table with information about each general segment map segment metadata storage in the semantic model. This function provides metadata about segment map storage characteristics.

## Syntax

```dax
INFO.GENERALSEGMENTMAPSEGMENTMETADATASTORAGES()
```

## Return value

A table whose columns match the schema rowset for general segment map segment metadata storages in the current semantic model.

## Remarks

- Typically used in DAX queries to inspect and document model metadata.
- Permissions required depend on the host. Querying full metadata may require model admin permissions.

## Example 1 - DAX query

```dax
EVALUATE
    INFO.GENERALSEGMENTMAPSEGMENTMETADATASTORAGES()
```

## Example 2 - DAX query with SELECTCOLUMNS

```dax
EVALUATE
    SELECTCOLUMNS(
        INFO.GENERALSEGMENTMAPSEGMENTMETADATASTORAGES(),
        "SegmentMapID", [SegmentMapID],
        "State", [State],
        "LastUpdateTime", [LastUpdateTime]
    )
```

## Example 3 - Calculated table

```dax
General Segment Map Storages =
SELECTCOLUMNS(
    INFO.GENERALSEGMENTMAPSEGMENTMETADATASTORAGES(),
    "SegmentMapID", [SegmentMapID],
    "State", [State]
)
```

## Example 4 - Measure

```dax
Number of General Segment Map Storages =
COUNTROWS(INFO.GENERALSEGMENTMAPSEGMENTMETADATASTORAGES())
```