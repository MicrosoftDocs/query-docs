---
description: "Learn more about: INFO.CALCULATIONGROUPS"
title: "INFO.CALCULATIONGROUPS function (DAX)"
author: jeroenterheerdt
---
# INFO.CALCULATIONGROUPS

[!INCLUDE[applies-to-query-only](includes/applies-to-query-only.md)]

Returns a table with information about each calculation group in the semantic model. This function provides metadata about calculation groups and their properties.

## Syntax

```dax
INFO.CALCULATIONGROUPS ( [<Restriction name>, <Restriction value>], ... )
```

[!INCLUDE[parameters-for-info-dax-functions](includes/parameters-for-info-dax-functions.md)]

## Return value

A table whose columns match the schema rowset for calculation groups in the current semantic model.

## Remarks

- Typically used in DAX queries to inspect and document model metadata.
- Permissions required depend on the host. Querying full metadata may require model admin permissions.

## Example

The following DAX query can be run in [DAX query view](/power-bi/transform-model/dax-query-view):

```dax
EVALUATE
	INFO.CALCULATIONGROUPS()
```

## Example 2 - DAX query with SELECTCOLUMNS

```dax
EVALUATE
    SELECTCOLUMNS(
        INFO.CALCULATIONGROUPS(),
        "Name", [Name],
        "Description", [Description],
        "Precedence", [Precedence]
    )
```

## Example 3 - Calculated table

```dax
Calculation Groups =
SELECTCOLUMNS(
    INFO.CALCULATIONGROUPS(),
    "Name", [Name],
    "Description", [Description]
)
```

## Example 4 - Measure

```dax
Number of Calculation Groups =
COUNTROWS(INFO.CALCULATIONGROUPS())
```