---
description: "Learn more about: INFO.DEPENDENCIES"
title: "INFO.DEPENDENCIES function (DAX)"
author: jeroenterheerdt
---
# INFO.DEPENDENCIES

[!INCLUDE[applies-to-query-only](includes/applies-to-query-only.md)]

Returns a table with information about each dependency in the semantic model. This function provides metadata about object dependencies and relationships between model objects.

## Syntax

```dax
INFO.DEPENDENCIES ( [<Restriction name>, <Restriction value>], ... )
```

[!INCLUDE[parameters-for-info-dax-functions](includes/parameters-for-info-dax-functions.md)]

## Return value

A table with the following columns:

| Column name | Data type | Description |
| --- | --- | --- |
| [DATABASE_NAME] | String | Name of the database containing the object |
| [OBJECT_TYPE] | String | Type of the object (e.g., ATTRIBUTE_HIERARCHY, HIERARCHY, MEASURE) |
| [TABLE] | String | Name of the table containing the object |
| [OBJECT] | String | Name of the object |
| [EXPRESSION] | String | Expression associated with the object |
| [REFERENCED_OBJECT_TYPE] | String | Type of the referenced object |
| [REFERENCED_TABLE] | String | Name of the table containing the referenced object |
| [REFERENCED_OBJECT] | String | Name of the referenced object |
| [REFERENCED_EXPRESSION] | String | Expression of the referenced object |
| [QUERY] | String | Query context for the dependency |

## Remarks

- Typically used in DAX queries to inspect and document model metadata.
- Permissions required depend on the host. Querying full metadata may require model admin permissions.

## Example

The following DAX query can be run in [DAX query view](/power-bi/transform-model/dax-query-view):

```dax
EVALUATE
	INFO.DEPENDENCIES()
```

## Example 2 - DAX query with joins

The following DAX query can be run in [DAX query view](/power-bi/transform-model/dax-query-view):

```dax
EVALUATE
	VAR _Dependencies =
		INFO.DEPENDENCIES()

	VAR _Tables = 
		SELECTCOLUMNS(
			INFO.TABLES(),
			"TABLE", [Name],
			"Table ID", [ID]
		)

	VAR _ReferencedTables = 
		SELECTCOLUMNS(
			INFO.TABLES(),
			"REFERENCED_TABLE", [Name],
			"Referenced Table ID", [ID]
		)

	VAR _CombinedWithTables =
		NATURALLEFTOUTERJOIN(
			_Dependencies,
			_Tables
		)

	VAR _CombinedWithReferencedTables =
		NATURALLEFTOUTERJOIN(
			_CombinedWithTables,
			_ReferencedTables
		)

	RETURN
		SELECTCOLUMNS(
			_CombinedWithReferencedTables,
			"Object Type", [OBJECT_TYPE],
			"Table", [TABLE],
			"Object", [OBJECT],
			"Referenced Object Type", [REFERENCED_OBJECT_TYPE],
			"Referenced Table", [REFERENCED_TABLE],
			"Referenced Object", [REFERENCED_OBJECT]
		)
	ORDER BY [TABLE], [OBJECT]
```
## See also

- [INFO.CALCDEPENDENCY](info-calcdependency-function-dax.md)
- [INFO.RELATEDCOLUMNDETAILS](info-relatedcolumndetails-function-dax.md)
- [INFO.TABLES](info-tables-function-dax.md)
- [INFO.COLUMNS](info-columns-function-dax.md)
- [INFO.MEASURES](info-measures-function-dax.md)
