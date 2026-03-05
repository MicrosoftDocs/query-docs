---
description: "Learn more about: INFO.HIERARCHIES"
title: "INFO.HIERARCHIES function (DAX)"
author: jeroenterheerdt
---
# INFO.HIERARCHIES

[!INCLUDE[applies-to-query-only](includes/applies-to-query-only.md)]

Returns a table with information about each hierarchy in the semantic model. This function provides metadata about hierarchies and their properties.

## Syntax

```dax
INFO.HIERARCHIES ( [<Restriction name>, <Restriction value>], ... )
```

[!INCLUDE[parameters-for-info-dax-functions](includes/parameters-for-info-dax-functions.md)]

## Return value

A table with the following columns:

| Column | Description |
|--------|-------------|
| [ID] | Unique identifier for the hierarchy |
| [TableID] | Identifier of the table containing the hierarchy |
| [Name] | Name of the hierarchy |
| [Description] | Description of the hierarchy |
| [IsHidden] | Boolean indicating if the hierarchy is hidden from client tools |
| [State] | Current state of the hierarchy (e.g., Ready, Processing) |
| [HierarchyStorageID] | Identifier linking to the hierarchy storage information |
| [ModifiedTime] | Timestamp of when the hierarchy was last modified |
| [StructureModifiedTime] | Timestamp of when the hierarchy structure was last modified |
| [RefreshedTime] | Timestamp of when the hierarchy was last refreshed |
| [DisplayFolder] | Display folder for organizing hierarchies in client tools |
| [HideMembers] | Setting for hiding hierarchy members |
| [LineageTag] | Lineage tag for tracking data lineage |
| [SourceLineageTag] | Source lineage tag from the original data source |

## Remarks

- Typically used in DAX queries to inspect and document model metadata.
- Permissions required depend on the host. Querying full metadata may require model admin permissions.

## Example

The following DAX query can be run in [DAX query view](/power-bi/transform-model/dax-query-view):

```dax
EVALUATE
	INFO.HIERARCHIES()
```

## Example 2 - DAX query with joins

The following DAX query can be run in [DAX query view](/power-bi/transform-model/dax-query-view):

```dax
EVALUATE
	VAR _Hierarchies =
		SELECTCOLUMNS(
			INFO.HIERARCHIES(),
			"HierarchyID", [ID],
			"Hierarchy Name", [Name],
			"TableID", [TableID]
		)
	VAR _Tables = 
		SELECTCOLUMNS(
			INFO.TABLES(),
			"TableID", [ID],
			"Table Name", [Name]
		)
	VAR _CombinedTable =
		NATURALLEFTOUTERJOIN(
			_Hierarchies,
			_Tables
		)
	RETURN
		_CombinedTable
	ORDER BY [Hierarchy Name]
```

## See also

- [INFO.ATTRIBUTEHIERARCHIES](info-attributehierarchies-function-dax.md)
- [INFO.HIERARCHYSTORAGES](info-hierarchystorages-function-dax.md)
- [INFO.ATTRIBUTEHIERARCHYSTORAGES](info-attributehierarchystorages-function-dax.md)
- [INFO.LEVELS](info-levels-function-dax.md)
- [INFO.TABLES](info-tables-function-dax.md)
