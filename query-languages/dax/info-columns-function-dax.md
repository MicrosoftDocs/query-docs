---
description: "Learn more about: INFO.COLUMNS"
title: "INFO.COLUMNS function (DAX)"
author: jeroenterheerdt
---
# INFO.COLUMNS

[!INCLUDE[applies-to-query-only](includes/applies-to-query-only.md)]

Returns a table with information about each column in the semantic model. This function provides metadata about all columns including their properties and characteristics.

## Syntax

```dax
INFO.COLUMNS ( [<Restriction name>, <Restriction value>], ... )
```

[!INCLUDE[parameters-for-info-dax-functions](includes/parameters-for-info-dax-functions.md)]

## Return value

A table whose columns match the schema rowset for columns in the current semantic model.

## Remarks

- Typically used in DAX queries to inspect and document model metadata.
- Permissions required depend on the host. Querying full metadata may require model admin permissions.

## Example

The following DAX query can be run in [DAX query view](/power-bi/transform-model/dax-query-view):

```dax
EVALUATE
	INFO.COLUMNS()
```

## Example 2 - DAX query with SELECTCOLUMNS

```dax
EVALUATE
    SELECTCOLUMNS(
        INFO.COLUMNS(),
        "ExplicitName", [ExplicitName],
        "DataType", [DataType],
        "IsHidden", [IsHidden]
    )
```

## Example 3 - Calculated table

```dax
Columns =
SELECTCOLUMNS(
    INFO.COLUMNS(),
    "Name", [ExplicitName],
    "DataType", [DataType]
)
```

## Example 4 - Measure

```dax
Number of Columns =
COUNTROWS(INFO.COLUMNS())
```