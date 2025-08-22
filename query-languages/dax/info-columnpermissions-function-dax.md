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

## Example 2 - DAX query with joins

The following DAX query can be run in [DAX query view](/power-bi/transform-model/dax-query-view):

```dax
EVALUATE
	VAR _ColumnPermissions =
		INFO.COLUMNPERMISSIONS()

	VAR _Roles = 
		SELECTCOLUMNS(
			INFO.ROLES(),
			"RoleID", [ID],
			"Role Name", [Name]
		)

	VAR _Tables = 
		SELECTCOLUMNS(
			INFO.TABLES(),
			"TableID", [ID],
			"Table Name", [Name]
		)

	VAR _Columns = 
		SELECTCOLUMNS(
			INFO.COLUMNS(),
			"ColumnID", [ID],
			"Column Name", [ExplicitName]
		)

	VAR _CombinedWithRoles =
		NATURALLEFTOUTERJOIN(
			_ColumnPermissions,
			_Roles
		)

	VAR _CombinedWithTables =
		NATURALLEFTOUTERJOIN(
			_CombinedWithRoles,
			_Tables
		)

	VAR _CombinedWithColumns =
		NATURALLEFTOUTERJOIN(
			_CombinedWithTables,
			_Columns
		)

	RETURN
		SELECTCOLUMNS(
			_CombinedWithColumns,
			"Role Name", [Role Name],
			"Table Name", [Table Name],
			"Column Name", [Column Name],
			"Metadata Permission", [MetadataPermission]
		)
	ORDER BY [Role Name], [Table Name], [Column Name]
```