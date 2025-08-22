---
description: "Learn more about: INFO.PARTITIONS"
title: "INFO.PARTITIONS function (DAX)"
author: jeroenterheerdt
---
# INFO.PARTITIONS

[!INCLUDE[applies-to-query-only](includes/applies-to-query-only.md)]

Returns a table with information about each partition in the semantic model. This function provides metadata about table partitions and their properties.

## Syntax

```dax
INFO.PARTITIONS ( [<Restriction name>, <Restriction value>], ... )
```

[!INCLUDE[parameters-for-info-dax-functions](includes/parameters-for-info-dax-functions.md)]

## Return value

A table with the following columns:

| Column | Data Type | Description |
|--------|-----------|-------------|
| [ID] | Integer | Unique identifier for the partition |
| [TableID] | Integer | ID of the table this partition belongs to |
| [Name] | String | Name of the partition |
| [Description] | String | Description of the partition |
| [DataSourceID] | Integer | ID of the data source for this partition |
| [QueryDefinition] | String | Query definition used to populate the partition |
| [State] | Integer | Current state of the partition |
| [Type] | Integer | Type of partition |
| [PartitionStorageID] | Integer | ID of the partition storage |
| [Mode] | Integer | Processing mode for the partition |
| [DataView] | Integer | Data view setting for the partition |
| [ModifiedTime] | DateTime | Date and time when the partition was last modified |
| [RefreshedTime] | DateTime | Date and time when the partition was last refreshed |
| [SystemFlags] | Integer | System flags for the partition |
| [ErrorMessage] | String | Error message if the partition is in an error state |
| [RetainDataTillForceCalculate] | Boolean | Whether to retain data until force calculate |
| [RangeStart] | String | Start range for incremental refresh, if applicable |
| [RangeEnd] | String | End range for incremental refresh, if applicable |
| [RangeGranularity] | Integer | Granularity for range-based partitioning |
| [RefreshBookmark] | String | Bookmark for incremental refresh operations |
| [QueryGroupID] | Integer | ID of the query group this partition belongs to |
| [ExpressionSourceID] | Integer | ID of the expression source |
| [MAttributes] | String | Additional partition attributes |

## Remarks

- Typically used in DAX queries to inspect and document model metadata.
- Permissions required depend on the host. Querying full metadata may require model admin permissions.

## Example

The following DAX query can be run in [DAX query view](/power-bi/transform-model/dax-query-view):

```dax
EVALUATE
	INFO.PARTITIONS()
```