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

|Column|Description|
|---|---|
|ID|Unique identifier for the role membership|
|RoleID|Foreign key to the role containing this membership|
|MemberName|Name of the member (user or group)|
|MemberID|Unique identifier for the member|
|IdentityProvider|Identity provider for the member authentication|
|MemberType|Type of member (e.g., User, Group)|
|ModifiedTime|Date and time when the role membership was last modified|

## Remarks

- Typically used in DAX queries to inspect and document model metadata.
- Permissions required depend on the host. Querying full metadata may require model admin permissions.

## Example

The following DAX query can be run in [DAX query view](/power-bi/transform-model/dax-query-view):

```dax
EVALUATE
	INFO.ROLEMEMBERSHIPS()
```

## See also

- [INFO.ROLES](info-roles-function-dax.md)
- [INFO.COLUMNPERMISSIONS](info-columnpermissions-function-dax.md)
- [INFO.TABLEPERMISSIONS](info-tablepermissions-function-dax.md)
- [INFO.TABLES](info-tables-function-dax.md)
- [INFO.COLUMNS](info-columns-function-dax.md)
