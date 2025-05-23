---
description: "Learn more about: SAMEPERIODLASTYEAR"
title: "SAMEPERIODLASTYEAR function (DAX)"
---
# SAMEPERIODLASTYEAR

[!INCLUDE[applies-to-measures-columns-tables-visual-calculations-discouraged](includes/applies-to-measures-columns-tables-visual-calculations-discouraged.md)]

Returns a table that contains a column of dates shifted one year back in time from the dates in the specified `dates` column, in the current context.

## Syntax

```dax
SAMEPERIODLASTYEAR(<dates>)
```

### Parameters

|Term|Definition|
|--------|--------------|
|`dates`|A column containing dates.|

## Return value

A single-column table of date values.

## Remarks

- The `dates` argument can be any of the following:
  - A reference to a date/time column,
  - A table expression that returns a single column of date/time values,
  - A Boolean expression that defines a single-column table of date/time values.

- Constraints on Boolean expressions are described in the topic, [CALCULATE](calculate-function-dax.md).

- The dates returned are the same as the dates returned by this equivalent formula: `DATEADD(dates, -1, year)`

- [!INCLUDE [function-not-supported-in-directquery-mode](includes/function-not-supported-in-directquery-mode.md)]

## Example

The following sample formula creates a measure that calculates the previous year sales of Reseller sales.

```dax
= CALCULATE(SUM(ResellerSales_USD[SalesAmount_USD]), SAMEPERIODLASTYEAR(DateTime[DateKey]))
```

## Special behavior

When the selection includes last two days of month, SAMEPERIODLASTYEAR will use "extension" semantics and will include the days till the end of month. For example, when Feb 27 and 28 of 2009 are included in the selection, SAMEPERIODLASTYEAR will return Feb 27 to 29 of 2008.

This behavior only happens when last two days of month are included in the selection. If only Feb 27 is selected, it will go to Feb 27.

```dax
= SAMEPERIODLASTYEAR(DateTime[DateKey])
```

## Related content

[Time intelligence functions](time-intelligence-functions-dax.md)
[Date and time functions ](date-and-time-functions-dax.md)
[PREVIOUSYEAR](previousyear-function-dax.md)
[PARALLELPERIOD](parallelperiod-function-dax.md)

