---
description: "Learn more about: INFO.COLUMNPERMISSIONS"
title: "INFO.COLUMNPERMISSIONS function (DAX)"
author: jeroenterheerdt
---
# INFO.COLUMNPERMISSIONS

[!INCLUDE[applies-to-measures-columns-tables-visual-calculations-discouraged](includes/applies-to-measures-columns-tables-visual-calculations-discouraged.md)]

Returns a table with information about each column permission in the semantic model. This function provides metadata about column-level security settings.

## Syntax

```dax
INFO.COLUMNPERMISSIONS()
```

## Return value

A table whose columns match the schema rowset for column permissions in the current semantic model.

## Remarks

- Typically used in DAX queries to inspect and document model metadata.
- Permissions required depend on the host. Querying full metadata may require model admin permissions.

## Example 1 - DAX query

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