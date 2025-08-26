---
description: "Learn more about: INFO.HIERARCHYSTORAGES"
title: "INFO.HIERARCHYSTORAGES function (DAX)"
author: jeroenterheerdt
---
# INFO.HIERARCHYSTORAGES

[!INCLUDE[applies-to-query-only](includes/applies-to-query-only.md)]

Returns a table with information about each hierarchy storage in the semantic model. This function provides metadata about how hierarchies are stored.

## Syntax

```dax
INFO.HIERARCHYSTORAGES ( [<Restriction name>, <Restriction value>], ... )
```

[!INCLUDE[parameters-for-info-dax-functions](includes/parameters-for-info-dax-functions.md)]

## Return value

A table with the following columns:

| Column | Description |
|--------|-------------|
| [ID] | Unique identifier for the hierarchy storage |
| [HierarchyID] | Identifier linking to the hierarchy |
| [Name] | Name of the hierarchy storage |
| [LevelDefinition] | Definition of levels within the hierarchy |
| [MaterializationType] | Type of materialization used for the hierarchy storage |
| [StructureType] | Type of structure used for the hierarchy |
| [SystemTableID] | Identifier of the system table associated with the hierarchy |

## Remarks

- Typically used in DAX queries to inspect and document model metadata.
- Permissions required depend on the host. Querying full metadata may require model admin permissions.

## Example

The following DAX query can be run in [DAX query view](/power-bi/transform-model/dax-query-view):

```dax
EVALUATE
	INFO.HIERARCHYSTORAGES()
```

## Example 2 - DAX query with joins

The following DAX query can be run in [DAX query view](/power-bi/transform-model/dax-query-view):

```dax
EVALUATE
	VAR _HierarchyStorages =
		SELECTCOLUMNS(
			INFO.HIERARCHYSTORAGES(),
			"HierarchyStorageID", [ID],
			"HierarchyID", [HierarchyID],
			"Storage Name", [Name]
		)
	VAR _Hierarchies = 
		SELECTCOLUMNS(
			INFO.HIERARCHIES(),
			"HierarchyID", [ID],
			"Hierarchy Name", [Name]
		)
	VAR _CombinedTable =
		NATURALLEFTOUTERJOIN(
			_HierarchyStorages,
			_Hierarchies
		)
	RETURN
		SELECTCOLUMNS(
			_CombinedTable,
			"Hierarchy Name", [Hierarchy Name],
			"Storage Name", [Storage Name],
			"Materialization Type", [MaterializationType]
		)
	ORDER BY [Hierarchy Name]
```

## See also

[INFO.HIERARCHIES](info-hierarchies-function-dax.md)
[INFO.ATTRIBUTEHIERARCHIES](info-attributehierarchies-function-dax.md)
[INFO.ATTRIBUTEHIERARCHYSTORAGES](info-attributehierarchystorages-function-dax.md)
[INFO.LEVELS](info-levels-function-dax.md)
[INFO.TABLES](info-tables-function-dax.md)
