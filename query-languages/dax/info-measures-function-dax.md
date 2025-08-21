---
description: "Learn more about: INFO.MEASURES"
title: "INFO.MEASURES function (DAX)"
author: jeroenterheerdt
---
# INFO.MEASURES

[!INCLUDE[applies-to-query-only](includes/applies-to-query-only.md)]

Returns a table with information about each measure in the semantic model, with columns that match the schema rowset for measure objects (for example, name, expression, and state).

## Syntax

```dax
INFO.MEASURES ( [<Restriction name>, <Restriction value>], ... )
```

[!INCLUDE[parameters-for-info-dax-functions](includes/parameters-for-info-dax-functions.md)]

## Return value

A table whose columns match the schema rowset for measure objects in the current semantic model.

## Remarks

- Typically used in DAX queries to inspect and document model metadata.
- Permissions required depend on the host. Querying full metadata may require model admin permissions.

## Example

The following DAX query can be run in [DAX query view](/power-bi/transform-model/dax-query-view):

```dax
EVALUATE
	INFO.MEASURES()
```

## Example 2 - DAX query with SELECTCOLUMNS

```dax
EVALUATE
    SELECTCOLUMNS(
        INFO.MEASURES(),
        "Name", [Name],
        "Expression", [Expression],
        "State", [State]
    )
```

## Example 3 - Calculated table

```dax
Measures in this semantic model =
SELECTCOLUMNS(
    INFO.MEASURES(),
    "Name", [Name],
    "Expression", [Expression]
)
```

## Example 4 - Measure

```dax
Number of measures =
COUNTROWS(INFO.MEASURES())
```