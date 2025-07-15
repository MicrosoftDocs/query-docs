---
description: "Learn more about: NEXTWEEK"
title: "NEXTWEEK function (DAX)"
---
# NEXTWEEK

[!INCLUDE[applies-to-measures-columns-tables-visual-calculations-discouraged](includes/applies-to-measures-columns-tables-visual-calculations-discouraged.md)]

For calendar input, returns primary tagged columns of all dates from the next week, based on the first date in the current context.

Note: weeks function only work with calendar based time intelligence.

## Syntax

```dax
NEXTWEEK(<calendar>)
```

### Parameters

|Term|Definition|
|--------|--------------|
|`calendar`|A calendar reference|

## Return value

For calendar input, a table that contains primary tagged columns for next week, in the current context.

## Remarks

- This function returns primary tagged columns related to all dates from the next month to the first date in the input parameter. For example, if the first date in the `dates` argument refers to June 10, 2009; then this function returns all dates for the next week of June 10, 2009.

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
[NEXTMONTH function](nextday-function-dax.md)
[NEXTQUARTER function](nextquarter-function-dax.md)
[NEXTYEAR function](nextyear-function-dax.md)
