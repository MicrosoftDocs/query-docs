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

## Remarks

- Typically used in DAX queries to inspect and document model metadata.
- Permissions required depend on the host. Querying full metadata may require model admin permissions.

## Example

The following DAX query can be run in [DAX query view](/power-bi/transform-model/dax-query-view):

```dax
EVALUATE
	INFO.STORAGEFILES()
```

## Example 2 - DAX query with SELECTCOLUMNS

```dax
EVALUATE
    SELECTCOLUMNS(
        INFO.STORAGEFILES(),
        "FileID", [FileID],
        "State", [State],
        "FileSize", [FileSize]
    )
```

## Example 3 - Calculated table

```dax
Storage Files =
SELECTCOLUMNS(
    INFO.STORAGEFILES(),
    "FileID", [FileID],
    "State", [State]
)
```

## Example 4 - Measure

```dax
Number of Storage Files =
COUNTROWS(INFO.STORAGEFILES())
```
## See also

[INFO.COLUMNSTORAGES](info-columnstorages-function-dax.md)
[INFO.COLUMNPARTITIONSTORAGES](info-columnpartitionstorages-function-dax.md)
[INFO.DICTIONARYSTORAGES](info-dictionarystorages-function-dax.md)
[INFO.SEGMENTSTORAGES](info-segmentstorages-function-dax.md)
[INFO.TABLESTORAGES](info-tablestorages-function-dax.md)
