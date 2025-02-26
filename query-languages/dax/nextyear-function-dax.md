---
description: "Learn more about: NEXTYEAR"
title: "NEXTYEAR function (DAX)"
---
# NEXTYEAR

[!INCLUDE[applies-to-measures-columns-tables-visual-calculations-discouraged](includes/applies-to-measures-columns-tables-visual-calculations-discouraged.md)]

Returns a table that contains a column of all dates in the next year, based on the first date in the `dates` column, in the current context.

## Syntax

```dax
NEXTYEAR(<dates>[,<year_end_date>])
```

### Parameters

|Term|Definition|
|--------|--------------|
|`dates`|A column containing dates.|
|`year_end_date`|(optional) A literal string with a date that defines the year-end date. The default is December 31.|

## Return value

A table containing a single column of date values.

## Remarks

- This function returns all dates in the next year, based on the first date in the input column. For example, if the first date in the `dates` column refers to the year 2007, this function returns all dates for the year 2008.

- The `dates` argument can be any of the following:
  - A reference to a date/time column.
  - A table expression that returns a single column of date/time values.
  - A Boolean expression that defines a single-column table of date/time values.

- Constraints on Boolean expressions are described in the topic, [CALCULATE function](calculate-function-dax.md).

- The `year_end_date` parameter is a string literal of a date, in the same locale as the locale of the client where the workbook was created. The year portion of the date is ignored.

- [!INCLUDE [function-not-supported-in-directquery-mode](includes/function-not-supported-in-directquery-mode.md)]

## Example

The following sample formula creates a measure that calculates the 'next year sales' for Internet sales.

```dax
= CALCULATE(SUM(InternetSales_USD[SalesAmount_USD]), NEXTYEAR('DateTime'[DateKey]))
```

## Related content

[Time intelligence functions](time-intelligence-functions-dax.md)
[Date and time functions](date-and-time-functions-dax.md)
[NEXTDAY function](nextday-function-dax.md)
[NEXTQUARTER function](nextquarter-function-dax.md)
[NEXTMONTH function](nextmonth-function-dax.md)
