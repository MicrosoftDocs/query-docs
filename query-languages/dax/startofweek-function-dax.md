---
description: "Learn more about: STARTOFWEEK"
title: "STARTOFWEEK function (DAX)"
---
# STARTOFWEEK

[!INCLUDE[applies-to-measures-columns-tables-visual-calculations-discouraged](includes/applies-to-measures-columns-tables-visual-calculations-discouraged.md)]
For calendar input, returns a table that contains all the tagged columns for first date of week, in the current context.
Note: week functions only work with calendar based time intelligence.

## Syntax

```dax
STARTOFWEEK(<calendar>)
```

### Parameters

|Term|Definition|
|--------|--------------|
|`calendar`|A calendar reference|

## Return value

For calendar input, a table that contains all the tagged column for first date of week, in the current context.

## Remarks

- Constraints on Boolean expressions are described in the topic, [CALCULATE](calculate-function-dax.md).

- [!INCLUDE [function-not-supported-in-directquery-mode](includes/function-not-supported-in-directquery-mode.md)]


## Example for calendar based time intelligence

The following sample formula returns primary tagged columns that corresponds to the start of the week, for the fiscal calendar.

```dax
= STARTOFWEEK(FiscalCalendar)
```

## Related content

[Date and time functions](date-and-time-functions-dax.md)
[Time intelligence functions](time-intelligence-functions-dax.md)
[STARTOFYEAR](startofyear-function-dax.md)
[STARTOFQUARTER](startofquarter-function-dax.md)
[STARTOFMONTH](startofmonth-function-dax.md)
