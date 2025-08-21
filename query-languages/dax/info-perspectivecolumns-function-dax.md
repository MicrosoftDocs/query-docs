---
description: "Learn more about: INFO.PERSPECTIVECOLUMNS"
title: "INFO.PERSPECTIVECOLUMNS function (DAX)"
author: jeroenterheerdt
---
# INFO.PERSPECTIVECOLUMNS

[!INCLUDE[applies-to-measures-columns-tables-visual-calculations-discouraged](includes/applies-to-measures-columns-tables-visual-calculations-discouraged.md)]

Returns a table with information about each perspective column in the semantic model. This function provides metadata about columns included in perspectives.

## Syntax

```dax
INFO.PERSPECTIVECOLUMNS()
```

## Return value

A table whose columns match the schema rowset for perspective columns in the current semantic model.

## Remarks

- Typically used in DAX queries to inspect and document model metadata.
- Permissions required depend on the host. Querying full metadata may require model admin permissions.

## Example 1 - DAX query

```dax
EVALUATE
    INFO.PERSPECTIVECOLUMNS()
```

## Example 2 - DAX query with SELECTCOLUMNS

```dax
EVALUATE
    SELECTCOLUMNS(
        INFO.PERSPECTIVECOLUMNS(),
        "PerspectiveID", [PerspectiveID],
        "ColumnID", [ColumnID],
        "IncludeInPerspective", [IncludeInPerspective]
    )
```

## Example 3 - Calculated table

```dax
Perspective Columns =
SELECTCOLUMNS(
    INFO.PERSPECTIVECOLUMNS(),
    "PerspectiveID", [PerspectiveID],
    "ColumnID", [ColumnID]
)
```

## Example 4 - Measure

```dax
Number of Perspective Columns =
COUNTROWS(INFO.PERSPECTIVECOLUMNS())
```