---
description: "Learn more about: STARTOFYEAR"
title: "STARTOFYEAR function (DAX)"
ms.topic: reference
---
# STARTOFYEAR

[!INCLUDE[applies-to-measures-columns-tables-visual-calculations-discouraged](includes/applies-to-measures-columns-tables-visual-calculations-discouraged.md)]

For date column input, returns the first date of year in the current context for the specified column of dates.  
For calendar input, returns a table for first date of year, in the current context. The table contains all primary tagged columns and all time related columns.

## Syntax

```
STARTOFYEAR(<dates> or <calendar>)
```

### Parameters

|Term|Definition|
|--------|--------------|
|`dates or calendar`|A column that contains dates or a calendar reference.|
|`YearEndDate`|(Optional) A year end date value. Only applies for date column input.|

## Return value

For date column input, a table containing a single column and single row with a date value.  
For calendar input, a table for first date of year, in the current context. The table contains all primary tagged columns and all time related columns.

## Remarks

- The `dates` argument can be any of the following:
  - A reference to a date/time column.
  - A table expression that returns a single column of date/time values.
  - A Boolean expression that defines a single-column table of date/time values.

- Constraints on Boolean expressions are described in the topic, [CALCULATE](calculate-function-dax.md).

- The `year_end_date` parameter must not be specified when a calendar is used.

- [!INCLUDE [function-not-supported-in-directquery-mode](includes/function-not-supported-in-directquery-mode.md)]

## Example

The following sample formula creates a measure that returns the start of the year, for the current context.

```dax
= STARTOFYEAR(DateTime[DateKey])
```

## Example for calendar based time intelligence

The following sample formula creates a table that returns tagged columns that corresponds to the start of the year, for the fiscal calendar.

```dax
= STARTOFYEAR(FiscalCalendar)
```

## Related content

- [Date and time functions](date-and-time-functions-dax.md)
- [Time intelligence functions](time-intelligence-functions-dax.md)
- [STARTOFQUARTER](startofquarter-function-dax.md)
- [STARTOFMONTH](startofmonth-function-dax.md)
- [STARTOFWEEK](startofweek-function-dax.md)
