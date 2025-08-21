---
description: "Learn more about: INFO.OBJECTTRANSLATIONS"
title: "INFO.OBJECTTRANSLATIONS function (DAX)"
author: jeroenterheerdt
---
# INFO.OBJECTTRANSLATIONS

[!INCLUDE[applies-to-query-only](includes/applies-to-query-only.md)]

Returns a table with information about each object translation in the semantic model. This function provides metadata about translations for model objects.

## Syntax

```dax
INFO.OBJECTTRANSLATIONS ( [<Restriction name>, <Restriction value>], ... )
```

[!INCLUDE[parameters-for-info-dax-functions](includes/parameters-for-info-dax-functions.md)]

## Return value

A table whose columns match the schema rowset for object translations in the current semantic model.

## Remarks

- Typically used in DAX queries to inspect and document model metadata.
- Permissions required depend on the host. Querying full metadata may require model admin permissions.

## Example

The following DAX query can be run in [DAX query view](/power-bi/transform-model/dax-query-view):

```dax
EVALUATE
	INFO.OBJECTTRANSLATIONS()
```

## Example 2 - DAX query with SELECTCOLUMNS

```dax
EVALUATE
    SELECTCOLUMNS(
        INFO.OBJECTTRANSLATIONS(),
        "ObjectID", [ObjectID],
        "CultureID", [CultureID],
        "Property", [Property]
    )
```

## Example 3 - Calculated table

```dax
Object Translations =
SELECTCOLUMNS(
    INFO.OBJECTTRANSLATIONS(),
    "ObjectID", [ObjectID],
    "CultureID", [CultureID]
)
```

## Example 4 - Measure

```dax
Number of Object Translations =
COUNTROWS(INFO.OBJECTTRANSLATIONS())
```