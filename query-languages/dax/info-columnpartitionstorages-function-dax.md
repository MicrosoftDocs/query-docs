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
| [TableID] | Integer | The identifier of the table containing the column |
| [ColumnID] | Integer | The identifier of the column |
| [PartitionID] | Integer | The identifier of the partition |
| [SegmentID] | Integer | The identifier of the segment |
| [State] | Integer | The state of the column partition storage |
| [DataSize] | Long | The size of the data in the storage |
| [DictionarySize] | Long | The size of the dictionary in the storage |
| [HierarchiesSize] | Long | The size of hierarchies in the storage |

## Remarks

- Typically used in DAX queries to inspect and document model metadata.
- Permissions required depend on the host. Querying full metadata may require model admin permissions.

## Example

The following DAX query can be run in [DAX query view](/power-bi/transform-model/dax-query-view):

```dax
EVALUATE
	INFO.COLUMNPARTITIONSTORAGES()
```