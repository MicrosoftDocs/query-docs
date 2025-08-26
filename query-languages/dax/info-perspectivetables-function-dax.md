---
description: "Learn more about: INFO.PERSPECTIVETABLES"
title: "INFO.PERSPECTIVETABLES function (DAX)"
author: jeroenterheerdt
---
# INFO.PERSPECTIVETABLES

[!INCLUDE[applies-to-query-only](includes/applies-to-query-only.md)]

Returns a table with information about each perspective table in the semantic model. This function provides metadata about tables included in perspectives.

## Syntax

```dax
INFO.PERSPECTIVETABLES ( [<Restriction name>, <Restriction value>], ... )
```

[!INCLUDE[parameters-for-info-dax-functions](includes/parameters-for-info-dax-functions.md)]

## Return value

A table whose columns match the schema rowset for perspective tables in the current semantic model.

|Column|Description|
|---|---|
|ID|Unique identifier for the perspective table relationship|
|PerspectiveID|Foreign key to the perspective containing this table|
|TableID|Foreign key to the table included in the perspective|
|IncludeAll|Boolean indicating whether all objects from the table are included in the perspective|
|ModifiedTime|Date and time when the perspective table was last modified|

## Remarks

- Typically used in DAX queries to inspect and document model metadata.
- Permissions required depend on the host. Querying full metadata may require model admin permissions.

## Example

The following DAX query can be run in [DAX query view](/power-bi/transform-model/dax-query-view):

```dax
EVALUATE
	INFO.PERSPECTIVETABLES()
```

### Example 2 - DAX query with joins

The following DAX query can be run in [DAX query view](/power-bi/transform-model/dax-query-view):

```dax
EVALUATE
VAR _PerspectiveTables = 
    SELECTCOLUMNS(
        INFO.PERSPECTIVETABLES(),
        "PerspectiveID", [PerspectiveID],
        "TableID", [TableID],
        "Include All", [IncludeAll],
        "Modified", [ModifiedTime]
    )

VAR _Perspectives = 
    SELECTCOLUMNS(
        INFO.PERSPECTIVES(),
        "PerspectiveID", [ID],
        "Perspective Name", [Name],
        "Perspective Description", [Description]
    )

VAR _Tables = 
    SELECTCOLUMNS(
        INFO.TABLES(),
        "TableID", [ID],
        "Table Name", [Name],
        "Table Description", [Description]
    )

VAR _CombinedTable1 = 
    NATURALLEFTOUTERJOIN(
        _PerspectiveTables,
        _Perspectives
    )

VAR _CombinedTable2 = 
    NATURALLEFTOUTERJOIN(
        _CombinedTable1,
        _Tables
    )

RETURN
    SELECTCOLUMNS(
        _CombinedTable2,
        "Perspective Name", [Perspective Name],
        "Table Name", [Table Name],
        "Include All", [Include All],
        "Modified", [Modified]
    )
ORDER BY [Perspective Name], [Table Name]
```

## See also

[INFO.PERSPECTIVES](info-perspectives-function-dax.md)
[INFO.PERSPECTIVECOLUMNS](info-perspectivecolumns-function-dax.md)
[INFO.PERSPECTIVEHIERARCHIES](info-perspectivehierarchies-function-dax.md)
[INFO.PERSPECTIVEMEASURES](info-perspectivemeasures-function-dax.md)
[INFO.TABLES](info-tables-function-dax.md)
