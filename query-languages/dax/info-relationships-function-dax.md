---
description: "Learn more about: INFO.RELATIONSHIPS"
title: "INFO.RELATIONSHIPS function (DAX)"
author: jeroenterheerdt
---
# INFO.RELATIONSHIPS

[!INCLUDE[applies-to-query-only](includes/applies-to-query-only.md)]

Returns a table with information about each relationship in the semantic model. This function provides metadata about relationships between tables.

## Syntax

```dax
INFO.RELATIONSHIPS ( [<Restriction name>, <Restriction value>], ... )
```

[!INCLUDE[parameters-for-info-dax-functions](includes/parameters-for-info-dax-functions.md)]

## Return value

A table whose columns match the schema rowset for relationships in the current semantic model.

## Remarks

- Typically used in DAX queries to inspect and document model metadata.
- Permissions required depend on the host. Querying full metadata may require model admin permissions.

## Example

The following DAX query can be run in [DAX query view](/power-bi/transform-model/dax-query-view):

```dax
EVALUATE
	INFO.RELATIONSHIPS()
```

## Example 2 - DAX query with SELECTCOLUMNS

```dax
EVALUATE
    SELECTCOLUMNS(
        INFO.RELATIONSHIPS(),
        "Name", [Name],
        "IsActive", [IsActive],
        "CrossFilteringBehavior", [CrossFilteringBehavior]
    )
```

## Example 3 - Calculated table

```dax
Relationships =
SELECTCOLUMNS(
    INFO.RELATIONSHIPS(),
    "Name", [Name],
    "IsActive", [IsActive]
)
```

## Example 4 - Measure

```dax
Number of Relationships =
COUNTROWS(INFO.RELATIONSHIPS())
```
## See also

[INFO.TABLES](info-tables-function-dax.md)
[INFO.COLUMNS](info-columns-function-dax.md)
[INFO.PARTITIONS](info-partitions-function-dax.md)
[INFO functions overview](info-functions-dax.md)
