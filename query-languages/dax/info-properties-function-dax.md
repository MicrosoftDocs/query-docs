---
description: "Learn more about: INFO.PROPERTIES"
title: "INFO.PROPERTIES function (DAX)"
author: jeroenterheerdt
---
# INFO.PROPERTIES

[!INCLUDE[applies-to-query-only](includes/applies-to-query-only.md)]

Returns a table with information about each property in the semantic model. This function provides metadata about properties defined for model objects.

## Syntax

```dax
INFO.PROPERTIES ( [<Restriction name>, <Restriction value>], ... )
```

[!INCLUDE[parameters-for-info-dax-functions](includes/parameters-for-info-dax-functions.md)]

## Return value

A table whose columns match the schema rowset for properties in the current semantic model.

## Remarks

- Typically used in DAX queries to inspect and document model metadata.
- Permissions required depend on the host. Querying full metadata may require model admin permissions.

## Example

The following DAX query can be run in [DAX query view](/power-bi/transform-model/dax-query-view):

```dax
EVALUATE
	INFO.PROPERTIES()
```

## Example 2 - DAX query with SELECTCOLUMNS

```dax
EVALUATE
    SELECTCOLUMNS(
        INFO.PROPERTIES(),
        "Name", [Name],
        "Value", [Value],
        "ObjectID", [ObjectID]
    )
```

## Example 3 - Calculated table

```dax
Properties =
SELECTCOLUMNS(
    INFO.PROPERTIES(),
    "Name", [Name],
    "Value", [Value]
)
```

## Example 4 - Measure

```dax
Number of Properties =
COUNTROWS(INFO.PROPERTIES())
```