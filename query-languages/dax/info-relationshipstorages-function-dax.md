---
description: "Learn more about: INFO.RELATIONSHIPSTORAGES"
title: "INFO.RELATIONSHIPSTORAGES function (DAX)"
author: jeroenterheerdt
---
# INFO.RELATIONSHIPSTORAGES

[!INCLUDE[applies-to-measures-columns-tables-visual-calculations-discouraged](includes/applies-to-measures-columns-tables-visual-calculations-discouraged.md)]

Returns a table with information about each relationship storage in the semantic model. This function provides metadata about how relationships are stored.

## Syntax

```dax
INFO.RELATIONSHIPSTORAGES()
```

## Return value

A table whose columns match the schema rowset for relationship storages in the current semantic model.

## Remarks

- Typically used in DAX queries to inspect and document model metadata.
- Permissions required depend on the host. Querying full metadata may require model admin permissions.

## Example 1 - DAX query

```dax
EVALUATE
    INFO.RELATIONSHIPSTORAGES()
```

## Example 2 - DAX query with SELECTCOLUMNS

```dax
EVALUATE
    SELECTCOLUMNS(
        INFO.RELATIONSHIPSTORAGES(),
        "RelationshipID", [RelationshipID],
        "State", [State],
        "LastUpdateTime", [LastUpdateTime]
    )
```

## Example 3 - Calculated table

```dax
Relationship Storages =
SELECTCOLUMNS(
    INFO.RELATIONSHIPSTORAGES(),
    "RelationshipID", [RelationshipID],
    "State", [State]
)
```

## Example 4 - Measure

```dax
Number of Relationship Storages =
COUNTROWS(INFO.RELATIONSHIPSTORAGES())
```