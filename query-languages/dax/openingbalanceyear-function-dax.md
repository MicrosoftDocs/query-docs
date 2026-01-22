---
description: "Learn more about: OPENINGBALANCEYEAR"
title: "OPENINGBALANCEYEAR function (DAX)"
ms.topic: reference
---
# OPENINGBALANCEYEAR

[!INCLUDE[applies-to-measures-columns-tables-visual-calculations-discouraged](includes/applies-to-measures-columns-tables-visual-calculations-discouraged.md)]

Evaluates the `expression` at the date corresponding to the end of the previous year in the current context.

## Syntax

```
OPENINGBALANCEYEAR(<expression>,<dates> or <calendar>[,<filter>][,<year_end_date>])
```

### Parameters

|Term|Definition|
|--------|--------------|
|`expression`|An expression that returns a scalar value.|
|`dates or calendar`|A column that contains dates or a calendar reference.|
|`filter`|(optional) An expression that specifies a filter to apply to the current context.|
|`year_end_date`|(optional) A literal string with a date that defines the year-end date. The default is December 31. Only applies when date column is used.|

## Return value

A scalar value that represents the `expression` evaluated at the end of the previous year in the current context.

## Remarks

- The `dates` argument can be any of the following:
  - A reference to a date/time column.
  - A table expression that returns a single column of date/time values.
  - A Boolean expression that defines a single-column table of date/time values.

- Constraints on Boolean expressions are described in the topic, [CALCULATE function](calculate-function-dax.md).

- The `filter` expression has restrictions described in the topic, [CALCULATE function](calculate-function-dax.md).

- The `year_end_date` parameter is a string literal of a date, in the same locale as the locale of the client where the workbook was created. The year portion of the date is ignored.

- The `year_end_date` parameter must not be specified when a calendar is used.

- [!INCLUDE [function-not-supported-in-directquery-mode](includes/function-not-supported-in-directquery-mode.md)]

## Example

The following sample formula creates a measure that calculates the 'Year Start Inventory Value' of the product inventory.

```dax
=
OPENINGBALANCEYEAR (
    SUMX (
        ProductInventory,
        ProductInventory[UnitCost] * ProductInventory[UnitsBalance]
    ),
    DateTime[DateKey]
)
```

## Example for calendar based time intelligence

The following sample formula creates a measure that calculates the 'Year Start Inventory Value' of the product inventory in terms of fiscal calendar.

```dax
=
OPENINGBALANCEYEAR (
    SUMX (
        ProductInventory,
        ProductInventory[UnitCost] * ProductInventory[UnitsBalance]
    ),
    FiscalCalendar
)
```

## Related content

- [OPENINGBALANCEWEEK function](openingbalanceweek-function-dax.md)
- [OPENINGBALANCEQUARTER function](openingbalancequarter-function-dax.md)
- [OPENINGBALANCEMONTH function](openingbalancemonth-function-dax.md)
- [Time intelligence functions](time-intelligence-functions-dax.md)
- [CLOSINGBALANCEYEAR function](closingbalanceyear-function-dax.md)
