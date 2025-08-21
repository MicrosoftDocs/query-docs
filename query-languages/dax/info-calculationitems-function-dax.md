---
description: "Learn more about: INFO.CALCULATIONITEMS"
title: "INFO.CALCULATIONITEMS function (DAX)"
author: jeroenterheerdt
---
# INFO.CALCULATIONITEMS

[!INCLUDE[applies-to-query-only](includes/applies-to-query-only.md)]

Returns a table with information about each calculation item in the semantic model. This function provides metadata about calculation items within calculation groups.

## Syntax

```dax
INFO.CALCULATIONITEMS ( [<Restriction name>, <Restriction value>], ... )
```

[!INCLUDE[parameters-for-info-dax-functions](includes/parameters-for-info-dax-functions.md)]

## Return value

A table whose columns match the schema rowset for calculation items in the current semantic model.

## Remarks

- Typically used in DAX queries to inspect and document model metadata.
- Permissions required depend on the host. Querying full metadata may require model admin permissions.

## Example

The following DAX query can be run in [DAX query view](/power-bi/transform-model/dax-query-view):

```dax
EVALUATE
	INFO.CALCULATIONITEMS()
```

## Example 2 - DAX query with SELECTCOLUMNS

```dax
EVALUATE
    SELECTCOLUMNS(
        INFO.CALCULATIONITEMS(),
        "Name", [Name],
        "Expression", [Expression],
        "Ordinal", [Ordinal]
    )
```

## Example 3 - Calculated table

```dax
Calculation Items =
SELECTCOLUMNS(
    INFO.CALCULATIONITEMS(),
    "Name", [Name],
    "Expression", [Expression]
)
```

## Example 4 - Measure

```dax
Number of Calculation Items =
COUNTROWS(INFO.CALCULATIONITEMS())
```