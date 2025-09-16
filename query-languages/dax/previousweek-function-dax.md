---
description: "Learn more about: PREVIOUSWEEK"
title: "PREVIOUSWEEK function (DAX)"
---
# PREVIOUSWEEK

[!INCLUDE[applies-to-measures-columns-tables-visual-calculations-discouraged](includes/applies-to-measures-columns-tables-visual-calculations-discouraged.md)]

Returns a table of all dates from the previous week, based on the first date in the current context. The table contains all primary tagged columns and all time related columns.

> [!NOTE]
> Week functions only work with calendar based time intelligence. 

## Syntax

```dax
PREVIOUSWEEK(<calendar>)
```

### Parameters

|Term|Definition|
|--------|--------------|
|`calendar`|A calendar reference|

## Return value

A table that contains all primary tagged columns and all time related columns.

## Remarks

- Constraints on Boolean expressions are described in the topic, [CALCULATE function](calculate-function-dax.md).

- [!INCLUDE [function-not-supported-in-directquery-mode](includes/function-not-supported-in-directquery-mode.md)]


## Example for calendar based time intelligence

The following sample formula creates a measure that calculates the 'previous week sales' for Internet sales in terms of fiscal calendar.

```dax
= CALCULATE (
    SUM ( InternetSales_USD[SalesAmount_USD] ),
    PREVIOUSWEEK ( FiscalCalendar )
)
```

## Related content

[Time intelligence functions](time-intelligence-functions-dax.md)
[Date and time functions](date-and-time-functions-dax.md)
[PREVIOUSDAY function](previousday-function-dax.md)
[PREVIOUSMONTH function](previousmonth-function-dax.md)
[PREVIOUSQUARTER function](previousquarter-function-dax.md)
[PREVIOUSYEAR function](previousyear-function-dax.md)

