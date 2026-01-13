---
description: "Learn more about: TOTALQTD"
title: "TOTALQTD function (DAX)"
ms.topic: reference
---
# TOTALQTD

[!INCLUDE[applies-to-measures-columns-tables-visual-calculations-discouraged](includes/applies-to-measures-columns-tables-visual-calculations-discouraged.md)]

Evaluates the value of the `expression` for the dates in the quarter to date, in the current context.

## Syntax

```
TOTALQTD(<expression>,<dates> or <calendar>[,<filter>])
```

### Parameters

|Parameter|Definition|
|-------------|--------------|
|`expression`|An expression that returns a scalar value.|
|`dates or calendar`|A column that contains dates or a calendar reference.|
|`filter`|(optional) An expression that specifies a filter to apply to the current context.|

## Return value

A scalar value that represents the `expression` evaluated for all dates in the current quarter to date, given the dates in `dates` or `calendar`.

## Remarks

- The `dates` argument can be any of the following:
  - A reference to a date/time column.
  - A table expression that returns a single column of date/time values.
  - A Boolean expression that defines a single-column table of date/time values.

- Constraints on Boolean expressions are described in the topic, [CALCULATE](calculate-function-dax.md).

- The `filter` expression has restrictions described in the topic, [CALCULATE](calculate-function-dax.md).

- [!INCLUDE [function-not-supported-in-directquery-mode](includes/function-not-supported-in-directquery-mode.md)]

## Example

The following sample formula creates a measure that calculates the 'quarter running total' or 'quarter running sum' for Internet sales.

```dax
= TOTALQTD(SUM(InternetSales_USD[SalesAmount_USD]),DateTime[DateKey])
```

## Example for calendar based time intelligence

The following sample formula creates a measure that calculates the 'quarter running total' or 'quarter running sum' for Internet sales in terms of fiscal calendar.

```dax
= TOTALQTD(SUM(InternetSales_USD[SalesAmount_USD]), FiscalCalendar)
```

## Related content

[ALL](all-function-dax.md)
[CALCULATE](calculate-function-dax.md)
[TOTALYTD](totalytd-function-dax.md)
[TOTALMTD](totalmtd-function-dax.md)
[TOTALWTD](totalwtd-function-dax.md)
