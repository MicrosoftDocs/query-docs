---
description: "Learn more about: INFO.CALENDARCOLUMNGROUPS"
title: "INFO.CALENDARCOLUMNGROUPS function (DAX)"
author: jajin
---
# INFO.CALENDARCOLUMNGROUPS

[!INCLUDE[applies-to-query-only](includes/applies-to-query-only.md)]

Returns a table with information about each calendar column group in the semantic model. Calendar column groups associate columns with categories within a calendar.

## Syntax

```dax
INFO.CALENDARCOLUMNGROUPS ( [<Restriction name>, <Restriction value>], ... )
```

[!INCLUDE[parameters-for-info-dax-functions](includes/parameters-for-info-dax-functions.md)]

## Return value

A table with the following columns:

| Column | Description |
|---|---|
| ID | Unique identifier for the calendar column group |
| CalendarID | ID of the calendar this calendar column group belongs to |
| TimeUnit | The category associated with this column group (e.g. DayOfWeek) |
| ModifiedTime | When the calendar column group was last modified |

## Remarks

- Typically used in DAX queries to inspect and document model metadata.
- Permissions required depend on the host. Querying full metadata may require model admin permissions.

## Example

The following DAX query can be run in [DAX query view](/power-bi/transform-model/dax-query-view):

```dax
EVALUATE
	INFO.CALENDARCOLUMNGROUPS()
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
- [INFO.CALENDARCOLUMNREFERENCES](info-calendarcolumnreferences-function-dax.md)
- [INFO.COLUMNS](info-columns-function-dax.md)
- [INFO functions overview](info-functions-dax.md)
