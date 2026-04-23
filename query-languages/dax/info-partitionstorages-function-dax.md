---
description: "Learn more about: INFO.PARTITIONSTORAGES"
title: "INFO.PARTITIONSTORAGES function (DAX)"
author: jeroenterheerdt
---
# INFO.PARTITIONSTORAGES

[!INCLUDE[applies-to-query-only](includes/applies-to-query-only.md)]

Returns a table with information about each partition storage in the semantic model. This function provides metadata about how partitions are stored.

## Syntax

```dax
INFO.PARTITIONSTORAGES ( [<Restriction name>, <Restriction value>], ... )
```

[!INCLUDE[parameters-for-info-dax-functions](includes/parameters-for-info-dax-functions.md)]

## Return value

A table with the following columns:

| Column | Description |
|--------|-------------|
| [ID] | Unique identifier for the partition storage |
| [PartitionID] | Identifier of the partition |
| [Name] | Name of the partition storage |
| [StoragePosition] | Position of the storage within the partition |
| [SegmentMapStorageID] | Identifier linking to segment map storage |
| [DataObjectId] | Identifier of the data object |
| [StorageFolderID] | Identifier of the storage folder |
| [DeltaTableMetadataStorageID] | Identifier linking to delta table metadata storage |

## Remarks

- Typically used in DAX queries to inspect and document model metadata.
- Permissions required depend on the host. Querying full metadata may require model admin permissions.

## Example

The following DAX query can be run in [DAX query view](/power-bi/transform-model/dax-query-view):

```dax
EVALUATE
	INFO.PARTITIONSTORAGES()
```

## Example 2 - DAX query with joins

The following DAX query can be run in [DAX query view](/power-bi/transform-model/dax-query-view):

```dax
EVALUATE
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
			"Partition Name", [Name],
			"TableID", [TableID]
		)
	VAR _Tables = 
		SELECTCOLUMNS(
			INFO.TABLES(),
			"TableID", [ID],
			"Table Name", [Name]
		)
	VAR _CombinedTable1 =
		NATURALLEFTOUTERJOIN(
			_PartitionStorages,
			_Partitions
		)
	VAR _CombinedTable2 =
		NATURALLEFTOUTERJOIN(
			_CombinedTable1,
			_Tables
		)
	RETURN
		SELECTCOLUMNS(
			_CombinedTable2,
			"Table Name", [Table Name],
			"Partition Name", [Partition Name],
			"Storage Name", [Storage Name]
		)
	ORDER BY [Table Name], [Partition Name]
```

## See also

- [INFO.TABLES](info-tables-function-dax.md)
- [INFO.COLUMNS](info-columns-function-dax.md)
- [INFO.MEASURES](info-measures-function-dax.md)
- [INFO functions overview](info-functions-dax.md)
