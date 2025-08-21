---
description: "Learn more about: INFO.PERSPECTIVEMEASURES"
title: "INFO.PERSPECTIVEMEASURES function (DAX)"
author: jeroenterheerdt
---
# INFO.PERSPECTIVEMEASURES

[!INCLUDE[applies-to-measures-columns-tables-visual-calculations-discouraged](includes/applies-to-measures-columns-tables-visual-calculations-discouraged.md)]

Returns a table with information about each perspective measure in the semantic model. This function provides metadata about measures included in perspectives.

## Syntax

```dax
INFO.PERSPECTIVEMEASURES()
```

## Return value

A table whose columns match the schema rowset for perspective measures in the current semantic model.

## Remarks

- Typically used in DAX queries to inspect and document model metadata.
- Permissions required depend on the host. Querying full metadata may require model admin permissions.

## Example 1 - DAX query

```dax
EVALUATE
    INFO.PERSPECTIVEMEASURES()
```

## Example 2 - DAX query with SELECTCOLUMNS

```dax
EVALUATE
    SELECTCOLUMNS(
        INFO.PERSPECTIVEMEASURES(),
        "PerspectiveID", [PerspectiveID],
        "MeasureID", [MeasureID],
        "IncludeInPerspective", [IncludeInPerspective]
    )
```

## Example 3 - Calculated table

```dax
Perspective Measures =
SELECTCOLUMNS(
    INFO.PERSPECTIVEMEASURES(),
    "PerspectiveID", [PerspectiveID],
    "MeasureID", [MeasureID]
)
```

## Example 4 - Measure

```dax
Number of Perspective Measures =
COUNTROWS(INFO.PERSPECTIVEMEASURES())
```