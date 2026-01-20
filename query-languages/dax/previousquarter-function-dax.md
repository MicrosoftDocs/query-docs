---
description: "Learn more about: PREVIOUSQUARTER"
title: "PREVIOUSQUARTER function (DAX)"
ms.topic: reference
---
# PREVIOUSQUARTER

[!INCLUDE[applies-to-measures-columns-tables-visual-calculations-discouraged](includes/applies-to-measures-columns-tables-visual-calculations-discouraged.md)]

For date column input, returns a table that contains a column of all dates from the previous quarter, based on the first date in the `dates` column, in the current context.

For calendar input, returns a table of all dates from the previous quarter, based on the first date in the current context. The table contains all primary tagged columns and all time related columns.

## Syntax

```
PREVIOUSQUARTER(<dates> or <calendar>)
```

### Parameters

|Term|Definition|
|--------|--------------|
|`dates or calendar`|A column that contains dates or a calendar reference|

## Return value

For date column input, a table containing a single column of date values.  
For calendar input, a table for previous quarter. The table contains all primary tagged columns and all time related columns.

## Remarks

- This function returns all dates from the previous quarter, using the first date in the input column. For example, if the first date in the `dates` argument refers to June 10, 2009,  this function returns all dates for the quarter January to March, 2009.

- The `dates` argument can be any of the following:
  - A reference to a date/time column.
  - A table expression that returns a single column of date/time values.
  - A Boolean expression that defines a single-column table of date/time values.

- Constraints on Boolean expressions are described in the topic, [CALCULATE](calculate-function-dax.md).

- [!INCLUDE [function-not-supported-in-directquery-mode](includes/function-not-supported-in-directquery-mode.md)]

## Example

The following sample formula creates a measure that calculates the 'previous quarter sales' for Internet sales.

```dax
= CALCULATE (
    SUM ( InternetSales_USD[SalesAmount_USD] ),
    PREVIOUSQUARTER ( 'DateTime'[DateKey] )
)
```

## Example for calendar

The following sample formula creates a measure that calculates the 'previous quarter sales' for Internet sales in terms of fiscal calendar.

```dax
= CALCULATE (
    SUM ( InternetSales_USD[SalesAmount_USD] ),
    PREVIOUSQUARTER ( FiscalCalendar )
)
```

## Related content

[Time intelligence functions](time-intelligence-functions-dax.md)
[Date and time functions](date-and-time-functions-dax.md)
[PREVIOUSDAY](previousday-function-dax.md)
[PREVIOUSWEEK](previousweek-function-dax.md)
[PREVIOUSMONTH](previousmonth-function-dax.md)
[PREVIOUSYEAR](previousyear-function-dax.md)
