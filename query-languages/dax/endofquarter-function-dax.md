---
description: "Learn more about: ENDOFQUARTER"
title: "ENDOFQUARTER function (DAX)"
---
# ENDOFQUARTER

[!INCLUDE[applies-to-measures-columns-tables-visual-calculations-discouraged](includes/applies-to-measures-columns-tables-visual-calculations-discouraged.md)]

For date column input, returns the last date of month in the current context for the specified column of dates.
For calendar input, returns a table that contains all primary tagged columns for last date of month, in the current context.

## Syntax

```dax
ENDOFQUARTER(<dates|calendar>)
```

### Parameters

|Term|Definition|
|--------|--------------| 
|`dates/calendar`|A column that contains dates or a calendar reference|

## Return value

For date column input, a table containing a single column and single row with a date value.
For calendar input, a table that contains all primary tagged columns for last date of quarter, in the current context.

## Remarks

- The `dates` argument can be any of the following:
  - A reference to a date/time column,
  - A table expression that returns a single column of date/time values,
  - A Boolean expression that defines a single-column table of date/time values.

- Constraints on Boolean expressions are described in the topic, [CALCULATE function](calculate-function-dax.md).

- The `year_end_date` parameter must not be specified when a calendar is used.

- [!INCLUDE [function-not-supported-in-directquery-mode](includes/function-not-supported-in-directquery-mode.md)]

## Example

The following sample formula creates a measure that returns the end of the quarter, for the current context.

```dax
= ENDOFQUARTER(DateTime[DateKey])
```

## Example for calendar based time intelligence

The following sample formula returns tagged primary columns that corresponds to end of quarter, for the fiscal calendar.

```dax
= ENDOFQUARTER(FiscalCalendar)
```

## Related content

[Date and time functions](date-and-time-functions-dax.md)
[Time intelligence functions](time-intelligence-functions-dax.md)
[ENDOFYEAR function](endofyear-function-dax.md)
[ENDOFMONTH function](endofmonth-function-dax.md)
[ENDOFWEEK function](endofweek-function-dax.md)
