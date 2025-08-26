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

## See also

[INFO.PERSPECTIVECOLUMNS](info-perspectivecolumns-function-dax.md)
[INFO.PERSPECTIVEHIERARCHIES](info-perspectivehierarchies-function-dax.md)
[INFO.PERSPECTIVEMEASURES](info-perspectivemeasures-function-dax.md)
[INFO.PERSPECTIVETABLES](info-perspectivetables-function-dax.md)
[INFO.TABLES](info-tables-function-dax.md)
