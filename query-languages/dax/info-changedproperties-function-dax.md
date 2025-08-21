---
description: "Learn more about: INFO.CHANGEDPROPERTIES"
title: "INFO.CHANGEDPROPERTIES function (DAX)"
author: jeroenterheerdt
---
# INFO.CHANGEDPROPERTIES

[!INCLUDE[applies-to-query-only](includes/applies-to-query-only.md)]

Returns a table with information about each changed property in the semantic model. This function provides metadata about properties that have been modified in the model.

## Syntax

```dax
INFO.CHANGEDPROPERTIES ( [<Restriction name>, <Restriction value>], ... )
```

[!INCLUDE[parameters-for-info-dax-functions](includes/parameters-for-info-dax-functions.md)]

## Return value

A table whose columns match the schema rowset for changed properties in the current semantic model.

## Remarks

- Typically used in DAX queries to inspect and document model metadata.
- Permissions required depend on the host. Querying full metadata may require model admin permissions.

## Example

The following DAX query can be run in [DAX query view](/power-bi/transform-model/dax-query-view):

```dax
EVALUATE
	INFO.CHANGEDPROPERTIES()
```

## Example 2 - DAX query with SELECTCOLUMNS

```dax
EVALUATE
    SELECTCOLUMNS(
        INFO.CHANGEDPROPERTIES(),
        "ObjectID", [ObjectID],
        "PropertyName", [PropertyName],
        "Value", [Value]
    )
```

## Example 3 - Calculated table

```dax
Changed Properties =
SELECTCOLUMNS(
    INFO.CHANGEDPROPERTIES(),
    "ObjectID", [ObjectID],
    "PropertyName", [PropertyName]
)
```

## Example 4 - Measure

```dax
Number of Changed Properties =
COUNTROWS(INFO.CHANGEDPROPERTIES())
```