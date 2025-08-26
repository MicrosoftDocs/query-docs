---
description: "Learn more about: INFO.PERSPECTIVEHIERARCHIES"
title: "INFO.PERSPECTIVEHIERARCHIES function (DAX)"
author: jeroenterheerdt
---
# INFO.PERSPECTIVEHIERARCHIES

[!INCLUDE[applies-to-query-only](includes/applies-to-query-only.md)]

Returns a table with information about each perspective hierarchy in the semantic model. This function provides metadata about hierarchies included in perspectives.

## Syntax

```dax
INFO.PERSPECTIVEHIERARCHIES ( [<Restriction name>, <Restriction value>], ... )
```

[!INCLUDE[parameters-for-info-dax-functions](includes/parameters-for-info-dax-functions.md)]

## Return value

A table whose columns match the schema rowset for perspective hierarchies in the current semantic model.

## Remarks

- Typically used in DAX queries to inspect and document model metadata.
- Permissions required depend on the host. Querying full metadata may require model admin permissions.

## Example

The following DAX query can be run in [DAX query view](/power-bi/transform-model/dax-query-view):

```dax
EVALUATE
	INFO.PERSPECTIVEHIERARCHIES()
```
## See also

[INFO.PERSPECTIVES](info-perspectives-function-dax.md)
[INFO.PERSPECTIVECOLUMNS](info-perspectivecolumns-function-dax.md)
[INFO.PERSPECTIVEMEASURES](info-perspectivemeasures-function-dax.md)
[INFO.PERSPECTIVETABLES](info-perspectivetables-function-dax.md)
[INFO.TABLES](info-tables-function-dax.md)
