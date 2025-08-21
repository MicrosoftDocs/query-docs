---
description: "Learn more about: INFO.PERSPECTIVES"
title: "INFO.PERSPECTIVES function (DAX)"
author: jeroenterheerdt
---
# INFO.PERSPECTIVES

[!INCLUDE[applies-to-query-only](includes/applies-to-query-only.md)]

Returns a table with information about each perspective in the semantic model. This function provides metadata about perspectives defined in the model.

## Syntax

```dax
INFO.PERSPECTIVES ( [<Restriction name>, <Restriction value>], ... )
```

[!INCLUDE[parameters-for-info-dax-functions](includes/parameters-for-info-dax-functions.md)]

## Return value

A table whose columns match the schema rowset for perspectives in the current semantic model.

## Remarks

- Typically used in DAX queries to inspect and document model metadata.
- Permissions required depend on the host. Querying full metadata may require model admin permissions.

## Example

The following DAX query can be run in [DAX query view](/power-bi/transform-model/dax-query-view):

```dax
EVALUATE
	INFO.PERSPECTIVES()
```

## Example 2 - DAX query with SELECTCOLUMNS

```dax
EVALUATE
    SELECTCOLUMNS(
        INFO.PERSPECTIVES(),
        "Name", [Name],
        "Description", [Description],
        "DefaultMeasure", [DefaultMeasure]
    )
```

## Example 3 - Calculated table

```dax
Perspectives =
SELECTCOLUMNS(
    INFO.PERSPECTIVES(),
    "Name", [Name],
    "Description", [Description]
)
```

## Example 4 - Measure

```dax
Number of Perspectives =
COUNTROWS(INFO.PERSPECTIVES())
```