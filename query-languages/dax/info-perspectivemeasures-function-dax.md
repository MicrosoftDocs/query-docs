---
description: "Learn more about: INFO.PERSPECTIVEMEASURES"
title: "INFO.PERSPECTIVEMEASURES function (DAX)"
author: jeroenterheerdt
---
# INFO.PERSPECTIVEMEASURES

[!INCLUDE[applies-to-query-only](includes/applies-to-query-only.md)]

Returns a table with information about each perspective measure in the semantic model. This function provides metadata about measures included in perspectives.

## Syntax

```dax
INFO.PERSPECTIVEMEASURES ( [<Restriction name>, <Restriction value>], ... )
```

[!INCLUDE[parameters-for-info-dax-functions](includes/parameters-for-info-dax-functions.md)]

## Return value

A table whose columns match the schema rowset for perspective measures in the current semantic model.

|Column|Description|
|---|---|
|ID|Unique identifier for the perspective measure relationship|
|PerspectiveTableID|Foreign key to the perspective table containing this measure|
|MeasureID|Foreign key to the measure included in the perspective|
|ModifiedTime|Date and time when the perspective measure was last modified|

## Remarks

- Typically used in DAX queries to inspect and document model metadata.
- Permissions required depend on the host. Querying full metadata may require model admin permissions.

## Example

The following DAX query can be run in [DAX query view](/power-bi/transform-model/dax-query-view):

```dax
EVALUATE
	INFO.PERSPECTIVEMEASURES()
```

### Example 2 - DAX query with joins

The following DAX query can be run in [DAX query view](/power-bi/transform-model/dax-query-view):

```dax
EVALUATE
VAR _PerspectiveMeasures = 
    SELECTCOLUMNS(
        INFO.PERSPECTIVEMEASURES(),
        "PerspectiveTableID", [PerspectiveTableID],
        "MeasureID", [MeasureID],
        "Modified", [ModifiedTime]
    )

VAR _PerspectiveTables = 
    SELECTCOLUMNS(
        INFO.PERSPECTIVETABLES(),
        "PerspectiveTableID", [ID],
        "PerspectiveID", [PerspectiveID],
        "TableID", [TableID]
    )

VAR _Measures = 
    SELECTCOLUMNS(
        INFO.MEASURES(),
        "MeasureID", [ID],
        "Measure Name", [Name],
        "Table ID", [TableID]
    )

VAR _Perspectives = 
    SELECTCOLUMNS(
        INFO.PERSPECTIVES(),
        "PerspectiveID", [ID],
        "Perspective Name", [Name]
    )

VAR _CombinedTable1 = 
    NATURALLEFTOUTERJOIN(
        _PerspectiveMeasures,
        _PerspectiveTables
    )

VAR _CombinedTable2 = 
    NATURALLEFTOUTERJOIN(
        _CombinedTable1,
        _Measures
    )

VAR _CombinedTable3 = 
    NATURALLEFTOUTERJOIN(
        _CombinedTable2,
        _Perspectives
    )

RETURN
    SELECTCOLUMNS(
        _CombinedTable3,
        "Perspective Name", [Perspective Name],
        "Measure Name", [Measure Name],
        "Modified", [Modified]
    )
ORDER BY [Perspective Name], [Measure Name]
```

## See also

[INFO.PERSPECTIVES](info-perspectives-function-dax.md)
[INFO.PERSPECTIVECOLUMNS](info-perspectivecolumns-function-dax.md)
[INFO.PERSPECTIVEHIERARCHIES](info-perspectivehierarchies-function-dax.md)
[INFO.PERSPECTIVETABLES](info-perspectivetables-function-dax.md)
[INFO.TABLES](info-tables-function-dax.md)
