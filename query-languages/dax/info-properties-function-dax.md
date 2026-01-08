---
description: "Learn more about: INFO.PROPERTIES"
title: "INFO.PROPERTIES function (DAX)"
author: jeroenterheerdt
---
# INFO.PROPERTIES

[!INCLUDE[applies-to-query-only](includes/applies-to-query-only.md)]

Returns a table with information about each property in the semantic model. This function provides metadata about properties defined for model objects.

## Syntax

```dax
INFO.PROPERTIES ( [<Restriction name>, <Restriction value>], ... )
```

[!INCLUDE[parameters-for-info-dax-functions](includes/parameters-for-info-dax-functions.md)]

## Return value

A table whose columns match the schema rowset for properties in the current semantic model.

|Column|Description|
|---|---|
|PropertyName|Name of the property|
|PropertyDescription|Description explaining the purpose and usage of the property|
|PropertyType|Data type of the property value (e.g., String, Integer, Boolean)|
|PropertyAccessType|Access level of the property (e.g., Read, Write, ReadWrite)|
|IsRequired|Boolean indicating whether the property is required|
|Value|Current value of the property|

## Remarks

- Typically used in DAX queries to inspect and document model metadata.
- Permissions required depend on the host. Querying full metadata may require model admin permissions.

## Example

The following DAX query can be run in [DAX query view](/power-bi/transform-model/dax-query-view):

```dax
EVALUATE
	INFO.PROPERTIES()
```

## See also

[INFO.MODEL](info-model-function-dax.md)
[INFO.EXPRESSIONS](info-expressions-function-dax.md)
[INFO.CATALOGS](info-catalogs-function-dax.md)
[INFO.TABLES](info-tables-function-dax.md)
[INFO.COLUMNS](info-columns-function-dax.md)
