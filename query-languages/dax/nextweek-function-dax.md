---
description: "Learn more about: NEXTWEEK"
title: "NEXTWEEK function (DAX)"
---
# NEXTWEEK

[!INCLUDE[applies-to-measures-columns-tables-visual-calculations-discouraged](includes/applies-to-measures-columns-tables-visual-calculations-discouraged.md)]

> [!NOTE]
> Week functions only work with calendar based time intelligence. 

Returns all primary tagged columns of all dates from the next week, based on the last date in the current context.


## Syntax

```
NEXTWEEK(<calendar>)
```

### Parameters

|Term|Definition|
|--------|--------------|
|`calendar`|A calendar reference|

## Return value

A table that contains primary tagged columns for next week, in the current context.

## Remarks

- Constraints on Boolean expressions are described in the topic, [CALCULATE function](calculate-function-dax.md).

- [!INCLUDE [function-not-supported-in-directquery-mode](includes/function-not-supported-in-directquery-mode.md)]

## Example

The following sample formula creates a measure that calculates the 'next week sales' for Internet sales.

```dax
=
CALCULATE (
    SUM ( InternetSales_USD[SalesAmount_USD] ),
    NEXTWEEK ( FiscalCalendar )
)
```

## Related content

[Time intelligence functions](time-intelligence-functions-dax.md)
[Date and time functions](date-and-time-functions-dax.md)
[NEXTDAY function](nextday-function-dax.md)
[NEXTMONTH function](nextmonth-function-dax.md)
[NEXTQUARTER function](nextquarter-function-dax.md)
[NEXTYEAR function](nextyear-function-dax.md)
