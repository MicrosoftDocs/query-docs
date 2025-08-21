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

A table whose columns match the schema rowset for column permissions in the current semantic model.

## Remarks

- Typically used in DAX queries to inspect and document model metadata.
- Permissions required depend on the host. Querying full metadata may require model admin permissions.

## Example

The following DAX query can be run in [DAX query view](/power-bi/transform-model/dax-query-view):

```dax
EVALUATE
	INFO.COLUMNPERMISSIONS()
```

## Example 2 - DAX query with SELECTCOLUMNS

```dax
EVALUATE
    SELECTCOLUMNS(
        INFO.COLUMNPERMISSIONS(),
        "RoleID", [RoleID],
        "ColumnID", [ColumnID],
        "State", [State]
    )
```

## Example 3 - Calculated table

```dax
Column Permissions =
SELECTCOLUMNS(
    INFO.COLUMNPERMISSIONS(),
    "RoleID", [RoleID],
    "ColumnID", [ColumnID]
)
```

## Example 4 - Measure

```dax
Number of Column Permissions =
COUNTROWS(INFO.COLUMNPERMISSIONS())
```