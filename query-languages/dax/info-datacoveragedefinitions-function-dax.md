---
description: "Learn more about: INFO.DATACOVERAGEDEFINITIONS"
title: "INFO.DATACOVERAGEDEFINITIONS function (DAX)"
author: jeroenterheerdt
---
# INFO.DATACOVERAGEDEFINITIONS

[!INCLUDE[applies-to-measures-columns-tables-visual-calculations-discouraged](includes/applies-to-measures-columns-tables-visual-calculations-discouraged.md)]

Returns a table with information about each data coverage definition in the semantic model. This function provides metadata about data coverage settings and definitions.

## Syntax

```dax
INFO.DATACOVERAGEDEFINITIONS()
```

## Return value

A table whose columns match the schema rowset for data coverage definitions in the current semantic model.

## Remarks

- Typically used in DAX queries to inspect and document model metadata.
- Permissions required depend on the host. Querying full metadata may require model admin permissions.

## Example 1 - DAX query

```dax
EVALUATE
    INFO.DATACOVERAGEDEFINITIONS()
```

## Example 2 - DAX query with SELECTCOLUMNS

```dax
EVALUATE
    SELECTCOLUMNS(
        INFO.DATACOVERAGEDEFINITIONS(),
        "Name", [Name],
        "Expression", [Expression],
        "ObjectType", [ObjectType]
    )
```

## Example 3 - Calculated table

```dax
Data Coverage Definitions =
SELECTCOLUMNS(
    INFO.DATACOVERAGEDEFINITIONS(),
    "Name", [Name],
    "Expression", [Expression]
)
```

## Example 4 - Measure

```dax
Number of Data Coverage Definitions =
COUNTROWS(INFO.DATACOVERAGEDEFINITIONS())
```