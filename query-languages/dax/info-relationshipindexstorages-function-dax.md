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

|Column|Description|
|---|---|
|ID|Unique identifier for the relationship index storage|
|RelationshipStorageID|Foreign key to the relationship storage using this index|
|IndexType|Type of index used for the relationship|
|Flags|Index configuration flags and options|
|RecordCount|Number of records in the relationship index|
|SecondaryRecordCount|Number of secondary records in the relationship index|
|StorageFolderID|Foreign key to the storage folder containing the index|
|StorageFileID|Foreign key to the storage file containing the index|
|SystemTableID|Foreign key to the primary system table|
|SecondarySystemTableID|Foreign key to the secondary system table|

## Remarks

- Typically used in DAX queries to inspect and document model metadata.
- Permissions required depend on the host. Querying full metadata may require model admin permissions.

## Example

The following DAX query can be run in [DAX query view](/power-bi/transform-model/dax-query-view):

```dax
EVALUATE
	INFO.RELATIONSHIPINDEXSTORAGES()
```

### Example 2 - DAX query with joins

The following DAX query can be run in [DAX query view](/power-bi/transform-model/dax-query-view):

```dax
EVALUATE
VAR _RelationshipIndexStorages = 
    SELECTCOLUMNS(
        INFO.RELATIONSHIPINDEXSTORAGES(),
        "RelationshipStorageID", [RelationshipStorageID],
        "Index Type", [IndexType],
        "Record Count", [RecordCount],
        "Secondary Record Count", [SecondaryRecordCount],
        "Flags", [Flags]
    )

VAR _RelationshipStorages = 
    SELECTCOLUMNS(
        INFO.RELATIONSHIPSTORAGES(),
        "RelationshipStorageID", [ID],
        "RelationshipID", [RelationshipID],
        "Storage Name", [Name]
    )

VAR _Relationships = 
    SELECTCOLUMNS(
        INFO.RELATIONSHIPS(),
        "RelationshipID", [ID],
        "Relationship Name", [Name]
    )

VAR _CombinedTable1 = 
    NATURALLEFTOUTERJOIN(
        _RelationshipIndexStorages,
        _RelationshipStorages
    )

VAR _CombinedTable2 = 
    NATURALLEFTOUTERJOIN(
        _CombinedTable1,
        _Relationships
    )

RETURN
    SELECTCOLUMNS(
        _CombinedTable2,
        "Relationship Name", [Relationship Name],
        "Storage Name", [Storage Name],
        "Index Type", [Index Type],
        "Record Count", [Record Count],
        "Secondary Record Count", [Secondary Record Count]
    )
ORDER BY [Relationship Name]
```

## See also

[INFO.TABLES](info-tables-function-dax.md)
[INFO.COLUMNS](info-columns-function-dax.md)
[INFO.MEASURES](info-measures-function-dax.md)
[INFO functions overview](info-functions-dax.md)
