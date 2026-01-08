---
description: "Learn more about: INFO.EXCLUDEDARTIFACTS"
title: "INFO.EXCLUDEDARTIFACTS function (DAX)"
author: jeroenterheerdt
---
# INFO.EXCLUDEDARTIFACTS

[!INCLUDE[applies-to-query-only](includes/applies-to-query-only.md)]

Returns a table with information about each excluded artifact in the semantic model. This function provides metadata about artifacts that are excluded from the model.

## Syntax

```dax
INFO.EXCLUDEDARTIFACTS ( [<Restriction name>, <Restriction value>], ... )
```

[!INCLUDE[parameters-for-info-dax-functions](includes/parameters-for-info-dax-functions.md)]

## Return value

A table whose columns match the schema rowset for excluded artifacts in the current semantic model.

## Remarks

- Typically used in DAX queries to inspect and document model metadata.
- Permissions required depend on the host. Querying full metadata may require model admin permissions.

## Example

The following DAX query can be run in [DAX query view](/power-bi/transform-model/dax-query-view):

```dax
EVALUATE
	INFO.EXCLUDEDARTIFACTS()
```

## Example 2 - DAX query with SELECTCOLUMNS

```dax
EVALUATE
    SELECTCOLUMNS(
        INFO.EXCLUDEDARTIFACTS(),
        "ObjectID", [ObjectID],
        "ObjectType", [ObjectType],
        "Reason", [Reason]
    )
```

## See also

[INFO.TABLES](info-tables-function-dax.md)
[INFO.COLUMNS](info-columns-function-dax.md)
[INFO.MEASURES](info-measures-function-dax.md)
[INFO functions overview](info-functions-dax.md)
