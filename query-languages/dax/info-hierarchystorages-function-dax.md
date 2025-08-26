---
description: "Learn more about: INFO.HIERARCHYSTORAGES"
title: "INFO.HIERARCHYSTORAGES function (DAX)"
author: jeroenterheerdt
---
# INFO.HIERARCHYSTORAGES

[!INCLUDE[applies-to-query-only](includes/applies-to-query-only.md)]

Returns a table with information about each hierarchy storage in the semantic model. This function provides metadata about how hierarchies are stored.

## Syntax

```dax
INFO.HIERARCHYSTORAGES ( [<Restriction name>, <Restriction value>], ... )
```

[!INCLUDE[parameters-for-info-dax-functions](includes/parameters-for-info-dax-functions.md)]

## Return value

A table whose columns match the schema rowset for hierarchy storages in the current semantic model.

## Remarks

- Typically used in DAX queries to inspect and document model metadata.
- Permissions required depend on the host. Querying full metadata may require model admin permissions.

## Example

The following DAX query can be run in [DAX query view](/power-bi/transform-model/dax-query-view):

```dax
EVALUATE
	INFO.HIERARCHYSTORAGES()
```