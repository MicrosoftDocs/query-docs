---
description: "Learn more about: INFO.OBJECTTRANSLATIONS"
title: "INFO.OBJECTTRANSLATIONS function (DAX)"
author: jeroenterheerdt
---
# INFO.OBJECTTRANSLATIONS

[!INCLUDE[applies-to-measures-columns-tables-visual-calculations-discouraged](includes/applies-to-measures-columns-tables-visual-calculations-discouraged.md)]

Returns a table with information about each object translation in the semantic model. This function provides metadata about translations for model objects.

## Syntax

```dax
INFO.OBJECTTRANSLATIONS()
```

## Return value

A table whose columns match the schema rowset for object translations in the current semantic model.

## Remarks

- Typically used in DAX queries to inspect and document model metadata.
- Permissions required depend on the host. Querying full metadata may require model admin permissions.

## Example 1 - DAX query

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