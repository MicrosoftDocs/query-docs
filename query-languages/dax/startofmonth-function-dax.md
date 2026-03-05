---
description: "Learn more about: STARTOFMONTH"
title: "STARTOFMONTH function (DAX)"
ms.topic: reference
---
# STARTOFMONTH

[!INCLUDE[applies-to-measures-columns-tables-visual-calculations-discouraged](includes/applies-to-measures-columns-tables-visual-calculations-discouraged.md)]
For date column input, returns the first date of month in the current context for the specified column of dates.  
For calendar input, returns a table for first date of month, in the current context. A table that contains all primary tagged columns and all time related columns.

## Syntax

```
STARTOFMONTH(<dates> or <calendar>)
```

### Parameters

|Term|Definition|
|--------|--------------|
|`dates or calendar`|A column that contains dates or a calendar reference|

## Return value

For date column input, a table containing a single column and single row with a date value.  
For calendar input, a table that contains all primary tagged columns and all time related columns.

## Remarks

- The `dates` argument can be any of the following:
  - A reference to a date/time column.
  - A table expression that returns a single column of date/time values.
  - A Boolean expression that defines a single-column table of date/time values.

- Constraints on Boolean expressions are described in the topic, [CALCULATE](calculate-function-dax.md).

- [!INCLUDE [function-not-supported-in-directquery-mode](includes/function-not-supported-in-directquery-mode.md)]

## Example

The following sample formula creates a measure that returns the start of the month, for the current context.

```dax
= STARTOFMONTH(DateTime[DateKey])
```

## Example for calendar based time intelligence

The following sample formula creates a table that returns tagged primary columns that corresponds to the start of the month, for the fiscal calendar.

```dax
= STARTOFMONTH(FiscalCalendar)
```

## Related content

- [Date and time functions](date-and-time-functions-dax.md)
- [Time intelligence functions](time-intelligence-functions-dax.md)
- [STARTOFYEAR](startofyear-function-dax.md)
- [STARTOFQUARTER](startofquarter-function-dax.md)
- [STARTOFWEEK](startofweek-function-dax.md)
