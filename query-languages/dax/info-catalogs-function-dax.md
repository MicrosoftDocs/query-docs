---
description: "Learn more about: INFO.CATALOGS"
title: "INFO.CATALOGS function (DAX)"
author: jeroenterheerdt
---
# INFO.CATALOGS

[!INCLUDE[applies-to-measures-columns-tables-visual-calculations-discouraged](includes/applies-to-measures-columns-tables-visual-calculations-discouraged.md)]

Returns a table with information about each catalog in the semantic model. This function provides metadata about the catalogs available in the current context.

## Syntax

```dax
INFO.CATALOGS()
```

## Return value

A table whose columns match the schema rowset for catalogs in the current semantic model.

## Remarks

- Typically used in DAX queries to inspect and document model metadata.
- Permissions required depend on the host. Querying full metadata may require model admin permissions.

## Example 1 - DAX query

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