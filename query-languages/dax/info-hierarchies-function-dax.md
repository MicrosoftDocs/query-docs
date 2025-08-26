---
description: "Learn more about: INFO.HIERARCHIES"
title: "INFO.HIERARCHIES function (DAX)"
author: jeroenterheerdt
---
# INFO.HIERARCHIES

[!INCLUDE[applies-to-query-only](includes/applies-to-query-only.md)]

Returns a table with information about each hierarchy in the semantic model. This function provides metadata about hierarchies and their properties.

## Syntax

```dax
INFO.HIERARCHIES ( [<Restriction name>, <Restriction value>], ... )
```

[!INCLUDE[parameters-for-info-dax-functions](includes/parameters-for-info-dax-functions.md)]

## Return value

A table whose columns match the schema rowset for hierarchies in the current semantic model.

## Remarks

- Typically used in DAX queries to inspect and document model metadata.
- Permissions required depend on the host. Querying full metadata may require model admin permissions.

## Example

The following DAX query can be run in [DAX query view](/power-bi/transform-model/dax-query-view):

```dax
EVALUATE
	INFO.HIERARCHIES()
```

## See also

[INFO.ATTRIBUTEHIERARCHIES](info-attributehierarchies-function-dax.md)
[INFO.HIERARCHYSTORAGES](info-hierarchystorages-function-dax.md)
[INFO.ATTRIBUTEHIERARCHYSTORAGES](info-attributehierarchystorages-function-dax.md)
[INFO.LEVELS](info-levels-function-dax.md)
[INFO.TABLES](info-tables-function-dax.md)
