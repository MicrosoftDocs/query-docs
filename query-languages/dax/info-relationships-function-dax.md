---
description: "Learn more about: INFO.RELATIONSHIPS"
title: "INFO.RELATIONSHIPS function (DAX)"
author: jeroenterheerdt
---
# INFO.RELATIONSHIPS

[!INCLUDE[applies-to-query-only](includes/applies-to-query-only.md)]

Returns a table with information about each relationship in the semantic model. This function provides metadata about relationships between tables.

## Syntax

```dax
INFO.RELATIONSHIPS ( [<Restriction name>, <Restriction value>], ... )
```

[!INCLUDE[parameters-for-info-dax-functions](includes/parameters-for-info-dax-functions.md)]

## Return value

A table whose columns match the schema rowset for relationships in the current semantic model.

|Column|Description|
|---|---|
|ID|Unique identifier for the relationship|
|ModelID|Foreign key to the model containing this relationship|
|Name|Name of the relationship|
|IsActive|Boolean indicating whether the relationship is active|
|Type|Type of relationship (e.g., OneToMany, ManyToOne)|
|CrossFilteringBehavior|Cross filtering behavior (e.g., OneDirection, BothDirections)|
|JoinOnDateBehavior|Behavior for date-based joins|
|RelyOnReferentialIntegrity|Boolean indicating whether to rely on referential integrity|
|FromTableID|Foreign key to the source table in the relationship|
|FromColumnID|Foreign key to the source column in the relationship|
|FromCardinality|Cardinality on the "from" side of the relationship|
|ToTableID|Foreign key to the target table in the relationship|
|ToColumnID|Foreign key to the target column in the relationship|
|ToCardinality|Cardinality on the "to" side of the relationship|
|State|Current state of the relationship|
|RelationshipStorageID|Foreign key to the relationship storage information|
|RelationshipStorage2ID|Foreign key to secondary relationship storage information|
|ModifiedTime|Date and time when the relationship was last modified|
|RefreshedTime|Date and time when the relationship was last refreshed|
|SecurityFilteringBehavior|Security filtering behavior for the relationship|

## Remarks

- Typically used in DAX queries to inspect and document model metadata.
- Permissions required depend on the host. Querying full metadata may require model admin permissions.

## Example

The following DAX query can be run in [DAX query view](/power-bi/transform-model/dax-query-view):

```dax
EVALUATE
	INFO.RELATIONSHIPS()
```

### Example 2 - DAX query with joins

The following DAX query can be run in [DAX query view](/power-bi/transform-model/dax-query-view):

```dax
EVALUATE
VAR _Relationships = 
    SELECTCOLUMNS(
        INFO.RELATIONSHIPS(),
        "Relationship Name", [Name],
        "Is Active", [IsActive],
        "Type", [Type],
        "Cross Filtering", [CrossFilteringBehavior],
        "From Table ID", [FromTableID],
        "From Column ID", [FromColumnID],
        "To Table ID", [ToTableID],
        "To Column ID", [ToColumnID]
    )

VAR _FromTables = 
    SELECTCOLUMNS(
        INFO.TABLES(),
        "FromTableID", [ID],
        "From Table Name", [Name]
    )

VAR _ToTables = 
    SELECTCOLUMNS(
        INFO.TABLES(),
        "ToTableID", [ID],
        "To Table Name", [Name]
    )

VAR _FromColumns = 
    SELECTCOLUMNS(
        INFO.COLUMNS(),
        "FromColumnID", [ID],
        "From Column Name", [Name]
    )

VAR _ToColumns = 
    SELECTCOLUMNS(
        INFO.COLUMNS(),
        "ToColumnID", [ID],
        "To Column Name", [Name]
    )

VAR _CombinedTable1 = 
    NATURALLEFTOUTERJOIN(
        _Relationships,
        _FromTables
    )

VAR _CombinedTable2 = 
    NATURALLEFTOUTERJOIN(
        _CombinedTable1,
        _ToTables
    )

VAR _CombinedTable3 = 
    NATURALLEFTOUTERJOIN(
        _CombinedTable2,
        _FromColumns
    )

VAR _CombinedTable4 = 
    NATURALLEFTOUTERJOIN(
        _CombinedTable3,
        _ToColumns
    )

RETURN
    SELECTCOLUMNS(
        _CombinedTable4,
        "Relationship Name", [Relationship Name],
        "From Table", [From Table Name],
        "From Column", [From Column Name],
        "To Table", [To Table Name],
        "To Column", [To Column Name],
        "Is Active", [Is Active],
        "Type", [Type],
        "Cross Filtering", [Cross Filtering]
    )
ORDER BY [Relationship Name]
```

## See also

- [INFO.TABLES](info-tables-function-dax.md)
- [INFO.COLUMNS](info-columns-function-dax.md)
- [INFO.PARTITIONS](info-partitions-function-dax.md)
- [INFO functions overview](info-functions-dax.md)
