---
description: "Learn more about: INFO.CSDLMETADATA"
title: "INFO.CSDLMETADATA function (DAX)"
author: jeroenterheerdt
---
# INFO.CSDLMETADATA

[!INCLUDE[applies-to-query-only](includes/applies-to-query-only.md)]

Returns a table with information about the CSDL metadata in the semantic model. This function provides metadata about the Conceptual Schema Definition Language representation of the model.

## Syntax

```dax
INFO.CSDLMETADATA ( [<Restriction name>, <Restriction value>], ... )
```

[!INCLUDE[parameters-for-info-dax-functions](includes/parameters-for-info-dax-functions.md)]

## Return value

A table whose columns match the schema rowset for CSDL metadata in the current semantic model.

|Column|Description|
|---|---|
|CATALOG_NAME|Name of the catalog containing the CSDL metadata|
|SCHEMA_NAME|Name of the schema containing the CSDL metadata|
|CSDL_METADATA|The complete CSDL (Conceptual Schema Definition Language) XML metadata|
|DATE_MODIFIED|Date and time when the CSDL metadata was last modified|
|SCHEMA_VERSION|Version of the CSDL schema being used|

## Remarks

- Typically used in DAX queries to inspect and document model metadata.
- Permissions required depend on the host. Querying full metadata may require model admin permissions.

## Example

The following DAX query can be run in [DAX query view](/power-bi/transform-model/dax-query-view):

```dax
EVALUATE
	INFO.CSDLMETADATA()
```

## See also

- [INFO.TABLES](info-tables-function-dax.md)
- [INFO.COLUMNS](info-columns-function-dax.md)
- [INFO.MEASURES](info-measures-function-dax.md)
- [INFO functions overview](info-functions-dax.md)
