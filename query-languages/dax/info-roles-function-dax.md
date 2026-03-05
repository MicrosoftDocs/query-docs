---
description: "Learn more about: INFO.ROLES"
title: "INFO.ROLES function (DAX)"
author: jeroenterheerdt
---
# INFO.ROLES

[!INCLUDE[applies-to-query-only](includes/applies-to-query-only.md)]

Returns a table with information about each role in the semantic model. This function provides metadata about security roles defined in the model.

## Syntax

```dax
INFO.ROLES ( [<Restriction name>, <Restriction value>], ... )
```

[!INCLUDE[parameters-for-info-dax-functions](includes/parameters-for-info-dax-functions.md)]

## Return value

A table whose columns match the schema rowset for roles in the current semantic model.

|Column|Description|
|---|---|
|ID|Unique identifier for the role|
|ModelID|Foreign key to the model containing this role|
|Name|Name of the role|
|Description|Description of the role|
|ModelPermission|Permission level for the role (e.g., Read, ReadRefresh, Administrator)|
|ModifiedTime|Date and time when the role was last modified|

## Remarks

- Typically used in DAX queries to inspect and document model metadata.
- Permissions required depend on the host. Querying full metadata may require model admin permissions.

## Example

The following DAX query can be run in [DAX query view](/power-bi/transform-model/dax-query-view):

```dax
EVALUATE
	INFO.ROLES()
```

### Example 2 - DAX query with joins

The following DAX query can be run in [DAX query view](/power-bi/transform-model/dax-query-view):

```dax
EVALUATE
VAR _Roles = 
    SELECTCOLUMNS(
        INFO.ROLES(),
        "RoleID", [ID],
        "Role Name", [Name],
        "Role Description", [Description],
        "Model Permission", [ModelPermission],
        "Modified", [ModifiedTime]
    )

VAR _RoleMemberships = 
    SELECTCOLUMNS(
        INFO.ROLEMEMBERSHIPS(),
        "RoleID", [RoleID],
        "Member Name", [MemberName],
        "Member Type", [MemberType]
    )

VAR _CombinedTable = 
    NATURALLEFTOUTERJOIN(
        _Roles,
        _RoleMemberships
    )

RETURN
    SELECTCOLUMNS(
        _CombinedTable,
        "Role Name", [Role Name],
        "Role Description", [Role Description],
        "Model Permission", [Model Permission],
        "Member Name", [Member Name],
        "Member Type", [Member Type],
        "Modified", [Modified]
    )
ORDER BY [Role Name], [Member Name]
```

## See also

- [INFO.ROLEMEMBERSHIPS](info-rolememberships-function-dax.md)
- [INFO.COLUMNPERMISSIONS](info-columnpermissions-function-dax.md)
- [INFO.TABLEPERMISSIONS](info-tablepermissions-function-dax.md)
- [INFO.TABLES](info-tables-function-dax.md)
- [INFO.COLUMNS](info-columns-function-dax.md)
