---
description: "Learn more about: INFO.MODEL"
title: "INFO.MODEL function (DAX)"
author: jeroenterheerdt
---
# INFO.MODEL

[!INCLUDE[applies-to-query-only](includes/applies-to-query-only.md)]

Returns a table with information about the model in the semantic model. This function provides metadata about the model itself and its properties.

## Syntax

```dax
INFO.MODEL ( [<Restriction name>, <Restriction value>], ... )
```

[!INCLUDE[parameters-for-info-dax-functions](includes/parameters-for-info-dax-functions.md)]

## Return value

A table whose columns match the schema rowset for the model in the current semantic model.

## Remarks

- Typically used in DAX queries to inspect and document model metadata.
- Permissions required depend on the host. Querying full metadata may require model admin permissions.

## Example

The following DAX query can be run in [DAX query view](/power-bi/transform-model/dax-query-view):

```dax
EVALUATE
	INFO.MODEL()
```

## Example 2 - DAX query with SELECTCOLUMNS

```dax
EVALUATE
    SELECTCOLUMNS(
        INFO.MODEL(),
        "Name", [Name],
        "Description", [Description],
        "Version", [Version]
    )
```

## Example 3 - Calculated table

```dax
Model Info =
SELECTCOLUMNS(
    INFO.MODEL(),
    "Name", [Name],
    "Description", [Description]
)
```

## Example 4 - Measure

```dax
Model Count =
COUNTROWS(INFO.MODEL())
```