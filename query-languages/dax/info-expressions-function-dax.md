---
description: "Learn more about: INFO.EXPRESSIONS"
title: "INFO.EXPRESSIONS function (DAX)"
author: jeroenterheerdt
---
# INFO.EXPRESSIONS

[!INCLUDE[applies-to-query-only](includes/applies-to-query-only.md)]

Returns a table with information about each expression in the semantic model. This function provides metadata about expressions defined in the model.

## Syntax

```dax
INFO.EXPRESSIONS ( [<Restriction name>, <Restriction value>], ... )
```

[!INCLUDE[parameters-for-info-dax-functions](includes/parameters-for-info-dax-functions.md)]

## Return value

A table with the following columns:

| Column name | Data type | Description |
|--|--|--|
| [ID] | Integer | Unique identifier for the expression |
| [ModelID] | Integer | Identifier of the model containing the expression |
| [Name] | String | Name of the expression |
| [Description] | String | Description of the expression |
| [Kind] | Integer | Type of expression (e.g., calculated table, shared expression) |
| [Expression] | String | DAX expression text |
| [ModifiedTime] | DateTime | When the expression was last modified |
| [QueryGroupID] | Integer | Identifier of the query group if applicable |
| [ParameterValuesColumnID] | Integer | Column identifier for parameter values if applicable |
| [MAttributes] | String | Additional attributes in JSON format |
| [LineageTag] | String | Lineage tag for tracking purposes |
| [SourceLineageTag] | String | Source lineage tag for tracking purposes |

## Remarks

- Typically used in DAX queries to inspect and document model metadata.
- Permissions required depend on the host. Querying full metadata may require model admin permissions.

## Example

The following DAX query can be run in [DAX query view](/power-bi/transform-model/dax-query-view):

```dax
EVALUATE
	INFO.EXPRESSIONS()
```

## See also

- [INFO.MODEL](info-model-function-dax.md)
- [INFO.PROPERTIES](info-properties-function-dax.md)
- [INFO.CATALOGS](info-catalogs-function-dax.md)
- [INFO.TABLES](info-tables-function-dax.md)
- [INFO.COLUMNS](info-columns-function-dax.md)
