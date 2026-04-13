---
description: "Learn more about: INFO.CALENDARS"
title: "INFO.CALENDARS function (DAX)"
author: jajin
---
# INFO.CALENDARS

[!INCLUDE[applies-to-query-only](includes/applies-to-query-only.md)]

Returns a table with information about each calendar in the semantic model. This function provides metadata about calendars defined on tables.

## Syntax

```dax
INFO.CALENDARS ( [<Restriction name>, <Restriction value>], ... )
```

[!INCLUDE[parameters-for-info-dax-functions](includes/parameters-for-info-dax-functions.md)]

## Return value

A table with the following columns:

| Column | Description |
|---|---|
| ID | Unique identifier for the calendar |
| TableID | ID of the table this calendar belongs to |
| Name | Name of the calendar |
| Description | Description of the calendar |
| LineageTag | Lineage tag for tracking calendar lineage |
| SourceLineageTag | Source lineage tag |
| ModifiedTime | When the calendar was last modified |

## Remarks

- Typically used in DAX queries to inspect and document model metadata.
- Permissions required depend on the host. Querying full metadata may require model admin permissions.

## Example

The following DAX query can be run in [DAX query view](/power-bi/transform-model/dax-query-view):

```dax
EVALUATE
	INFO.CALENDARS()
```

### Example 2 - DAX query with joins

The following DAX query can be run in [DAX query view](/power-bi/transform-model/dax-query-view):

```dax
EVALUATE
VAR _Calendars = 
    SELECTCOLUMNS(
        INFO.CALENDARS(),
        "CalendarID", [ID],
        "Calendar Name", [Name],
        "Description", [Description],
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
        _Calendars,
        _Tables
    )

RETURN
    SELECTCOLUMNS(
        _CombinedTable,
        "Table Name", [Table Name],
        "Calendar Name", [Calendar Name],
        "Description", [Description]
    )
ORDER BY [Table Name], [Calendar Name]
```

## See also

- [INFO.CALENDARCOLUMNGROUPS](info-calendarcolumngroups-function-dax.md)
- [INFO.CALENDARCOLUMNREFERENCES](info-calendarcolumnreferences-function-dax.md)
- [INFO.TABLES](info-tables-function-dax.md)
- [INFO functions overview](info-functions-dax.md)
