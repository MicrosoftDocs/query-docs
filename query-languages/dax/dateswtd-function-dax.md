---
description: "Learn more about: DATESWTD"
title: "DATESWTD function (DAX)"
---
# DATESWTD

[!INCLUDE[applies-to-measures-columns-tables-visual-calculations-discouraged](includes/applies-to-measures-columns-tables-visual-calculations-discouraged.md)]

> [!NOTE]
> Week functions only work with calendar based time intelligence. 

For calendar input, returns a table for week to date, in the current context. The table contains all primary tagged columns and all time related columns.

## Syntax

```
DATESWTD(<calendar>)
```

### Parameters

|Term|Definition|
|--------|--------------|
|`calendar`|A calendar reference.|

## Return value

A table containing all primary tagged and time-related columns

## Remarks

- [!INCLUDE [function-not-supported-in-directquery-mode](includes/function-not-supported-in-directquery-mode.md)]


## Example for calendar based time intelligence

The following sample formula creates a measure that calculates the 'Week To Date Total' for Internet sales uing fiscal calendar.

```dax
= CALCULATE (
    SUM ( InternetSales_USD[SalesAmount_USD] ),
    DATESWTD ( FiscalCalendar )
)
```

## Related content

[Time intelligence functions](time-intelligence-functions-dax.md)
[Date and time functions](date-and-time-functions-dax.md)
[DATESYTD function](datesytd-function-dax.md)
[DATESQTD function](datesqtd-function-dax.md)
[DATESMTD function](datesmtd-function-dax.md)
