---
description: "Learn more about: INFO.EXTENDEDPROPERTIES"
title: "INFO.EXTENDEDPROPERTIES function (DAX)"
author: jeroenterheerdt
---
# INFO.EXTENDEDPROPERTIES

[!INCLUDE[applies-to-measures-columns-tables-visual-calculations-discouraged](includes/applies-to-measures-columns-tables-visual-calculations-discouraged.md)]

Returns a table with information about each extended property in the semantic model. This function provides metadata about extended properties defined for model objects.

## Syntax

```dax
INFO.EXTENDEDPROPERTIES()
```

## Return value

A table whose columns match the schema rowset for extended properties in the current semantic model.

## Remarks

- Typically used in DAX queries to inspect and document model metadata.
- Permissions required depend on the host. Querying full metadata may require model admin permissions.

## Example 1 - DAX query

```dax
EVALUATE
    INFO.EXTENDEDPROPERTIES()
```

## Example 2 - DAX query with SELECTCOLUMNS

```dax
EVALUATE
    SELECTCOLUMNS(
        INFO.EXTENDEDPROPERTIES(),
        "Name", [Name],
        "Value", [Value],
        "ObjectID", [ObjectID]
    )
```

## Example 3 - Calculated table

```dax
Extended Properties =
SELECTCOLUMNS(
    INFO.EXTENDEDPROPERTIES(),
    "Name", [Name],
    "Value", [Value]
)
```

## Example 4 - Measure

```dax
Number of Extended Properties =
COUNTROWS(INFO.EXTENDEDPROPERTIES())
```