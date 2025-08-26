---
description: "Learn more about: INFO.REFRESHPOLICIES"
title: "INFO.REFRESHPOLICIES function (DAX)"
author: jeroenterheerdt
---
# INFO.REFRESHPOLICIES

[!INCLUDE[applies-to-query-only](includes/applies-to-query-only.md)]

Returns a table with information about each refresh policy in the semantic model. This function provides metadata about refresh policies defined for tables.

## Syntax

```dax
INFO.REFRESHPOLICIES ( [<Restriction name>, <Restriction value>], ... )
```

[!INCLUDE[parameters-for-info-dax-functions](includes/parameters-for-info-dax-functions.md)]

## Return value

A table whose columns match the schema rowset for refresh policies in the current semantic model.

## Remarks

- Typically used in DAX queries to inspect and document model metadata.
- Permissions required depend on the host. Querying full metadata may require model admin permissions.

## Example

The following DAX query can be run in [DAX query view](/power-bi/transform-model/dax-query-view):

```dax
EVALUATE
	INFO.REFRESHPOLICIES()
```

## Example 2 - DAX query with SELECTCOLUMNS

```dax
EVALUATE
    SELECTCOLUMNS(
        INFO.REFRESHPOLICIES(),
        "Name", [Name],
        "Mode", [Mode],
        "IncrementalGranularity", [IncrementalGranularity]
    )
```

## Example 3 - Calculated table

```dax
Refresh Policies =
SELECTCOLUMNS(
    INFO.REFRESHPOLICIES(),
    "Name", [Name],
    "Mode", [Mode]
)
```

## Example 4 - Measure

```dax
Number of Refresh Policies =
COUNTROWS(INFO.REFRESHPOLICIES())
```
## See also

[INFO.TABLES](info-tables-function-dax.md)
[INFO.COLUMNS](info-columns-function-dax.md)
[INFO.MEASURES](info-measures-function-dax.md)
[INFO functions overview](info-functions-dax.md)
