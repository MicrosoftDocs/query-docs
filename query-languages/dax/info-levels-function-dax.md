---
description: "Learn more about: INFO.LEVELS"
title: "INFO.LEVELS function (DAX)"
author: jeroenterheerdt
---
# INFO.LEVELS

[!INCLUDE[applies-to-query-only](includes/applies-to-query-only.md)]

Returns a table with information about each level in the semantic model. This function provides metadata about hierarchy levels and their properties.

## Syntax

```dax
INFO.LEVELS ( [<Restriction name>, <Restriction value>], ... )
```

[!INCLUDE[parameters-for-info-dax-functions](includes/parameters-for-info-dax-functions.md)]

## Return value

A table whose columns match the schema rowset for levels in the current semantic model.

## Remarks

- Typically used in DAX queries to inspect and document model metadata.
- Permissions required depend on the host. Querying full metadata may require model admin permissions.

## Example

The following DAX query can be run in [DAX query view](/power-bi/transform-model/dax-query-view):

```dax
EVALUATE
	INFO.LEVELS()
```