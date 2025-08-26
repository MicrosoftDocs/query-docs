---
description: "Learn more about: INFO.DATACOVERAGEDEFINITIONS"
title: "INFO.DATACOVERAGEDEFINITIONS function (DAX)"
author: jeroenterheerdt
---
# INFO.DATACOVERAGEDEFINITIONS

[!INCLUDE[applies-to-query-only](includes/applies-to-query-only.md)]

Returns a table with information about each data coverage definition in the semantic model. This function provides metadata about data coverage settings and definitions.

## Syntax

```dax
INFO.DATACOVERAGEDEFINITIONS ( [<Restriction name>, <Restriction value>], ... )
```

[!INCLUDE[parameters-for-info-dax-functions](includes/parameters-for-info-dax-functions.md)]

## Return value

A table whose columns match the schema rowset for data coverage definitions in the current semantic model.

## Remarks

- Typically used in DAX queries to inspect and document model metadata.
- Permissions required depend on the host. Querying full metadata may require model admin permissions.

## Example

The following DAX query can be run in [DAX query view](/power-bi/transform-model/dax-query-view):

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

## See also

[INFO.TABLES](info-tables-function-dax.md)
[INFO.COLUMNS](info-columns-function-dax.md)
[INFO.MEASURES](info-measures-function-dax.md)
[INFO functions overview](info-functions-dax.md)
