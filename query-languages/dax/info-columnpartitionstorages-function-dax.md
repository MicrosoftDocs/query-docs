---
description: "Learn more about: INFO.COLUMNPARTITIONSTORAGES"
title: "INFO.COLUMNPARTITIONSTORAGES function (DAX)"
author: jeroenterheerdt
---
# INFO.COLUMNPARTITIONSTORAGES

[!INCLUDE[applies-to-query-only](includes/applies-to-query-only.md)]

Returns a table with information about each column partition storage in the semantic model. This function provides metadata about how column partitions are stored.

## Syntax

```dax
INFO.COLUMNPARTITIONSTORAGES ( [<Restriction name>, <Restriction value>], ... )
```

[!INCLUDE[parameters-for-info-dax-functions](includes/parameters-for-info-dax-functions.md)]

## Return value

A table with the following columns:

| Column name | Data type | Description |
|-------------|-----------|-------------|
| [ID] | Integer | The unique identifier of the column partition storage |
| [ColumnStorageID] | Integer | The identifier of the column storage this partition belongs to |
| [PartitionStorageID] | Integer | The identifier of the partition storage |
| [DataVersion] | Integer | The version of the data in the partition storage |
| [State] | Integer | The current state of the column partition storage |
| [SegmentStorageID] | Integer | The identifier of the segment storage |
| [StorageFileID] | Integer | The identifier of the storage file |

## Remarks

- Typically used in DAX queries to inspect and document model metadata.
- Permissions required depend on the host. Querying full metadata may require model admin permissions.

## Example

The following DAX query can be run in [DAX query view](/power-bi/transform-model/dax-query-view):

```dax
EVALUATE
	INFO.COLUMNPARTITIONSTORAGES()
```

## Example 2 - DAX query with joins

The following DAX query can be run in [DAX query view](/power-bi/transform-model/dax-query-view):

```dax
EVALUATE
	VAR _ColumnPartitionStorages =
		INFO.COLUMNPARTITIONSTORAGES()

	VAR _ColumnStorages = 
		SELECTCOLUMNS(
			INFO.COLUMNSTORAGES(),
			"ColumnStorageID", [ID],
			"ColumnID", [ColumnID],
			"Storage Name", [Name]
		)

	VAR _Columns = 
		SELECTCOLUMNS(
			INFO.COLUMNS(),
			"ColumnID", [ID],
			"Column Name", [ExplicitName],
			"TableID", [TableID]
		)

	VAR _Tables = 
		SELECTCOLUMNS(
			INFO.TABLES(),
			"TableID", [ID],
			"Table Name", [Name]
		)

	VAR _CombinedWithColumnStorages =
		NATURALLEFTOUTERJOIN(
			_ColumnPartitionStorages,
			_ColumnStorages
		)

	VAR _CombinedWithColumns =
		NATURALLEFTOUTERJOIN(
			_CombinedWithColumnStorages,
			_Columns
		)

	VAR _CombinedWithTables =
		NATURALLEFTOUTERJOIN(
			_CombinedWithColumns,
			_Tables
		)

	RETURN
		SELECTCOLUMNS(
			_CombinedWithTables,
			"Table Name", [Table Name],
			"Column Name", [Column Name],
			"Storage Name", [Storage Name],
			"Data Version", [DataVersion],
			"State", [State]
		)
	ORDER BY [Table Name], [Column Name]
```
## See also

- [INFO.COLUMNSTORAGES](info-columnstorages-function-dax.md)
- [INFO.DICTIONARYSTORAGES](info-dictionarystorages-function-dax.md)
- [INFO.SEGMENTSTORAGES](info-segmentstorages-function-dax.md)
- [INFO.STORAGEFILES](info-storagefiles-function-dax.md)
- [INFO.TABLESTORAGES](info-tablestorages-function-dax.md)
