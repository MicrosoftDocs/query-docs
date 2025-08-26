---
description: "Learn more about: INFO.SEGMENTSTORAGES"
title: "INFO.SEGMENTSTORAGES function (DAX)"
author: jeroenterheerdt
---
# INFO.SEGMENTSTORAGES

[!INCLUDE[applies-to-query-only](includes/applies-to-query-only.md)]

Returns a table with information about each segment storage in the semantic model. This function provides metadata about segment storage characteristics.

## Syntax

```dax
INFO.SEGMENTSTORAGES ( [<Restriction name>, <Restriction value>], ... )
```

[!INCLUDE[parameters-for-info-dax-functions](includes/parameters-for-info-dax-functions.md)]

## Return value

A table whose columns match the schema rowset for segment storages in the current semantic model.

|Column|Description|
|---|---|
|ID|Unique identifier for the segment storage|
|ColumnPartitionStorageID|Foreign key to the column partition storage using this segment|
|SegmentCount|Number of segments in the storage|
|StorageFileID|Foreign key to the storage file containing the segment data|

## Remarks

- Typically used in DAX queries to inspect and document model metadata.
- Permissions required depend on the host. Querying full metadata may require model admin permissions.

## Example

The following DAX query can be run in [DAX query view](/power-bi/transform-model/dax-query-view):

```dax
EVALUATE
	INFO.SEGMENTSTORAGES()
```

### Example 2 - DAX query with joins

The following DAX query can be run in [DAX query view](/power-bi/transform-model/dax-query-view):

```dax
EVALUATE
VAR _SegmentStorages = 
    SELECTCOLUMNS(
        INFO.SEGMENTSTORAGES(),
        "ColumnPartitionStorageID", [ColumnPartitionStorageID],
        "Segment Count", [SegmentCount],
        "StorageFileID", [StorageFileID]
    )

VAR _ColumnPartitionStorages = 
    SELECTCOLUMNS(
        INFO.COLUMNPARTITIONSTORAGES(),
        "ColumnPartitionStorageID", [ID],
        "ColumnStorageID", [ColumnStorageID],
        "PartitionStorageID", [PartitionStorageID]
    )

VAR _StorageFiles = 
    SELECTCOLUMNS(
        INFO.STORAGEFILES(),
        "StorageFileID", [ID],
        "File Name", [FileName]
    )

VAR _CombinedTable1 = 
    NATURALLEFTOUTERJOIN(
        _SegmentStorages,
        _ColumnPartitionStorages
    )

VAR _CombinedTable2 = 
    NATURALLEFTOUTERJOIN(
        _CombinedTable1,
        _StorageFiles
    )

RETURN
    SELECTCOLUMNS(
        _CombinedTable2,
        "Column Storage ID", [ColumnStorageID],
        "Partition Storage ID", [PartitionStorageID],
        "Segment Count", [Segment Count],
        "File Name", [File Name]
    )
ORDER BY [Column Storage ID]
```

## See also

[INFO.COLUMNSTORAGES](info-columnstorages-function-dax.md)
[INFO.COLUMNPARTITIONSTORAGES](info-columnpartitionstorages-function-dax.md)
[INFO.DICTIONARYSTORAGES](info-dictionarystorages-function-dax.md)
[INFO.STORAGEFILES](info-storagefiles-function-dax.md)
[INFO.TABLESTORAGES](info-tablestorages-function-dax.md)
