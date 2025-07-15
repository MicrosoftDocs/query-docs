---
description: "Learn more about: PREVIOUSYEAR"
title: "PREVIOUSYEAR function (DAX)"
---
# PREVIOUSYEAR

[!INCLUDE[applies-to-measures-columns-tables-visual-calculations-discouraged](includes/applies-to-measures-columns-tables-visual-calculations-discouraged.md)]

For date column input, Returns a table that contains a column of all dates from the previous year, given the last date in the `dates` column, in the current context.

For calendar input, returns primary tagged columns of all dates from the previous year, based on the first date in the current context.

## Syntax

```dax
PREVIOUSYEAR(<dates> or <calendar>[,<year_end_date>])
```

### Parameters

|Term|Definition|
|--------|--------------|
|`dates or calendar`|A column that contains dates or a calendar reference|
|`year_end_date`|(optional) A literal string with a date that defines the year-end date. The default is December 31.|

## Return value

For date column input, a table containing a single column of date values.
For calendar input, a table that contains primary tagged columns for previous year, in the current context.

## Remarks

- This function returns all dates from the previous year given the latest date in the input parameter. For example, if the latest date in the `dates` argument refers to the year 2009, then this function returns all dates for the year of 2008, up to the specified `year_end_date`.

- The `dates` argument can be any of the following:
  - A reference to a date/time column.
  - A table expression that returns a single column of date/time values.
  - A Boolean expression that defines a single-column table of date/time values.

- Constraints on Boolean expressions are described in the topic, [CALCULATE](calculate-function-dax.md).

- The `year_end_date` parameter is a string literal of a date, in the same locale as the locale of the client where the workbook was created. The year portion of the date is ignored.

- [!INCLUDE [function-not-supported-in-directquery-mode](includes/function-not-supported-in-directquery-mode.md)]

## Example

The following sample formula creates a measure that calculates the previous year sales for Internet sales.

```dax
= CALCULATE(SUM(InternetSales_USD[SalesAmount_USD]), PREVIOUSYEAR('DateTime'[DateKey]))
```

## Example for calendar

The following sample formula creates a measure that calculates the 'previous quarter sales' for Internet sales in terms of fiscal calendar.

```dax
= CALCULATE (
    SUM ( InternetSales_USD[SalesAmount_USD] ),
    PREVIOUSYEAR ( FiscalCalendar )
)
```

## Related content

[Time intelligence functions](time-intelligence-functions-dax.md)
[Date and time functions](date-and-time-functions-dax.md)
[PREVIOUSMONTH](previousmonth-function-dax.md)
[PREVIOUSDAY](previousday-function-dax.md)
[PREVIOUSQUARTER](previousquarter-function-dax.md)
