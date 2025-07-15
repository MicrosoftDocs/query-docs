---
description: "Learn more about: PARALLELPERIOD"
title: "PARALLELPERIOD function (DAX)"
---
# PARALLELPERIOD

[!INCLUDE[applies-to-measures-columns-tables-visual-calculations-discouraged](includes/applies-to-measures-columns-tables-visual-calculations-discouraged.md)]

For date column input, returns a table that contains a column of dates that represents a period parallel to the dates in the specified `dates` column, in the current context, with the dates shifted a number of intervals either forward in time or back in time.

For calendar input, returns a table that contains all primary tagged columns that represent a period parallel to the dates in the specified `dates` column, in the current context, with the dates shifted a number of intervals either forward in time or back in time.

## Syntax

```dax
PARALLELPERIOD(<dates> or <calendar>,<number_of_intervals>,<interval>)
```

### Parameters

|Term|Definition|
|--------|--------------|
|`dates or calendar`|A column that contains dates or a calendar reference|
|`number_of_intervals`|An integer that specifies the number of intervals to add to or subtract from the dates.|
|`interval`|The interval by which to shift the dates. The value for interval can be one of the following: `year`, `quarter`, `month`.|

## Return value

For date column input, a table containing a single column of date values.
For calendar input, a table that contains all the tagged column for the year to date, in the current context.

## Remarks

- For date column input, this function takes the current set of dates in the column specified by `dates`, shifts the first date and the last date the specified number of intervals, and then returns all contiguous dates between the two shifted dates. If the interval is a partial range of month, quarter, or year then any partial months in the result are also filled out to complete the entire interval.

- The `dates` argument can be any of the following:
  - A reference to a date/time column,
  - A table expression that returns a single column of date/time values,
  - A Boolean expression that defines a single-column table of date/time values.

- Constraints on Boolean expressions are described in the topic, [CALCULATE function](calculate-function-dax.md).

- If the number specified for `number_of_intervals` is positive, the dates in `dates` are moved forward in time; if the number is negative, the dates in `dates` are shifted back in time.

- The `interval` parameter is an enumeration, not a set of strings; therefore values should not be enclosed in quotation marks. Also, the values: `year`, `quarter`, `month` should be spelled in full when using them.

- The result table includes only dates that appear in the values of the underlying table column.

- The PARALLELPERIOD function is similar to the DATEADD function except that PARALLELPERIOD always returns full periods at the given granularity level instead of the partial periods that DATEADD returns. For example, if you have a selection of dates that starts at June 10 and finishes at June 21 of the same year, and you want to shift that selection forward by one month then the PARALLELPERIOD function will return all dates from the next month (July 1 to July 31); however, if DATEADD is used instead, then the result will include only dates from July 10 to July 21.

- [!INCLUDE [function-not-supported-in-directquery-mode](includes/function-not-supported-in-directquery-mode.md)]

## Example

The following sample formula creates a measure that calculates the previous year sales for Internet sales.

```dax
= CALCULATE(SUM(InternetSales_USD[SalesAmount_USD]), PARALLELPERIOD(DateTime[DateKey],-1,year))
```

## Example for calendar based time intelligence

The following sample formula creates a measure that calculates the previous year sales for Internet sales using fiscal calendar.

```dax
=
CALCULATE (
    SUM ( InternetSales_USD[SalesAmount_USD] ),
    PARALLELPERIOD ( FiscalCalendar, -1, YEAR )
)
```

## Related content

[Time intelligence functions](time-intelligence-functions-dax.md)
[Date and time functions](date-and-time-functions-dax.md)
[DATEADD function](dateadd-function-dax.md)
