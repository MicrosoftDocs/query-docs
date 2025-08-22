---
description: "Learn more about: INFO.DELTATABLEMETADATASTORAGES"
title: "INFO.DELTATABLEMETADATASTORAGES function (DAX)"
author: jeroenterheerdt
---
# INFO.DELTATABLEMETADATASTORAGES

[!INCLUDE[applies-to-query-only](includes/applies-to-query-only.md)]

Returns a table with information about each delta table metadata storage in the semantic model. This function provides metadata about delta table storage characteristics.

## Syntax

```dax
INFO.DELTATABLEMETADATASTORAGES ( [<Restriction name>, <Restriction value>], ... )
```

[!INCLUDE[parameters-for-info-dax-functions](includes/parameters-for-info-dax-functions.md)]

## Return value

A table with the following columns:

| Column name | Data type | Description |
| --- | --- | --- |
| [ID] | Integer | Unique identifier for the delta table metadata storage |
| [PartitionStorageID] | Integer | Identifier of the partition storage |
| [DataSourceReference] | String | Reference to the data source |
| [TableName] | String | Name of the delta table |
| [RootLocation] | String | Root location of the delta table |
| [CurrentVersion] | Integer | Current version of the delta table |
| [TableObjectID] | String | Object identifier for the table |
| [DatamartObjectID] | String | Object identifier for the datamart |
| [FramedSchemaName] | String | Name of the framed schema |
| [FallbackReason] | String | Reason for fallback behavior |
| [DeltaColumnMappingMode] | String | Column mapping mode for the delta table |
| [DeltaLogETag] | String | ETag for the delta log |
| [ArtifactObjectId] | String | Object identifier for the artifact |
| [ArtifactSecurityVersion] | String | Security version of the artifact |

## Remarks

- Typically used in DAX queries to inspect and document model metadata.
- Permissions required depend on the host. Querying full metadata may require model admin permissions.

## Example

The following DAX query can be run in [DAX query view](/power-bi/transform-model/dax-query-view):

```dax
EVALUATE
	INFO.DELTATABLEMETADATASTORAGES()
```

