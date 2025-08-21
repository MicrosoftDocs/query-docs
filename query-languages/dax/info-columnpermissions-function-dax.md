---
description: "Learn more about: INFO.COLUMNPERMISSIONS"
title: "INFO.COLUMNPERMISSIONS function (DAX)"
author: jeroenterheerdt
---
# INFO.COLUMNPERMISSIONS

[!INCLUDE[applies-to-query-only](includes/applies-to-query-only.md)]

Returns a table with information about each column permission in the semantic model. This function provides metadata about column-level security settings.

## Syntax

```dax
INFO.COLUMNPERMISSIONS ( [<Restriction name>, <Restriction value>], ... )
```

[!INCLUDE[parameters-for-info-dax-functions](includes/parameters-for-info-dax-functions.md)]

## Return value

A table with the following columns:

| Column name | Data type | Description |
|-------------|-----------|-------------|
| [ID] | Integer | The unique identifier of the column permission |
| [RoleID] | Integer | The identifier of the role that has the column permission |
| [TableID] | Integer | The identifier of the table containing the column |
| [ColumnID] | Integer | The identifier of the column |
| [State] | Integer | The state of the column permission |
| [MetadataPermission] | Integer | The metadata permission level for the column |

## Remarks

- Typically used in DAX queries to inspect and document model metadata.
- Permissions required depend on the host. Querying full metadata may require model admin permissions.

## Example

The following DAX query can be run in [DAX query view](/power-bi/transform-model/dax-query-view):

```dax
EVALUATE
	INFO.COLUMNPERMISSIONS()
```