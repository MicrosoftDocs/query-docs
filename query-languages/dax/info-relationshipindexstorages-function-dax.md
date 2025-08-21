---
description: "Learn more about: INFO.RELATIONSHIPINDEXSTORAGES"
title: "INFO.RELATIONSHIPINDEXSTORAGES function (DAX)"
author: jeroenterheerdt
---
# INFO.RELATIONSHIPINDEXSTORAGES

[!INCLUDE[applies-to-query-only](includes/applies-to-query-only.md)]

Returns a table with information about each relationship index storage in the semantic model. This function provides metadata about relationship index storage characteristics.

## Syntax

```dax
INFO.RELATIONSHIPINDEXSTORAGES ( [<Restriction name>, <Restriction value>], ... )
```

[!INCLUDE[parameters-for-info-dax-functions](includes/parameters-for-info-dax-functions.md)]

## Return value

A table whose columns match the schema rowset for relationship index storages in the current semantic model.

## Remarks

- Typically used in DAX queries to inspect and document model metadata.
- Permissions required depend on the host. Querying full metadata may require model admin permissions.

## Example

The following DAX query can be run in [DAX query view](/power-bi/transform-model/dax-query-view):

```dax
EVALUATE
	INFO.RELATIONSHIPINDEXSTORAGES()
```

## Example 2 - DAX query with SELECTCOLUMNS

```dax
EVALUATE
    SELECTCOLUMNS(
        INFO.RELATIONSHIPINDEXSTORAGES(),
        "RelationshipID", [RelationshipID],
        "State", [State],
        "LastUpdateTime", [LastUpdateTime]
    )
```

## Example 3 - Calculated table

```dax
Relationship Index Storages =
SELECTCOLUMNS(
    INFO.RELATIONSHIPINDEXSTORAGES(),
    "RelationshipID", [RelationshipID],
    "State", [State]
)
```

## Example 4 - Measure

```dax
Number of Relationship Index Storages =
COUNTROWS(INFO.RELATIONSHIPINDEXSTORAGES())
```