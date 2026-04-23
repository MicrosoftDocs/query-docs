---
description: "Learn more about: INFO.SEGMENTMAPSTORAGES"
title: "INFO.SEGMENTMAPSTORAGES function (DAX)"
author: jeroenterheerdt
---
# INFO.SEGMENTMAPSTORAGES

[!INCLUDE[applies-to-query-only](includes/applies-to-query-only.md)]

Returns a table with information about each segment map storage in the semantic model. This function provides metadata about segment map storage characteristics.

## Syntax

```dax
INFO.SEGMENTMAPSTORAGES ( [<Restriction name>, <Restriction value>], ... )
```

[!INCLUDE[parameters-for-info-dax-functions](includes/parameters-for-info-dax-functions.md)]

## Return value

A table whose columns match the schema rowset for segment map storages in the current semantic model.

|Column|Description|
|---|---|
|ID|Unique identifier for the segment map storage|
|PartitionStorageID|Foreign key to the partition storage using this segment map|
|Type|Type of segment map storage|
|RecordCount|Number of records in the segment map|
|SegmentCount|Number of segments in the segment map|
|RecordsPerSegment|Average number of records per segment|

## Remarks

- Typically used in DAX queries to inspect and document model metadata.
- Permissions required depend on the host. Querying full metadata may require model admin permissions.

## Example

The following DAX query can be run in [DAX query view](/power-bi/transform-model/dax-query-view):

```dax
EVALUATE
	INFO.SEGMENTMAPSTORAGES()
```

### Example 2 - DAX query with joins

The following DAX query can be run in [DAX query view](/power-bi/transform-model/dax-query-view):

```dax
EVALUATE
VAR _SegmentMapStorages = 
    SELECTCOLUMNS(
        INFO.SEGMENTMAPSTORAGES(),
        "PartitionStorageID", [PartitionStorageID],
        "Type", [Type],
        "Record Count", [RecordCount],
        "Segment Count", [SegmentCount],
        "Records Per Segment", [RecordsPerSegment]
    )

VAR _PartitionStorages = 
    SELECTCOLUMNS(
        INFO.PARTITIONSTORAGES(),
        "PartitionStorageID", [ID],
        "PartitionID", [PartitionID],
        "Storage Name", [Name]
    )

VAR _Partitions = 
    SELECTCOLUMNS(
        INFO.PARTITIONS(),
        "PartitionID", [ID],
        "TableID", [TableID],
        "Partition Name", [Name]
    )

VAR _Tables = 
    SELECTCOLUMNS(
        INFO.TABLES(),
        "TableID", [ID],
        "Table Name", [Name]
    )

VAR _CombinedTable1 = 
    NATURALLEFTOUTERJOIN(
        _SegmentMapStorages,
        _PartitionStorages
    )

VAR _CombinedTable2 = 
    NATURALLEFTOUTERJOIN(
        _CombinedTable1,
        _Partitions
    )

VAR _CombinedTable3 = 
    NATURALLEFTOUTERJOIN(
        _CombinedTable2,
        _Tables
    )

RETURN
    SELECTCOLUMNS(
        _CombinedTable3,
        "Table Name", [Table Name],
        "Partition Name", [Partition Name],
        "Storage Type", [Type],
        "Record Count", [Record Count],
        "Segment Count", [Segment Count],
        "Records Per Segment", [Records Per Segment]
    )
ORDER BY [Table Name], [Partition Name]
```

## See also

- [INFO.TABLES](info-tables-function-dax.md)
- [INFO.COLUMNS](info-columns-function-dax.md)
- [INFO.MEASURES](info-measures-function-dax.md)
- [INFO functions overview](info-functions-dax.md)
