---
description: "Learn more about: INFO.RELATIONSHIPSTORAGES"
title: "INFO.RELATIONSHIPSTORAGES function (DAX)"
author: jeroenterheerdt
---
# INFO.RELATIONSHIPSTORAGES

[!INCLUDE[applies-to-query-only](includes/applies-to-query-only.md)]

Returns a table with information about each relationship storage in the semantic model. This function provides metadata about how relationships are stored.

## Syntax

```dax
INFO.RELATIONSHIPSTORAGES ( [<Restriction name>, <Restriction value>], ... )
```

[!INCLUDE[parameters-for-info-dax-functions](includes/parameters-for-info-dax-functions.md)]

## Return value

A table whose columns match the schema rowset for relationship storages in the current semantic model.

|Column|Description|
|---|---|
|ID|Unique identifier for the relationship storage|
|RelationshipID|Foreign key to the relationship using this storage|
|Name|Name of the relationship storage|
|DefinitionType|Type definition for the relationship storage|
|Cardinality|Cardinality characteristics of the relationship storage|
|Flags|Storage flags and configuration options|
|RelationshipIndexStorageID|Foreign key to the relationship index storage|

## Remarks

- Typically used in DAX queries to inspect and document model metadata.
- Permissions required depend on the host. Querying full metadata may require model admin permissions.

## Example

The following DAX query can be run in [DAX query view](/power-bi/transform-model/dax-query-view):

```dax
EVALUATE
	INFO.RELATIONSHIPSTORAGES()
```

### Example 2 - DAX query with joins

The following DAX query can be run in [DAX query view](/power-bi/transform-model/dax-query-view):

```dax
EVALUATE
VAR _RelationshipStorages = 
    SELECTCOLUMNS(
        INFO.RELATIONSHIPSTORAGES(),
        "RelationshipID", [RelationshipID],
        "Storage Name", [Name],
        "Definition Type", [DefinitionType],
        "Cardinality", [Cardinality],
        "Flags", [Flags]
    )

VAR _Relationships = 
    SELECTCOLUMNS(
        INFO.RELATIONSHIPS(),
        "RelationshipID", [ID],
        "Relationship Name", [Name],
        "Is Active", [IsActive],
        "Type", [Type]
    )

VAR _CombinedTable = 
    NATURALLEFTOUTERJOIN(
        _RelationshipStorages,
        _Relationships
    )

RETURN
    SELECTCOLUMNS(
        _CombinedTable,
        "Relationship Name", [Relationship Name],
        "Storage Name", [Storage Name],
        "Is Active", [Is Active],
        "Type", [Type],
        "Definition Type", [Definition Type],
        "Cardinality", [Cardinality]
    )
ORDER BY [Relationship Name]
```
## See also

[INFO.TABLES](info-tables-function-dax.md)
[INFO.COLUMNS](info-columns-function-dax.md)
[INFO.MEASURES](info-measures-function-dax.md)
[INFO functions overview](info-functions-dax.md)
