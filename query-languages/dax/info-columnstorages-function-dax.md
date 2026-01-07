---
description: "Learn more about: INFO.COLUMNSTORAGES"
title: "INFO.COLUMNSTORAGES function (DAX)"
author: jeroenterheerdt
---
# INFO.COLUMNSTORAGES

[!INCLUDE[applies-to-query-only](includes/applies-to-query-only.md)]

Returns a table with information about each column storage in the semantic model. This function provides metadata about how columns are stored and their storage characteristics.

## Syntax

```dax
INFO.COLUMNSTORAGES ( [<Restriction name>, <Restriction value>], ... )
```

[!INCLUDE[parameters-for-info-dax-functions](includes/parameters-for-info-dax-functions.md)]

## Return value

A table with the following columns:

| Column | Data type | Description |
| ------ | --------- | ----------- |
| [ID] | Integer | Unique identifier for the column storage |
| [ColumnID] | Integer | Identifier of the column that this storage belongs to |
| [Name] | String | Name of the column storage |
| [StoragePosition] | Integer | Position of the column in storage |
| [DictionaryStorageID] | Integer | Identifier for the dictionary storage |
| [Settings] | String | Storage settings and configuration |
| [ColumnFlags] | Integer | Flags indicating column storage properties |
| [Collation] | String | Collation settings for the column |
| [OrderByColumn] | String | Column used for ordering |
| [Locale] | String | Locale information for the column |
| [BinaryCharacters] | String | Binary character information |
| [Statistics_DistinctStates] | Integer | Number of distinct states in statistics |
| [Statistics_MinDataID] | Integer | Minimum data ID in statistics |
| [Statistics_MaxDataID] | Integer | Maximum data ID in statistics |
| [Statistics_OriginalMinSegmentDataID] | Integer | Original minimum segment data ID |
| [Statistics_RLESortOrder] | Integer | RLE sort order in statistics |
| [Statistics_RowCount] | Integer | Row count in statistics |
| [Statistics_HasNulls] | Boolean | Whether statistics contain nulls |
| [Statistics_RLERuns] | Integer | Number of RLE runs in statistics |
| [Statistics_OthersRLERuns] | Integer | Number of other RLE runs |
| [Statistics_Usage] | Integer | Usage statistics |
| [Statistics_DBType] | Integer | Database type in statistics |
| [Statistics_XMType] | Integer | XML type in statistics |

## Remarks

- Typically used in DAX queries to inspect and document model metadata.
- Permissions required depend on the host. Querying full metadata may require model admin permissions.

## Example

The following DAX query can be run in [DAX query view](/power-bi/transform-model/dax-query-view):

```dax
EVALUATE
	INFO.COLUMNSTORAGES()
```

## Example 2 - DAX query with joins

The following DAX query can be run in [DAX query view](/power-bi/transform-model/dax-query-view):

```dax
EVALUATE
	VAR _ColumnStorages =
		INFO.COLUMNSTORAGES()

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

	VAR _CombinedWithColumns =
		NATURALLEFTOUTERJOIN(
			_ColumnStorages,
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
			"Storage Name", [Name],
			"Storage Position", [StoragePosition],
			"Statistics Row Count", [Statistics_RowCount]
		)
	ORDER BY [Table Name], [Column Name]
```
## See also

[INFO.COLUMNPARTITIONSTORAGES](info-columnpartitionstorages-function-dax.md)
[INFO.DICTIONARYSTORAGES](info-dictionarystorages-function-dax.md)
[INFO.SEGMENTSTORAGES](info-segmentstorages-function-dax.md)
[INFO.STORAGEFILES](info-storagefiles-function-dax.md)
[INFO.TABLESTORAGES](info-tablestorages-function-dax.md)
