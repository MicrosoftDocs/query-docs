---
description: "Learn more about: INFO.STORAGEFILES"
title: "INFO.STORAGEFILES function (DAX)"
author: jeroenterheerdt
---
# INFO.STORAGEFILES

[!INCLUDE[applies-to-query-only](includes/applies-to-query-only.md)]

Returns a table with information about each storage file in the semantic model. This function provides metadata about storage files and their characteristics.

## Syntax

```dax
INFO.STORAGEFILES ( [<Restriction name>, <Restriction value>], ... )
```

[!INCLUDE[parameters-for-info-dax-functions](includes/parameters-for-info-dax-functions.md)]

## Return value

A table whose columns match the schema rowset for storage files in the current semantic model.

|Column|Description|
|---|---|
|ID|Unique identifier for the storage file|
|OwnerID|Identifier of the object that owns this storage file|
|OwnerType|Type of the object that owns this storage file|
|StorageFolderID|Foreign key to the storage folder containing this file|
|FileName|Name of the storage file|

## Remarks

- Typically used in DAX queries to inspect and document model metadata.
- Permissions required depend on the host. Querying full metadata may require model admin permissions.

## Example

The following DAX query can be run in [DAX query view](/power-bi/transform-model/dax-query-view):

```dax
EVALUATE
	INFO.STORAGEFILES()
```

### Example 2 - DAX query with joins

The following DAX query can be run in [DAX query view](/power-bi/transform-model/dax-query-view):

```dax
EVALUATE
VAR _StorageFiles = 
    SELECTCOLUMNS(
        INFO.STORAGEFILES(),
        "OwnerID", [OwnerID],
        "Owner Type", [OwnerType],
        "StorageFolderID", [StorageFolderID],
        "File Name", [FileName]
    )

VAR _StorageFolders = 
    SELECTCOLUMNS(
        INFO.STORAGEFOLDERS(),
        "StorageFolderID", [ID],
        "Folder Name", [Name]
    )

VAR _CombinedTable = 
    NATURALLEFTOUTERJOIN(
        _StorageFiles,
        _StorageFolders
    )

RETURN
    SELECTCOLUMNS(
        _CombinedTable,
        "Folder Name", [Folder Name],
        "File Name", [File Name],
        "Owner Type", [Owner Type],
        "Owner ID", [OwnerID]
    )
ORDER BY [Folder Name], [File Name]
```

## See also

- [INFO.COLUMNSTORAGES](info-columnstorages-function-dax.md)
- [INFO.COLUMNPARTITIONSTORAGES](info-columnpartitionstorages-function-dax.md)
- [INFO.DICTIONARYSTORAGES](info-dictionarystorages-function-dax.md)
- [INFO.SEGMENTSTORAGES](info-segmentstorages-function-dax.md)
- [INFO.TABLESTORAGES](info-tablestorages-function-dax.md)
