---
description: "Learn more about: INFO.COLUMNS"
title: "INFO.COLUMNS function (DAX)"
author: jeroenterheerdt
---
# INFO.COLUMNS

[!INCLUDE[applies-to-query-only](includes/applies-to-query-only.md)]

Returns a table with information about each column in the semantic model. This function provides metadata about all columns including their properties and characteristics.

## Syntax

```dax
INFO.COLUMNS ( [<Restriction name>, <Restriction value>], ... )
```

[!INCLUDE[parameters-for-info-dax-functions](includes/parameters-for-info-dax-functions.md)]

## Return value

A table with the following columns:

| Column | Data type | Description |
| ------ | --------- | ----------- |
| [ID] | Integer | Unique identifier for the column |
| [TableID] | Integer | Identifier of the table that contains this column |
| [ExplicitName] | String | The explicitly defined name of the column |
| [InferredName] | String | The inferred name of the column |
| [ExplicitDataType] | Integer | The explicitly defined data type of the column |
| [InferredDataType] | Integer | The inferred data type of the column |
| [DataCategory] | String | The data category classification for the column |
| [Description] | String | The description of the column |
| [IsHidden] | Boolean | Whether the column is hidden from client tools |
| [State] | Integer | The current state of the column |
| [IsUnique] | Boolean | Whether the column contains unique values |
| [IsKey] | Boolean | Whether the column is a key column |
| [IsNullable] | Boolean | Whether the column can contain null values |
| [Alignment] | Integer | The alignment setting for the column |
| [TableDetailPosition] | Integer | The position of the column in table detail views |
| [IsDefaultLabel] | Boolean | Whether this column is the default label |
| [IsDefaultImage] | Boolean | Whether this column is the default image |
| [SummarizeBy] | Integer | How the column should be summarized |
| [ColumnStorageID] | Integer | Identifier for the column's storage |
| [Type] | Integer | The type classification of the column |
| [SourceColumn] | String | The source column name |
| [ColumnOriginID] | Integer | Identifier for the column's origin |
| [Expression] | String | The DAX expression for calculated columns |
| [FormatString] | String | The format string for the column |
| [IsAvailableInMDX] | Boolean | Whether the column is available in MDX queries |
| [SortByColumnID] | Integer | Identifier of the column to sort by |
| [AttributeHierarchyID] | Integer | Identifier of the attribute hierarchy |
| [ModifiedTime] | DateTime | When the column was last modified |
| [StructureModifiedTime] | DateTime | When the column structure was last modified |
| [RefreshedTime] | DateTime | When the column data was last refreshed |
| [SystemFlags] | Integer | System flags for the column |
| [KeepUniqueRows] | Boolean | Whether to keep unique rows |
| [DisplayOrdinal] | Integer | The display order of the column |
| [ErrorMessage] | String | Any error message associated with the column |
| [SourceProviderType] | String | The source provider type |
| [DisplayFolder] | String | The display folder for organizing columns |
| [EncodingHint] | Integer | Encoding hint for the column |
| [RelatedColumnDetailsID] | Integer | Identifier for related column details |
| [AlternateOfID] | Integer | Identifier if this is an alternate of another column |
| [LineageTag] | String | The lineage tag for tracking column lineage |
| [SourceLineageTag] | String | The source lineage tag |

## Remarks

- Typically used in DAX queries to inspect and document model metadata.
- Permissions required depend on the host. Querying full metadata may require model admin permissions.

## Example

The following DAX query can be run in [DAX query view](/power-bi/transform-model/dax-query-view):

```dax
EVALUATE
	INFO.COLUMNS()
```

## Example 2 - DAX query with joins

The following DAX query can be run in [DAX query view](/power-bi/transform-model/dax-query-view):

```dax
EVALUATE
	VAR _Columns =
		INFO.COLUMNS()

	VAR _Tables = 
		SELECTCOLUMNS(
			INFO.TABLES(),
			"TableID", [ID],
			"Table Name", [Name]
		)

	VAR _CombinedTable =
		NATURALLEFTOUTERJOIN(
			_Columns,
			_Tables
		)

	RETURN
		SELECTCOLUMNS(
			_CombinedTable,
			"Table Name", [Table Name],
			"Column Name", [ExplicitName],
			"Data Type", [ExplicitDataType],
			"Is Hidden", [IsHidden],
			"Is Key", [IsKey]
		)
	ORDER BY [Table Name], [Column Name]
```

