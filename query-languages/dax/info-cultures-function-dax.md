---
description: "Learn more about: INFO.CULTURES"
title: "INFO.CULTURES function (DAX)"
author: jeroenterheerdt
---
# INFO.CULTURES

[!INCLUDE[applies-to-measures-columns-tables-visual-calculations-discouraged](includes/applies-to-measures-columns-tables-visual-calculations-discouraged.md)]

Returns a table with information about each culture in the semantic model. This function provides metadata about the cultures and locales supported by the model.

## Syntax

```dax
INFO.CULTURES()
```

## Return value

A table whose columns match the schema rowset for cultures in the current semantic model.

## Remarks

- Typically used in DAX queries to inspect and document model metadata.
- Permissions required depend on the host. Querying full metadata may require model admin permissions.

## Example 1 - DAX query

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