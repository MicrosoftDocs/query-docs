---
description: "Learn more about: INFO.REFRESHPOLICIES"
title: "INFO.REFRESHPOLICIES function (DAX)"
author: jeroenterheerdt
---
# INFO.REFRESHPOLICIES

[!INCLUDE[applies-to-measures-columns-tables-visual-calculations-discouraged](includes/applies-to-measures-columns-tables-visual-calculations-discouraged.md)]

Returns a table with information about each refresh policy in the semantic model. This function provides metadata about refresh policies defined for tables.

## Syntax

```dax
INFO.REFRESHPOLICIES()
```

## Return value

A table whose columns match the schema rowset for refresh policies in the current semantic model.

## Remarks

- Typically used in DAX queries to inspect and document model metadata.
- Permissions required depend on the host. Querying full metadata may require model admin permissions.

## Example 1 - DAX query

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