---
description: "Learn more about: INFO.DATASOURCES"
title: "INFO.DATASOURCES function (DAX)"
author: jeroenterheerdt
---
# INFO.DATASOURCES

[!INCLUDE[applies-to-query-only](includes/applies-to-query-only.md)]

Returns a table with information about each data source in the semantic model. This function provides metadata about the data sources connected to the model.

## Syntax

```dax
INFO.DATASOURCES ( [<Restriction name>, <Restriction value>], ... )
```

[!INCLUDE[parameters-for-info-dax-functions](includes/parameters-for-info-dax-functions.md)]

## Return value

A table whose columns match the schema rowset for data sources in the current semantic model.

## Remarks

- Typically used in DAX queries to inspect and document model metadata.
- Permissions required depend on the host. Querying full metadata may require model admin permissions.

## Example

The following DAX query can be run in [DAX query view](/power-bi/transform-model/dax-query-view):

```dax
EVALUATE
	INFO.DATASOURCES()
```

## Example 2 - DAX query with SELECTCOLUMNS

```dax
EVALUATE
    SELECTCOLUMNS(
        INFO.DATASOURCES(),
        "Name", [Name],
        "Description", [Description],
        "Type", [Type]
    )
```

## Example 3 - Calculated table

```dax
Data Sources =
SELECTCOLUMNS(
    INFO.DATASOURCES(),
    "Name", [Name],
    "Type", [Type]
)
```

## Example 4 - Measure

```dax
Number of Data Sources =
COUNTROWS(INFO.DATASOURCES())
```