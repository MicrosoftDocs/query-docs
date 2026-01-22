---
description: "Learn more about: DATESMTD"
title: "DATESMTD function (DAX)"
ms.topic: reference
---
# DATESMTD

[!INCLUDE[applies-to-measures-columns-tables-visual-calculations-discouraged](includes/applies-to-measures-columns-tables-visual-calculations-discouraged.md)]

For date column input, returns a table that contains a column of the dates for the month to date, in the current context.  
For calendar input, returns a table for the month to date, in the current context. The table contains all primary tagged columns and all time related columns.

## Syntax

```
DATESMTD(<dates> or <calendar>)
```

### Parameters

|Term|Definition|
|--------|--------------|
|`dates or calendar`|A column that contains dates or a calendar reference.|

## Return value

For date column input, a table containing a single column of date values.  
For calendar input, a table that contains all primary tagged columns and all time related columns.

## Remarks

The `dates` argument can be any of the following:

- A reference to a date/time column.

- A table expression that returns a single column of date/time values.

- A Boolean expression that defines a single-column table of date/time values.

    > [!NOTE]
    > Constraints on Boolean expressions are described in the topic, [CALCULATE function](calculate-function-dax.md).

- [!INCLUDE [function-not-supported-in-directquery-mode](includes/function-not-supported-in-directquery-mode.md)]

## Example

The following sample formula creates a measure that calculates the 'Month To Date Total' for Internet Sales.

```dax
= CALCULATE (
    SUM ( InternetSales_USD[SalesAmount_USD] ),
    DATESMTD ( DateTime[DateKey] )
)
```

## Example for calendar based time intelligence

The following sample formula creates a measure that calculates the 'Monthly Running Total' for Internet sales uing fiscal calendar.

```dax
=
CALCULATE (
    SUM ( InternetSales_USD[SalesAmount_USD] ),
    DATESMTD ( FiscalCalendar )
)
```

## Related content

- [Time intelligence functions](time-intelligence-functions-dax.md)
- [Date and time functions](date-and-time-functions-dax.md)
- [DATESWTD function](dateswtd-function-dax.md)
- [DATESQTD function](datesqtd-function-dax.md)
- [DATESYTD function](datesytd-function-dax.md)
