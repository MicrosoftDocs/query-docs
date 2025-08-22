---
description: "Learn more about: INFO.PARQUETFILESTORAGES"
title: "INFO.PARQUETFILESTORAGES function (DAX)"
author: jeroenterheerdt
---
# INFO.PARQUETFILESTORAGES

[!INCLUDE[applies-to-query-only](includes/applies-to-query-only.md)]

Returns a table with information about each Parquet file storage in the semantic model. This function provides metadata about Parquet file storage characteristics.

## Syntax

```dax
INFO.PARQUETFILESTORAGES ( [<Restriction name>, <Restriction value>], ... )
```

[!INCLUDE[parameters-for-info-dax-functions](includes/parameters-for-info-dax-functions.md)]

## Return value

A table with the following columns:

| Column | Data Type | Description |
|--------|-----------|-------------|
| [ID] | Integer | Unique identifier for the Parquet file storage |
| [DeltaTableMetadataStorageID] | Integer | ID of the associated delta table metadata storage |
| [Size] | Integer | Size of the Parquet file in bytes |
| [Location] | String | Location path of the Parquet file |
| [CreatedVersion] | Integer | Version when the file was created |
| [DeletedVersion] | Integer | Version when the file was deleted, if applicable |
| [RowgroupCount] | Integer | Number of row groups in the Parquet file |
| [Ordinal] | Integer | Ordinal position of the file |
| [ETag] | String | Entity tag for file versioning and caching |
| [DeletionVectorFileLocation] | String | Location of the deletion vector file |
| [DeletionVectorBitmapOffset] | Integer | Offset for the deletion vector bitmap |
| [DeletionVectorBitmapSize] | Integer | Size of the deletion vector bitmap |
| [DeletionVectorFileETag] | String | Entity tag for the deletion vector file |

## Remarks

- Typically used in DAX queries to inspect and document model metadata.
- Permissions required depend on the host. Querying full metadata may require model admin permissions.

## Example

The following DAX query can be run in [DAX query view](/power-bi/transform-model/dax-query-view):

```dax
EVALUATE
	INFO.PARQUETFILESTORAGES()
```