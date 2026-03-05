---
description: "Learn more about: INFO.REFRESHPOLICIES"
title: "INFO.REFRESHPOLICIES function (DAX)"
author: jeroenterheerdt
---
# INFO.REFRESHPOLICIES

[!INCLUDE[applies-to-query-only](includes/applies-to-query-only.md)]

Returns a table with information about each refresh policy in the semantic model. This function provides metadata about refresh policies defined for tables.

## Syntax

```dax
INFO.REFRESHPOLICIES ( [<Restriction name>, <Restriction value>], ... )
```

[!INCLUDE[parameters-for-info-dax-functions](includes/parameters-for-info-dax-functions.md)]

## Return value

A table whose columns match the schema rowset for refresh policies in the current semantic model.

|Column|Description|
|---|---|
|ID|Unique identifier for the refresh policy|
|TableID|Foreign key to the table this refresh policy applies to|
|PolicyType|Type of refresh policy (e.g., Incremental, Rolling Window)|
|RollingWindowGranularity|Granularity for rolling window refresh (e.g., Day, Month, Year)|
|RollingWindowPeriods|Number of periods to keep in rolling window|
|IncrementalGranularity|Granularity for incremental refresh (e.g., Day, Month, Year)|
|IncrementalPeriods|Number of periods for incremental refresh|
|IncrementalPeriodsOffset|Offset periods for incremental refresh timing|
|PollingExpression|DAX expression used for polling to detect changes|
|SourceExpression|DAX expression defining the source data for refresh|
|Mode|Refresh mode configuration|

## Remarks

- Typically used in DAX queries to inspect and document model metadata.
- Permissions required depend on the host. Querying full metadata may require model admin permissions.

## Example

The following DAX query can be run in [DAX query view](/power-bi/transform-model/dax-query-view):

```dax
EVALUATE
	INFO.REFRESHPOLICIES()
```

### Example 2 - DAX query with joins

The following DAX query can be run in [DAX query view](/power-bi/transform-model/dax-query-view):

```dax
EVALUATE
VAR _RefreshPolicies = 
    SELECTCOLUMNS(
        INFO.REFRESHPOLICIES(),
        "TableID", [TableID],
        "Policy Type", [PolicyType],
        "Rolling Window Granularity", [RollingWindowGranularity],
        "Rolling Window Periods", [RollingWindowPeriods],
        "Incremental Granularity", [IncrementalGranularity],
        "Incremental Periods", [IncrementalPeriods]
    )

VAR _Tables = 
    SELECTCOLUMNS(
        INFO.TABLES(),
        "TableID", [ID],
        "Table Name", [Name],
        "Description", [Description]
    )

VAR _CombinedTable = 
    NATURALLEFTOUTERJOIN(
        _RefreshPolicies,
        _Tables
    )

RETURN
    SELECTCOLUMNS(
        _CombinedTable,
        "Table Name", [Table Name],
        "Description", [Description],
        "Policy Type", [Policy Type],
        "Rolling Window Granularity", [Rolling Window Granularity],
        "Rolling Window Periods", [Rolling Window Periods],
        "Incremental Granularity", [Incremental Granularity],
        "Incremental Periods", [Incremental Periods]
    )
ORDER BY [Table Name]
```

## See also

- [INFO.TABLES](info-tables-function-dax.md)
- [INFO.COLUMNS](info-columns-function-dax.md)
- [INFO.MEASURES](info-measures-function-dax.md)
- [INFO functions overview](info-functions-dax.md)
