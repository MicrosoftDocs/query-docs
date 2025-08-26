---
description: "Learn more about: INFO.DICTIONARYSTORAGES"
title: "INFO.DICTIONARYSTORAGES function (DAX)"
author: jeroenterheerdt
---
# INFO.DICTIONARYSTORAGES

[!INCLUDE[applies-to-query-only](includes/applies-to-query-only.md)]

Returns a table with information about each dictionary storage in the semantic model. This function provides metadata about dictionary storage characteristics and compression.

## Syntax

```dax
INFO.DICTIONARYSTORAGES ( [<Restriction name>, <Restriction value>], ... )
```

[!INCLUDE[parameters-for-info-dax-functions](includes/parameters-for-info-dax-functions.md)]

## Return value

A table with the following columns:

| Column name | Data type | Description |
| --- | --- | --- |
| [ID] | Integer | Unique identifier for the dictionary storage |
| [ColumnStorageID] | Integer | Identifier of the column storage this dictionary belongs to |
| [Type] | Integer | Type of the dictionary storage |
| [DataType] | Integer | Data type stored in the dictionary |
| [DataVersion] | Integer | Version of the data format |
| [BaseId] | Integer | Base identifier for the dictionary |
| [Magnitude] | Integer | Magnitude value for the dictionary |
| [LastId] | Integer | Last identifier used in the dictionary |
| [IsNullable] | Boolean | Whether the dictionary can contain null values |
| [IsUnique] | Boolean | Whether all values in the dictionary are unique |
| [IsOperatingOn32] | Boolean | Whether the dictionary operates on 32-bit values |
| [DictionaryFlags] | Integer | Flags indicating dictionary characteristics |
| [StorageFileID] | Integer | Identifier of the storage file containing the dictionary |
| [Size] | Integer | Size of the dictionary in bytes |

## Remarks

- Typically used in DAX queries to inspect and document model metadata.
- Permissions required depend on the host. Querying full metadata may require model admin permissions.

## Example

The following DAX query can be run in [DAX query view](/power-bi/transform-model/dax-query-view):

```dax
EVALUATE
	INFO.DICTIONARYSTORAGES()
```

## Example 2 - DAX query with joins

The following DAX query can be run in [DAX query view](/power-bi/transform-model/dax-query-view):

```dax
EVALUATE
	VAR _DictionaryStorages =
		INFO.DICTIONARYSTORAGES()

	VAR _ColumnStorages = 
		SELECTCOLUMNS(
			INFO.COLUMNSTORAGES(),
			"ColumnStorageID", [ID],
			"Column Storage Name", [Name],
			"ColumnID", [ColumnID]
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
			_DictionaryStorages,
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
			"Dictionary Type", [Type],
			"Data Type", [DataType],
			"Is Nullable", [IsNullable],
			"Size", [Size]
		)
	ORDER BY [Table Name], [Column Name]
```
## See also

[INFO.COLUMNSTORAGES](info-columnstorages-function-dax.md)
[INFO.COLUMNPARTITIONSTORAGES](info-columnpartitionstorages-function-dax.md)
[INFO.SEGMENTSTORAGES](info-segmentstorages-function-dax.md)
[INFO.STORAGEFILES](info-storagefiles-function-dax.md)
[INFO.TABLESTORAGES](info-tablestorages-function-dax.md)
