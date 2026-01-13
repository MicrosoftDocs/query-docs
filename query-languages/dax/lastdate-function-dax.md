---
description: "Learn more about: LASTDATE"
title: "LASTDATE function (DAX)"
ms.topic: reference
---
# LASTDATE

[!INCLUDE[applies-to-measures-columns-tables-visual-calculations-discouraged](includes/applies-to-measures-columns-tables-visual-calculations-discouraged.md)]

For date column input, returns the last date in the current context for the specified column of dates.  

For calendar input, returns the last date based on the calendar.

## Syntax

```
LASTDATE(<dates> or <calendar>)
```

### Parameters

|Term|Definition|
|--------|--------------|
|`dates or calendar`|A column that contains dates or a calendar reference|

## Return value

For date column input, a table containing a single column and single row with a date value.

For calendar input, a single row table that contains all primary tagged columns and all time related columns.

## Remarks

- The `dates` argument can be any of the following: 
  - A reference to a date/time column,
  - A table expression that returns a single column of date/time values,
  - A Boolean expression that defines a single-column table of date/time values.

- Constraints on Boolean expressions are described in the topic, [CALCULATE function](calculate-function-dax.md).

- When the current context is a single date, the date returned by the FIRSTDATE and LASTDATE functions will be equal.

- For date column input, the Return value is a table that contains a single column and single value. Therefore, this function can be used as an argument to any function that requires a table in its arguments. Also, the returned value can be used whenever a date value is required.

- [!INCLUDE [function-not-supported-in-directquery-mode](includes/function-not-supported-in-directquery-mode.md)]

## Example

The following sample formula creates a measure that obtains the last date, for the current context, when a sale was made in the Internet sales channel.

```dax
= LASTDATE('InternetSales_USD'[SaleDateKey])
```

## Example for calendar based time intelligence

The following sample formula creates a measure that obtains the last date, for the current context, when a sale was made in the Internet sales channel.

```dax
= LASTDATE(FiscalCalendar)
```

## Related content

[Date and time functions](date-and-time-functions-dax.md)
[Time intelligence functions](time-intelligence-functions-dax.md)
[FIRSTDATE function](firstdate-function-dax.md)
[LASTNONBLANK function](lastnonblank-function-dax.md)
