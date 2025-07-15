---
description: "Learn more about: TOTALWTD"
title: "TOTALWTD function (DAX)"
---
# TOTALWTD

[!INCLUDE[applies-to-measures-columns-tables-visual-calculations-discouraged](includes/applies-to-measures-columns-tables-visual-calculations-discouraged.md)]

Evaluates the value of the `expression` for the week to date, in the current context.
Note: weeks function only work with calendar based time intelligence.

## Syntax

```
TOTALWTD(<expression>,<calendar>[,<filter>])
```

### Parameters

|Parameter|Definition|
|-------------|--------------|
|`expression`|An expression that returns a scalar value.|
|`calendar`|A calendar reference.|
|`filter`|(optional) An expression that specifies a filter to apply to the current context.|

## Return value

A scalar value that represents the `expression` evaluated for the dates in the current week-to-date, given the dates in `dates` or `calendar`.

## Remarks

- Constraints on Boolean expressions are described in the topic, [CALCULATE](calculate-function-dax.md).

- The `filter` expression has restrictions described in the topic, [CALCULATE](calculate-function-dax.md).

- [!INCLUDE [function-not-supported-in-directquery-mode](includes/function-not-supported-in-directquery-mode.md)]


## Example for calendar based time intelligence

The following sample formula creates a measure that calculates the 'week running total' or 'week running sum' for Internet sales in terms of fiscal calendar.

```dax
= TOTALWTD(SUM(InternetSales_USD[SalesAmount_USD]), FiscalCalendar)
```

## Related content

[ALL](all-function-dax.md)
[CALCULATE](calculate-function-dax.md)
[TOTALYTD](totalytd-function-dax.md)
[TOTALQTD](totalqtd-function-dax.md)
[TOTALMTD](totalqtd-function-dax.md)
