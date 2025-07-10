---
description: "Learn more about: STARTOFWEEK"
title: "STARTOFWEEK function (DAX)"
---
# STARTOFMONTH

[!INCLUDE[applies-to-measures-columns-tables-visual-calculations-discouraged](includes/applies-to-measures-columns-tables-visual-calculations-discouraged.md)]
For date column input, returns the first date of week in the current context for the specified column of dates.
For calendar input, returns a table that contains all the tagged columns for first date of week, in the current context.

## Syntax

```dax
STARTOFWEEK(<dates|calendar>)
```

### Parameters

|Term|Definition|
|--------|--------------|
|`dates/calendar`|A column that contains dates or a calendar reference|

## Return value

For date column input, a table containing a single column and single row with a date value.
For calendar input, a table that contains all the tagged column for first date of week, in the current context.

## Remarks

- The `dates` argument can be any of the following:
  - A reference to a date/time column.
  - A table expression that returns a single column of date/time values.
  - A Boolean expression that defines a single-column table of date/time values.

- Constraints on Boolean expressions are described in the topic, [CALCULATE](calculate-function-dax.md).

- In addition to `dates`, a calendar reference could also be used at first argument.

- [!INCLUDE [function-not-supported-in-directquery-mode](includes/function-not-supported-in-directquery-mode.md)]

## Example

The following sample formula creates a measure that returns the start of the week, for the current context.

```dax
= STARTOFWEEK(DateTime[DateKey])
```

## Example for calendar based time intelligence

The following sample formula creates a table that returns tagged columns that corresponds to the start of the week, for the fiscal calendar.

```dax
= STARTOFWEEK(FiscalCalendar)
```

## Related content

[Date and time functions](date-and-time-functions-dax.md)
[Time intelligence functions](time-intelligence-functions-dax.md)
[STARTOFYEAR](startofyear-function-dax.md)
[STARTOFQUARTER](startofquarter-function-dax.md)
[STARTOFMONTH](startofmonth-function-dax.md)
