---
description: "Learn more about: DATESYTD"
title: "DATESYTD function (DAX)"
ms.topic: reference
---
# DATESYTD

[!INCLUDE[applies-to-measures-columns-tables-visual-calculations-discouraged](includes/applies-to-measures-columns-tables-visual-calculations-discouraged.md)]

For date column input, returns a table that contains a column of the dates for year to date, in the current context.  
For calendar input, returns a table for year to date, in the current context. The table contains all primary tagged columns and all time related columns.

## Syntax

```
DATESYTD(<dates> or <calendar> [,<year_end_date>])
```

### Parameters

|Term|Definition|
|--------|--------------|
|`dates or calendar`|A column that contains dates or a calendar reference.|
|`year_end_date`|(optional) A literal string with a date that defines the year-end date. The default is December 31. This parameter is permitted only when the date column syntax is used.|

## Return value

For date column input, a table containing a single column of date values.  
For calendar input, a table that contains all primary tagged columns and all time related columns.

## Remarks

The `dates` argument can be any of the following:

- A reference to a date/time column,

- A table expression that returns a single column of date/time values,

- A Boolean expression that defines a single-column table of date/time values.

    > [!NOTE]
    > Constraints on Boolean expressions are described in the topic, [CALCULATE function](calculate-function-dax.md).

- The `year_end_date` parameter is a string literal of a date, in the same locale as the locale of the client where the workbook was created. The year portion of the date is ignored.  Depending on locale, the format might be something like "m-dd" or "dd-m".

- The `year_end_date` parameter is permitted only when the date column syntax is used.

- [!INCLUDE [function-not-supported-in-directquery-mode](includes/function-not-supported-in-directquery-mode.md)]

## Example

The following sample formula creates a measure that calculates the 'Running Total' for Internet sales.

```dax
= CALCULATE (
    SUM ( InternetSales_USD[SalesAmount_USD] ),
    DATESYTD ( DateTime[DateKey] )
)
```

The following sample formula creates a measure that calculates the 'Fiscal Year Running Total' for Internet sales, using a US Locale for the Date format.

```dax
= CALCULATE(
    SUM(InternetSales_USD[SalesAmount_USD]), 
    DATESYTD(DateTime[DateKey],
        "6-30"
        )
)
```

## Example for calendar based time intelligence

The following sample formula creates a measure that calculates the 'Running Total' for Internet sales uing fiscal calendar.

```dax
= CALCULATE (
    SUM ( InternetSales_USD[SalesAmount_USD] ),
    DATESYTD ( FiscalCalendar )
)
```


## Related content

[Time intelligence functions](time-intelligence-functions-dax.md)
[Date and time functions](date-and-time-functions-dax.md)
[DATESWTD function](dateswtd-function-dax.md)
[DATESMTD function](datesmtd-function-dax.md)
[DATESQTD function](datesqtd-function-dax.md)
