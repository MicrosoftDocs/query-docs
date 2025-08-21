---
description: "Learn more about: INFO.EXCLUDEDARTIFACTS"
title: "INFO.EXCLUDEDARTIFACTS function (DAX)"
author: jeroenterheerdt
---
# INFO.EXCLUDEDARTIFACTS

[!INCLUDE[applies-to-measures-columns-tables-visual-calculations-discouraged](includes/applies-to-measures-columns-tables-visual-calculations-discouraged.md)]

Returns a table with information about each excluded artifact in the semantic model. This function provides metadata about artifacts that are excluded from the model.

## Syntax

```dax
INFO.EXCLUDEDARTIFACTS()
```

## Return value

A table whose columns match the schema rowset for excluded artifacts in the current semantic model.

## Remarks

- Typically used in DAX queries to inspect and document model metadata.
- Permissions required depend on the host. Querying full metadata may require model admin permissions.

## Example 1 - DAX query

```dax
EVALUATE
    INFO.EXCLUDEDARTIFACTS()
```

## Example 2 - DAX query with SELECTCOLUMNS

```dax
EVALUATE
    SELECTCOLUMNS(
        INFO.EXCLUDEDARTIFACTS(),
        "ObjectID", [ObjectID],
        "ObjectType", [ObjectType],
        "Reason", [Reason]
    )
```

## Example 3 - Calculated table

```dax
Excluded Artifacts =
SELECTCOLUMNS(
    INFO.EXCLUDEDARTIFACTS(),
    "ObjectID", [ObjectID],
    "ObjectType", [ObjectType]
)
```

## Example 4 - Measure

```dax
Number of Excluded Artifacts =
COUNTROWS(INFO.EXCLUDEDARTIFACTS())
```