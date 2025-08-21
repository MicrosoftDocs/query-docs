---
description: "Learn more about: INFO.LINGUISTICMETADATA"
title: "INFO.LINGUISTICMETADATA function (DAX)"
author: jeroenterheerdt
---
# INFO.LINGUISTICMETADATA

[!INCLUDE[applies-to-measures-columns-tables-visual-calculations-discouraged](includes/applies-to-measures-columns-tables-visual-calculations-discouraged.md)]

Returns a table with information about each linguistic metadata entry in the semantic model. This function provides metadata about linguistic metadata definitions.

## Syntax

```dax
INFO.LINGUISTICMETADATA()
```

## Return value

A table whose columns match the schema rowset for linguistic metadata in the current semantic model.

## Remarks

- Typically used in DAX queries to inspect and document model metadata.
- Permissions required depend on the host. Querying full metadata may require model admin permissions.

## Example 1 - DAX query

```dax
EVALUATE
    INFO.LINGUISTICMETADATA()
```

## Example 2 - DAX query with SELECTCOLUMNS

```dax
EVALUATE
    SELECTCOLUMNS(
        INFO.LINGUISTICMETADATA(),
        "Name", [Name],
        "Description", [Description],
        "Content", [Content]
    )
```

## Example 3 - Calculated table

```dax
Linguistic Metadata =
SELECTCOLUMNS(
    INFO.LINGUISTICMETADATA(),
    "Name", [Name],
    "Description", [Description]
)
```

## Example 4 - Measure

```dax
Number of Linguistic Metadata Entries =
COUNTROWS(INFO.LINGUISTICMETADATA())
```