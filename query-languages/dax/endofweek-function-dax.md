---
description: "Learn more about: ENDOFWEEK"
title: "ENDOFWEEK function (DAX)"
---
# ENDOFWEEK

[!INCLUDE[applies-to-measures-columns-tables-visual-calculations-discouraged](includes/applies-to-measures-columns-tables-visual-calculations-discouraged.md)]

For calendar input, returns all primary tagged columns for last date of week, in the current context.
Note: week function only works with calendar based time intelligence.

## Syntax

```dax
ENDOFWEEK(<calendar>)
```

### Parameters

|Term|Definition|
|--------|--------------|
|`calendar`|A calendar reference|

## Return value

For calendar input, a table that contains all primary tagged columns for end date of week, in the current context.

## Remarks

- Constraints on Boolean expressions are described in the topic, [CALCULATE function](calculate-function-dax.md).

- [!INCLUDE [function-not-supported-in-directquery-mode](includes/function-not-supported-in-directquery-mode.md)]

## Example for calendar based time intelligence

The following sample formula returns tagged primary columns that corresponds to the end of the month, for the fiscal calendar.

```dax
= ENDOFWEEK(FiscalCalendar)
```

## Related content

[Date and time functions](date-and-time-functions-dax.md)
[Time intelligence functions](time-intelligence-functions-dax.md)
[ENDOFYEAR function](endofyear-function-dax.md)
[ENDOFQUARTER function](endofquarter-function-dax.md)
[ENDOFMONTH function](endofmonth-function-dax.md)

