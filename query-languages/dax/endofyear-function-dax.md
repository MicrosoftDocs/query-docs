---
description: "Learn more about: ENDOFYEAR"
title: "ENDOFYEAR function (DAX)"
---
# ENDOFYEAR

[!INCLUDE[applies-to-measures-columns-tables-visual-calculations-discouraged](includes/applies-to-measures-columns-tables-visual-calculations-discouraged.md)]

For date column input, returns the last date of year in the current context for the specified column of dates.
For calendar input, returns a table that contains all primary tagged columns for last date of year, in the current context.

## Syntax

```dax
ENDOFYEAR(<dates> or <calendar> [,<year_end_date>])
```

### Parameters

|Term|Definition|
|--------|--------------|
|`dates or calendar`|A column that contains dates or a calendar reference|
|`year_end_date`|(optional) A literal string with a date that defines the year-end date. The default is December 31.|

## Return value

For date column input, a table containing a single column and single row with a date value.
For calendar input, a table that contains all primary tagged columns for last date of year, in the current context.

## Remarks

- The `dates` argument can be any of the following:
  - A reference to a date/time column,
  - A table expression that returns a single column of date/time values,
  - A Boolean expression that defines a single-column table of date/time values.

- Constraints on Boolean expressions are described in the topic, [CALCULATE function](calculate-function-dax.md).

- The `year_end_date` parameter is a string literal of a date, in the same locale as the locale of the client where the workbook was created. The year portion of the date is ignored.

- [!INCLUDE [function-not-supported-in-directquery-mode](includes/function-not-supported-in-directquery-mode.md)]

## Example

The following sample formula creates a measure that returns the end of the fiscal year that ends on June 30, for the current context.

```dax
= ENDOFYEAR(DateTime[DateKey],"06/30/2004")
```

## Example for calendar based time intelligence

The following sample formula returns tagged primary columns that corresponds to end of year, for the fiscal calendar.

```dax
= ENDOFYEAR(FiscalCalendar)
```

## Related content

[Date and time functions](date-and-time-functions-dax.md)
[Time intelligence functions](time-intelligence-functions-dax.md)
[ENDOFWEEK function](endofweek-function-dax.md)
[ENDOFMONTH function](endofmonth-function-dax.md)
[ENDOFQUARTER function](endofquarter-function-dax.md)
