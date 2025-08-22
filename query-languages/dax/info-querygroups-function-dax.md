---
description: "Learn more about: INFO.QUERYGROUPS"
title: "INFO.QUERYGROUPS function (DAX)"
author: jeroenterheerdt
---
# INFO.QUERYGROUPS

[!INCLUDE[applies-to-query-only](includes/applies-to-query-only.md)]

Returns a table with information about each query group in the semantic model. This function provides metadata about query groups defined in the model.

## Syntax

```dax
INFO.QUERYGROUPS ( [<Restriction name>, <Restriction value>], ... )
```

[!INCLUDE[parameters-for-info-dax-functions](includes/parameters-for-info-dax-functions.md)]

## Return value

A table whose columns match the schema rowset for query groups in the current semantic model.

## Remarks

- Typically used in DAX queries to inspect and document model metadata.
- Permissions required depend on the host. Querying full metadata may require model admin permissions.

## Example

The following DAX query can be run in [DAX query view](/power-bi/transform-model/dax-query-view):

```dax
EVALUATE
	INFO.QUERYGROUPS()
```

## Example 2 - DAX query with SELECTCOLUMNS

```dax
EVALUATE
    SELECTCOLUMNS(
        INFO.QUERYGROUPS(),
        "Name", [Name],
        "Description", [Description],
        "FolderName", [FolderName]
    )
```

## Example 3 - Calculated table

```dax
Query Groups =
SELECTCOLUMNS(
    INFO.QUERYGROUPS(),
    "Name", [Name],
    "Description", [Description]
)
```

## Example 4 - Measure

```dax
Number of Query Groups =
COUNTROWS(INFO.QUERYGROUPS())
```