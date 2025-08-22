---
description: "Learn more about: INFO.CULTURES"
title: "INFO.CULTURES function (DAX)"
author: jeroenterheerdt
---
# INFO.CULTURES

[!INCLUDE[applies-to-query-only](includes/applies-to-query-only.md)]

Returns a table with information about each culture in the semantic model. This function provides metadata about the cultures and locales supported by the model.

## Syntax

```dax
INFO.CULTURES ( [<Restriction name>, <Restriction value>], ... )
```

[!INCLUDE[parameters-for-info-dax-functions](includes/parameters-for-info-dax-functions.md)]

## Return value

A table whose columns match the schema rowset for cultures in the current semantic model.

## Remarks

- Typically used in DAX queries to inspect and document model metadata.
- Permissions required depend on the host. Querying full metadata may require model admin permissions.

## Example

The following DAX query can be run in [DAX query view](/power-bi/transform-model/dax-query-view):

```dax
EVALUATE
	INFO.CULTURES()
```

## Example 2 - DAX query with SELECTCOLUMNS

```dax
EVALUATE
    SELECTCOLUMNS(
        INFO.CULTURES(),
        "Name", [Name],
        "Description", [Description],
        "LinguisticMetadataID", [LinguisticMetadataID]
    )
```

## Example 3 - Calculated table

```dax
Cultures =
SELECTCOLUMNS(
    INFO.CULTURES(),
    "Name", [Name],
    "Description", [Description]
)
```

## Example 4 - Measure

```dax
Number of Cultures =
COUNTROWS(INFO.CULTURES())
```