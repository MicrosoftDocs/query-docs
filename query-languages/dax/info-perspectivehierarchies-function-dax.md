---
description: "Learn more about: INFO.PERSPECTIVEHIERARCHIES"
title: "INFO.PERSPECTIVEHIERARCHIES function (DAX)"
author: jeroenterheerdt
---
# INFO.PERSPECTIVEHIERARCHIES

[!INCLUDE[applies-to-measures-columns-tables-visual-calculations-discouraged](includes/applies-to-measures-columns-tables-visual-calculations-discouraged.md)]

Returns a table with information about each perspective hierarchy in the semantic model. This function provides metadata about hierarchies included in perspectives.

## Syntax

```dax
INFO.PERSPECTIVEHIERARCHIES()
```

## Return value

A table whose columns match the schema rowset for perspective hierarchies in the current semantic model.

## Remarks

- Typically used in DAX queries to inspect and document model metadata.
- Permissions required depend on the host. Querying full metadata may require model admin permissions.

## Example 1 - DAX query

```dax
EVALUATE
    INFO.PERSPECTIVEHIERARCHIES()
```

## Example 2 - DAX query with SELECTCOLUMNS

```dax
EVALUATE
    SELECTCOLUMNS(
        INFO.PERSPECTIVEHIERARCHIES(),
        "PerspectiveID", [PerspectiveID],
        "HierarchyID", [HierarchyID],
        "IncludeInPerspective", [IncludeInPerspective]
    )
```

## Example 3 - Calculated table

```dax
Perspective Hierarchies =
SELECTCOLUMNS(
    INFO.PERSPECTIVEHIERARCHIES(),
    "PerspectiveID", [PerspectiveID],
    "HierarchyID", [HierarchyID]
)
```

## Example 4 - Measure

```dax
Number of Perspective Hierarchies =
COUNTROWS(INFO.PERSPECTIVEHIERARCHIES())
```