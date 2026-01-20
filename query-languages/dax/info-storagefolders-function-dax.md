---
description: "Learn more about: INFO.STORAGEFOLDERS"
title: "INFO.STORAGEFOLDERS function (DAX)"
author: jeroenterheerdt
---
# INFO.STORAGEFOLDERS

[!INCLUDE[applies-to-query-only](includes/applies-to-query-only.md)]

Returns a table with information about all table storage in the semantic model. This information helps you understand the model.

## Syntax

```dax
INFO.STORAGEFOLDERS([<Restriction name>, <Restriction value>], ...)
```

[!INCLUDE[parameters-for-info-dax-functions](includes/parameters-for-info-dax-functions.md)]

## Return value

A table with the following columns:

|Column|Description|
|---|---|
|[ID]|The name of the database|
|[OwnerID]||
|[OwnerType]||
|[Path]||

## Remarks

Can only be ran by users with write permission on the semantic model and not when live connected to the semantic model in Power BI Desktop. This function can be used in [DAX queries](/dax/dax-queries), and can't be used in calculations.

## Example 1 - DAX query

The following DAX query can be run in [DAX query view](/power-bi/transform-model/dax-query-view):

```dax
EVALUATE
	INFO.STORAGEFOLDERS()
```
## See also

[INFO.TABLES](info-tables-function-dax.md)
[INFO.COLUMNS](info-columns-function-dax.md)
[INFO.MEASURES](info-measures-function-dax.md)
[INFO functions overview](info-functions-dax.md)
