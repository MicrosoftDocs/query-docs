---
description: "Learn more about: INFO.TABLES"
title: "INFO.TABLES function (DAX)"
author: jeroenterheerdt
---
# INFO.TABLES

[!INCLUDE[applies-to-query-only](includes/applies-to-query-only.md)]

Returns a table with information about each table in the semantic model, with columns that match the schema rowset for table objects (for example, name, description, and visibility).

## Syntax

```dax
INFO.TABLES ( [<Restriction name>, <Restriction value>], ... )
```

[!INCLUDE[parameters-for-info-dax-functions](includes/parameters-for-info-dax-functions.md)]

## Return value

A table whose columns match the schema rowset for table objects in the current semantic model.

|Column|Description|
|---|---|
|ID|Unique identifier for the table|
|ModelID|Foreign key to the model containing this table|
|Name|Name of the table|
|DataCategory|Data category classification for the table|
|Description|Description of the table|
|IsHidden|Boolean indicating whether the table is hidden from client applications|
|TableStorageID|Foreign key to the table storage information|
|ModifiedTime|Date and time when the table was last modified|
|StructureModifiedTime|Date and time when the table structure was last modified|
|SystemFlags|System flags for internal table management|
|ShowAsVariationsOnly|Boolean indicating whether the table should only show variations|
|IsPrivate|Boolean indicating whether the table is private|
|DefaultDetailRowsDefinitionID|Foreign key to the default detail rows definition|
|AlternateSourcePrecedence|Precedence order for alternate data sources|
|RefreshPolicyID|Foreign key to the refresh policy for incremental refresh|
|CalculationGroupID|Foreign key to the calculation group if this table is a calculation group|
|ExcludeFromModelRefresh|Boolean indicating whether to exclude this table from model refresh|
|LineageTag|Lineage tag for tracking table lineage|
|SourceLineageTag|Source lineage tag from the original data source|
|SystemManaged|Boolean indicating whether the table is system-managed|

## Remarks

- Useful for documentation and governance scenarios.
- Permissions required depend on the host. Querying full metadata may require model admin permissions.

## Example

The following DAX query can be run in [DAX query view](/power-bi/transform-model/dax-query-view):

```dax
EVALUATE
	INFO.TABLES()
```

### Example 2 - DAX query with joins

The following DAX query can be run in [DAX query view](/power-bi/transform-model/dax-query-view):

```dax
EVALUATE
VAR _Tables = 
    SELECTCOLUMNS(
        INFO.TABLES(),
        "TableID", [ID],
        "Table Name", [Name],
        "Description", [Description],
        "Is Hidden", [IsHidden],
        "Calculation Group ID", [CalculationGroupID],
        "Refresh Policy ID", [RefreshPolicyID]
    )

VAR _CalculationGroups = 
    SELECTCOLUMNS(
        INFO.CALCULATIONGROUPS(),
        "CalculationGroupID", [ID],
        "Calculation Group Name", [Name]
    )

VAR _RefreshPolicies = 
    SELECTCOLUMNS(
        INFO.REFRESHPOLICIES(),
        "RefreshPolicyID", [ID],
        "Policy Type", [PolicyType],
        "Incremental Periods", [IncrementalPeriods]
    )

VAR _CombinedTable1 = 
    NATURALLEFTOUTERJOIN(
        _Tables,
        _CalculationGroups
    )

VAR _CombinedTable2 = 
    NATURALLEFTOUTERJOIN(
        _CombinedTable1,
        _RefreshPolicies
    )

RETURN
    SELECTCOLUMNS(
        _CombinedTable2,
        "Table Name", [Table Name],
        "Description", [Description],
        "Is Hidden", [Is Hidden],
        "Calculation Group", [Calculation Group Name],
        "Policy Type", [Policy Type],
        "Incremental Periods", [Incremental Periods]
    )
ORDER BY [Table Name]
```

## See also

[INFO.COLUMNS](info-columns-function-dax.md)
[INFO.PARTITIONS](info-partitions-function-dax.md)
[INFO.RELATIONSHIPS](info-relationships-function-dax.md)
[INFO functions overview](info-functions-dax.md)
