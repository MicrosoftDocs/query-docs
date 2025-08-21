---
description: "Learn more about: INFO.CATALOGS"
title: "INFO.CATALOGS function (DAX)"
author: jeroenterheerdt
---
# INFO.CATALOGS

[!INCLUDE[applies-to-query-only](includes/applies-to-query-only.md)]

Returns a table with information about each catalog in the semantic model. This function provides metadata about the catalogs available in the current context.

## Syntax

```dax
INFO.CATALOGS ( [<Restriction name>, <Restriction value>], ... )
```

[!INCLUDE[parameters-for-info-dax-functions](includes/parameters-for-info-dax-functions.md)]

## Return value

A table whose columns match the schema rowset for catalogs in the current semantic model.

## Remarks

- Typically used in DAX queries to inspect and document model metadata.
- Permissions required depend on the host. Querying full metadata may require model admin permissions.

## Example

The following DAX query can be run in [DAX query view](/power-bi/transform-model/dax-query-view):

```dax
EVALUATE
	INFO.CATALOGS()
```

## Example 2 - DAX query with SELECTCOLUMNS

```dax
EVALUATE
    SELECTCOLUMNS(
        INFO.CATALOGS(),
        "CatalogName", [CATALOG_NAME],
        "Description", [DESCRIPTION]
    )
```

## Example 3 - Calculated table

```dax
Catalogs =
SELECTCOLUMNS(
    INFO.CATALOGS(),
    "CatalogName", [CATALOG_NAME],
    "Description", [DESCRIPTION]
)
```

## Example 4 - Measure

```dax
Number of Catalogs =
COUNTROWS(INFO.CATALOGS())
```