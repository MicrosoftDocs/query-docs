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
| [TablePermissionID] | Integer | The identifier of the table permission this column permission belongs to |
| [ColumnID] | Integer | The identifier of the column |
| [ModifiedTime] | DateTime | The date and time when the column permission was last modified |
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

	VAR _TablePermissions = 
		SELECTCOLUMNS(
			INFO.TABLEPERMISSIONS(),
			"TablePermissionID", [ID],
			"Table Permission Name", [Name],
			"RoleID", [RoleID],
			"TableID", [TableID]
		)

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

	VAR _CombinedWithTablePermissions =
		NATURALLEFTOUTERJOIN(
			_ColumnPermissions,
			_TablePermissions
		)

	VAR _CombinedWithRoles =
		NATURALLEFTOUTERJOIN(
			_CombinedWithTablePermissions,
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
			"Metadata Permission", [MetadataPermission],
			"Modified Time", [ModifiedTime]
		)
	ORDER BY [Role Name], [Table Name], [Column Name]
```
## See also

[INFO.ROLES](info-roles-function-dax.md)
[INFO.ROLEMEMBERSHIPS](info-rolememberships-function-dax.md)
[INFO.TABLEPERMISSIONS](info-tablepermissions-function-dax.md)
[INFO.TABLES](info-tables-function-dax.md)
[INFO.COLUMNS](info-columns-function-dax.md)
