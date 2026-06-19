---
description: "Learn more about: INFO.LEVELS"
title: "INFO.LEVELS function (DAX)"
author: jeroenterheerdt
---
# INFO.LEVELS

[!INCLUDE[applies-to-query-only](includes/applies-to-query-only.md)]

Returns a table with information about each level in the semantic model. This function provides metadata about hierarchy levels and their properties.

## Syntax

```dax
INFO.LEVELS ( [<Restriction name>, <Restriction value>], ... )
```

[!INCLUDE[parameters-for-info-dax-functions](includes/parameters-for-info-dax-functions.md)]

## Return value

A table with the following columns:

| Column | Description |
|--------|-------------|
| [ID] | Unique identifier for the level |
| [HierarchyID] | Identifier of the hierarchy containing this level |
| [Ordinal] | Ordinal position of the level within the hierarchy |
| [Name] | Name of the level |
| [Description] | Description of the level |
| [ColumnID] | Identifier of the column associated with this level |
| [ModifiedTime] | Timestamp of when the level was last modified |
| [LineageTag] | Lineage tag for tracking data lineage |
| [SourceLineageTag] | Source lineage tag from the original data source |

## Remarks

- Typically used in DAX queries to inspect and document model metadata.
- Permissions required depend on the host. Querying full metadata may require model admin permissions.

## Example

The following DAX query can be run in [DAX query view](/power-bi/transform-model/dax-query-view):

```dax
EVALUATE
	INFO.LEVELS()
```

## Example 2 - DAX query with joins

The following DAX query can be run in [DAX query view](/power-bi/transform-model/dax-query-view):

```dax
EVALUATE
	VAR _Levels =
		SELECTCOLUMNS(
			INFO.LEVELS(),
			"LevelID", [ID],
			"HierarchyID", [HierarchyID],
			"Level Name", [Name],
			"Ordinal", [Ordinal]
		)
	VAR _Hierarchies = 
		SELECTCOLUMNS(
			INFO.HIERARCHIES(),
			"HierarchyID", [ID],
			"Hierarchy Name", [Name]
		)
	VAR _CombinedTable =
		NATURALLEFTOUTERJOIN(
			_Levels,
			_Hierarchies
		)
	RETURN
		SELECTCOLUMNS(
			_CombinedTable,
			"Hierarchy Name", [Hierarchy Name],
			"Level Name", [Level Name],
			"Ordinal", [Ordinal]
		)
	ORDER BY [Hierarchy Name], [Ordinal]
```

## See also

- [INFO.HIERARCHIES](info-hierarchies-function-dax.md)
- [INFO.ATTRIBUTEHIERARCHIES](info-attributehierarchies-function-dax.md)
- [INFO.HIERARCHYSTORAGES](info-hierarchystorages-function-dax.md)
- [INFO.ATTRIBUTEHIERARCHYSTORAGES](info-attributehierarchystorages-function-dax.md)
- [INFO.TABLES](info-tables-function-dax.md)