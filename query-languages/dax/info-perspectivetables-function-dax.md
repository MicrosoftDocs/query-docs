---
description: "Learn more about: INFO.PERSPECTIVETABLES"
title: "INFO.PERSPECTIVETABLES function (DAX)"
author: jeroenterheerdt
---
# INFO.PERSPECTIVETABLES

[!INCLUDE[applies-to-measures-columns-tables-visual-calculations-discouraged](includes/applies-to-measures-columns-tables-visual-calculations-discouraged.md)]

Returns a table with information about each perspective table in the semantic model. This function provides metadata about tables included in perspectives.

## Syntax

```dax
INFO.PERSPECTIVETABLES()
```

## Return value

A table whose columns match the schema rowset for perspective tables in the current semantic model.

## Remarks

- Typically used in DAX queries to inspect and document model metadata.
- Permissions required depend on the host. Querying full metadata may require model admin permissions.

## Example 1 - DAX query

```dax
EVALUATE
    INFO.PERSPECTIVETABLES()
```

## Example 2 - DAX query with SELECTCOLUMNS

```dax
EVALUATE
    SELECTCOLUMNS(
        INFO.PERSPECTIVETABLES(),
        "PerspectiveID", [PerspectiveID],
        "TableID", [TableID],
        "IncludeInPerspective", [IncludeInPerspective]
    )
```

## Example 3 - Calculated table

```dax
Perspective Tables =
SELECTCOLUMNS(
    INFO.PERSPECTIVETABLES(),
    "PerspectiveID", [PerspectiveID],
    "TableID", [TableID]
)
```

## Example 4 - Measure

```dax
Number of Perspective Tables =
COUNTROWS(INFO.PERSPECTIVETABLES())
```