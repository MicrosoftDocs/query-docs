---
description: "Learn more about: INFO.CHANGEDPROPERTIES"
title: "INFO.CHANGEDPROPERTIES function (DAX)"
author: jeroenterheerdt
---
# INFO.CHANGEDPROPERTIES

[!INCLUDE[applies-to-measures-columns-tables-visual-calculations-discouraged](includes/applies-to-measures-columns-tables-visual-calculations-discouraged.md)]

Returns a table with information about each changed property in the semantic model. This function provides metadata about properties that have been modified in the model.

## Syntax

```dax
INFO.CHANGEDPROPERTIES()
```

## Return value

A table whose columns match the schema rowset for changed properties in the current semantic model.

## Remarks

- Typically used in DAX queries to inspect and document model metadata.
- Permissions required depend on the host. Querying full metadata may require model admin permissions.

## Example 1 - DAX query

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