---
description: "Learn more about: INFO.GENERALSEGMENTMAPSEGMENTMETADATASTORAGES"
title: "INFO.GENERALSEGMENTMAPSEGMENTMETADATASTORAGES function (DAX)"
author: jeroenterheerdt
---
# INFO.GENERALSEGMENTMAPSEGMENTMETADATASTORAGES

[!INCLUDE[applies-to-query-only](includes/applies-to-query-only.md)]

Returns a table with information about each general segment map segment metadata storage in the semantic model. This function provides metadata about segment map storage characteristics.

## Syntax

```dax
INFO.GENERALSEGMENTMAPSEGMENTMETADATASTORAGES ( [<Restriction name>, <Restriction value>], ... )
```

[!INCLUDE[parameters-for-info-dax-functions](includes/parameters-for-info-dax-functions.md)]

## Return value

A table whose columns match the schema rowset for general segment map segment metadata storages in the current semantic model.

## Remarks

- Typically used in DAX queries to inspect and document model metadata.
- Permissions required depend on the host. Querying full metadata may require model admin permissions.

## Example

The following DAX query can be run in [DAX query view](/power-bi/transform-model/dax-query-view):

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