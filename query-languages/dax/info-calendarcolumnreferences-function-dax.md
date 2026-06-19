---
description: "Learn more about: INFO.CALENDARCOLUMNREFERENCES"
title: "INFO.CALENDARCOLUMNREFERENCES function (DAX)"
author: jajin
---
# INFO.CALENDARCOLUMNREFERENCES

[!INCLUDE[applies-to-query-only](includes/applies-to-query-only.md)]

Returns a table with information about each calendar column reference in the semantic model. Calendar column references associate columns to calendar column groups.

## Syntax

```dax
INFO.CALENDARCOLUMNREFERENCES ( [<Restriction name>, <Restriction value>], ... )
```

[!INCLUDE[parameters-for-info-dax-functions](includes/parameters-for-info-dax-functions.md)]

## Return value

A table with the following columns:

| Column | Description |
|---|---|
| ID | Unique identifier for the calendar column reference |
| CalendarColumnGroupID | ID of the calendar column group this calendar column reference belongs to |
| ColumnID | ID of the column being referenced |
| IsPrimaryColumn | Indicates whether this is the primary column in the calendar column group |
| ModifiedTime | When the calendar column reference was last modified |

## Remarks

- Typically used in DAX queries to inspect and document model metadata.
- Permissions required depend on the host. Querying full metadata may require model admin permissions.

## Example

The following DAX query can be run in [DAX query view](/power-bi/transform-model/dax-query-view):

```dax
EVALUATE
	INFO.CALENDARCOLUMNREFERENCES()
```

### Example 2 - DAX query with joins

The following DAX query can be run in [DAX query view](/power-bi/transform-model/dax-query-view):

```dax
EVALUATE
VAR _CalendarColumnGroups = 
    SELECTCOLUMNS(
        INFO.CALENDARCOLUMNGROUPS(),
        "GroupID", [ID],
        "CalendarID", [CalendarID],
        "Category", [TimeUnit]
    )

VAR _CalendarColumnReferences = 
    SELECTCOLUMNS(
        INFO.CALENDARCOLUMNREFERENCES(),
        "GroupID", [CalendarColumnGroupID],
        "ColumnID", [ColumnID],
		"IsPrimaryColumn", [IsPrimaryColumn]
    )

VAR _Calendars = 
    SELECTCOLUMNS(
        INFO.CALENDARS(),
        "CalendarID", [ID],
        "Calendar Name", [Name]
    )

VAR _Columns = 
    SELECTCOLUMNS(
        INFO.COLUMNS(),
        "ColumnID", [ID],
        "Column Name", [ExplicitName]
    )

VAR _GroupsWithReferences = 
    NATURALLEFTOUTERJOIN(
        _CalendarColumnGroups,
        _CalendarColumnReferences
    )

VAR _WithCalendars = 
    NATURALLEFTOUTERJOIN(
        _GroupsWithReferences,
        _Calendars
    )

VAR _WithColumns = 
    NATURALLEFTOUTERJOIN(
        _WithCalendars,
        _Columns
    )

RETURN
    SELECTCOLUMNS(
        _WithColumns,
        "Calendar Name", [Calendar Name],
        "Category", [Category],
		"Is Primary Column", [IsPrimaryColumn],
        "Column Name", [Column Name]
    )
ORDER BY [Calendar Name], [Category], [Is Primary Column], [Column Name]
```

## See also

- [INFO.CALENDARS](info-calendars-function-dax.md)
- [INFO.CALENDARCOLUMNGROUPS](info-calendarcolumngroups-function-dax.md)
- [INFO.COLUMNS](info-columns-function-dax.md)
- [INFO functions overview](info-functions-dax.md)
