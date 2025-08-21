---
description: "Learn more about: INFO.DEPENDENCIES"
title: "INFO.DEPENDENCIES function (DAX)"
author: jeroenterheerdt
---
# INFO.DEPENDENCIES

[!INCLUDE[applies-to-measures-columns-tables-visual-calculations-discouraged](includes/applies-to-measures-columns-tables-visual-calculations-discouraged.md)]

Returns a table with information about each dependency in the semantic model. This function provides metadata about object dependencies and relationships between model objects.

## Syntax

```dax
INFO.DEPENDENCIES()
```

## Return value

A table whose columns match the schema rowset for dependencies in the current semantic model.

## Remarks

- Typically used in DAX queries to inspect and document model metadata.
- Permissions required depend on the host. Querying full metadata may require model admin permissions.

## Example 1 - DAX query

```dax
EVALUATE
    INFO.DEPENDENCIES()
```

## Example 2 - DAX query with SELECTCOLUMNS

```dax
EVALUATE
    SELECTCOLUMNS(
        INFO.DEPENDENCIES(),
        "ObjectID", [ObjectID],
        "ReferencedObjectID", [ReferencedObjectID],
        "DependencyType", [DependencyType]
    )
```

## Example 3 - Calculated table

```dax
Dependencies =
SELECTCOLUMNS(
    INFO.DEPENDENCIES(),
    "ObjectID", [ObjectID],
    "ReferencedObjectID", [ReferencedObjectID]
)
```

## Example 4 - Measure

```dax
Number of Dependencies =
COUNTROWS(INFO.DEPENDENCIES())
```