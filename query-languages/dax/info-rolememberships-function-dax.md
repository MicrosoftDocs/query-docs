---
description: "Learn more about: INFO.ROLEMEMBERSHIPS"
title: "INFO.ROLEMEMBERSHIPS function (DAX)"
author: jeroenterheerdt
---
# INFO.ROLEMEMBERSHIPS

[!INCLUDE[applies-to-query-only](includes/applies-to-query-only.md)]

Returns a table with information about each role membership in the semantic model. This function provides metadata about role memberships and security settings.

## Syntax

```dax
INFO.ROLEMEMBERSHIPS ( [<Restriction name>, <Restriction value>], ... )
```

[!INCLUDE[parameters-for-info-dax-functions](includes/parameters-for-info-dax-functions.md)]

## Return value

A table whose columns match the schema rowset for role memberships in the current semantic model.

## Remarks

- Typically used in DAX queries to inspect and document model metadata.
- Permissions required depend on the host. Querying full metadata may require model admin permissions.

## Example

The following DAX query can be run in [DAX query view](/power-bi/transform-model/dax-query-view):

```dax
EVALUATE
	INFO.ROLEMEMBERSHIPS()
```

## Example 2 - DAX query with SELECTCOLUMNS

```dax
EVALUATE
    SELECTCOLUMNS(
        INFO.ROLEMEMBERSHIPS(),
        "RoleID", [RoleID],
        "MemberName", [MemberName],
        "MemberType", [MemberType]
    )
```

## See also

[INFO.ROLES](info-roles-function-dax.md)
[INFO.COLUMNPERMISSIONS](info-columnpermissions-function-dax.md)
[INFO.TABLEPERMISSIONS](info-tablepermissions-function-dax.md)
[INFO.TABLES](info-tables-function-dax.md)
[INFO.COLUMNS](info-columns-function-dax.md)
