---
description: "Learn more about: DATESQTD"
title: "DATESQTD function (DAX)"
---
# DATESQTD

[!INCLUDE[applies-to-measures-columns-tables-visual-calculations-discouraged](includes/applies-to-measures-columns-tables-visual-calculations-discouraged.md)]

For date column input, returns a table that contains a column of the dates for quarter to date, in the current context.
For calendar input, returns a table that contains all the tagged column for quarter to date, in the current context.

## Syntax

```dax
DATESQTD(<dates|calendar>)
```

### Parameters

|Term|Definition|
|--------|--------------|
|`dates/calendar`|A column that contains dates or a calendar reference.|

## Return value

For date column input, a table containing a single column of date values.
For calendar input, a table that contains all the tagged column for quarter to date, in the current context.

## Remarks

The `dates` argument can be any of the following:

- A reference to a date/time column.

- A table expression that returns a single column of date/time values.

- A Boolean expression that defines a single-column table of date/time values.

    > [!NOTE]
    > Constraints on Boolean expressions are described in the topic, [CALCULATE function](calculate-function-dax.md).

- [!INCLUDE [function-not-supported-in-directquery-mode](includes/function-not-supported-in-directquery-mode.md)]

## Example

The following sample formula creates a measure that calculates the 'Quarterly Running Total' of Internet Sales.

```dax
= CALCULATE(SUM(InternetSales_USD[SalesAmount_USD]), DATESQTD(DateTime[DateKey]))
```

## Example for calendar based time intelligence

The following sample formula creates a measure that calculates the 'Quarterly Running Total' for Internet sales uing fiscal calendar.

```dax
= CALCULATE(SUM(InternetSales_USD[SalesAmount_USD]), DATESQTD(FiscalCalendar))
```

## Related content

[Time intelligence functions](time-intelligence-functions-dax.md)
[Date and time functions](date-and-time-functions-dax.md)
[DATESYTD function](datesytd-function-dax.md)
[DATESQTD function](datesqtd-function-dax.md)
[DATESMTD function](datesmtd-function-dax.md)
