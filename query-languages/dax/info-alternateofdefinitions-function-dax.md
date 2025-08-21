---
description: "Learn more about: INFO.ALTERNATEOFDEFINITIONS"
title: "INFO.ALTERNATEOFDEFINITIONS function (DAX)"
author: jeroenterheerdt
---
# INFO.ALTERNATEOFDEFINITIONS

[!INCLUDE[applies-to-measures-columns-tables-visual-calculations-discouraged](includes/applies-to-measures-columns-tables-visual-calculations-discouraged.md)]

Returns a table with information about each alternate of definition in the semantic model. This function provides metadata about alternate definitions for model objects.

## Syntax

```dax
INFO.ALTERNATEOFDEFINITIONS()
```

## Return value

A table whose columns match the schema rowset for alternate of definitions in the current semantic model.

## Remarks

- Typically used in DAX queries to inspect and document model metadata.
- Permissions required depend on the host. Querying full metadata may require model admin permissions.

## Example 1 - DAX query

```dax
EVALUATE
    INFO.ALTERNATEOFDEFINITIONS()
```

## Example 2 - DAX query with SELECTCOLUMNS

```dax
EVALUATE
    SELECTCOLUMNS(
        INFO.ALTERNATEOFDEFINITIONS(),
        "Name", [Name],
        "ObjectType", [ObjectType]
    )
```

## Example 3 - Calculated table

```dax
Alternate Definitions =
SELECTCOLUMNS(
    INFO.ALTERNATEOFDEFINITIONS(),
    "Name", [Name],
    "ObjectType", [ObjectType]
)
```

## Example 4 - Measure

```dax
Number of Alternate Definitions =
COUNTROWS(INFO.ALTERNATEOFDEFINITIONS())
```