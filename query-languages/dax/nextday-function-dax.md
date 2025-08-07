---
description: "Learn more about: NEXTDAY"
title: "NEXTDAY function (DAX)"
---
# NEXTDAY

[!INCLUDE[applies-to-measures-columns-tables-visual-calculations-discouraged](includes/applies-to-measures-columns-tables-visual-calculations-discouraged.md)]

For date column input, returns a table that contains a column of all dates from the next day, based on the last date specified in the `dates` column in the current context.    

For calendar input, returns returns the next day of the last date in the current context, based on the calendar. The output will include all primary tagged columns for that day.


## Syntax

```
NEXTDAY(<dates> or <calendar>)
```

### Parameters

|Term|Definition|
|--------|--------------|
|`dates or calendar`|A column that contains dates or a calendar reference|

## Return value

For date column input, a table containing a single column of date values.  
For calendar input, a table that contains primary tagged columns for next day, in the current context.

## Remarks

- For date column input, this function returns all dates from the next day to the last date in the input parameter. For example, if the last date in the `dates` argument refers to June 10, 2009; then this function returns all dates equal to June 11, 2009.

- The `dates` argument can be any of the following:
  - A reference to a date/time column.
  - A table expression that returns a single column of date/time values.
  - A Boolean expression that defines a single-column table of date/time values.

- Constraints on Boolean expressions are described in the topic, [CALCULATE function](calculate-function-dax.md).

- [!INCLUDE [function-not-supported-in-directquery-mode](includes/function-not-supported-in-directquery-mode.md)] 

## Example

The following sample formula creates a measure that calculates the 'next day sales' of Internet sales.

```dax
= CALCULATE (
    SUM ( InternetSales_USD[SalesAmount_USD] ),
    NEXTDAY ( 'DateTime'[DateKey] )
)
```

## Example for calendar based time intelligence

The following sample formula creates a measure that calculates the 'next day sales' of Internet sales for a fiscal calendar.

```dax
=
CALCULATE (
    SUM ( InternetSales_USD[SalesAmount_USD] ),
    NEXTDAY ( FiscalCalendar )
)
```

## Related content

[Time intelligence functions](time-intelligence-functions-dax.md)
[Date and time functions](date-and-time-functions-dax.md)
[NEXTWEEK function](nextweek-function-dax.md)
[NEXTMONTH function](nextmonth-function-dax.md)
[NEXTQUARTER function](nextquarter-function-dax.md)
[NEXTYEAR function](nextyear-function-dax.md)
