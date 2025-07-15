---
description: "Learn more about: CLOSINGBALANCEWEEK"
title: "CLOSINGBALANCEWEEK function (DAX)"
---
# CLOSINGBALANCEWEEK

[!INCLUDE[applies-to-measures-columns-tables-visual-calculations-discouraged](includes/applies-to-measures-columns-tables-visual-calculations-discouraged.md)]

Evaluates the `expression` at the last date of the week in the current context.
Note: week functions only work with calendar based time intelligence.

## Syntax

```
CLOSINGBALANCEWEEK(<expression>,<calendar>[,<filter>])
```

### Parameters

|Term|Definition|
|--------|--------------|
|`expression`|An expression that returns a scalar value.|
|`calendar`|A calendar reference.|
|`filter`|(optional) An expression that specifies a filter to apply to the current context.|

## Return value

A scalar value that represents the `expression` evaluated at the last date of the week in the current context.

## Remarks

- [!INCLUDE [function-not-supported-in-directquery-mode](includes/function-not-supported-in-directquery-mode.md)]


## Example for calendar based time intelligence

The following sample formula creates a measure that calculates the 'Week End Inventory Value' of the product inventory in terms of fiscal calendar.

```dax
= CLOSINGBALANCEWEEK (
    SUMX (
        ProductInventory,
        ProductInventory[UnitCost] * ProductInventory[UnitsBalance]
    ),
    FiscalCalendar
)
```

## Related content

[Time intelligence functions](time-intelligence-functions-dax.md)
[CLOSINGBALANCEYEAR function](closingbalanceyear-function-dax.md)
[CLOSINGBALANCEQUARTER function](closingbalancequarter-function-dax.md)
[CLOSINGBALANCEMONTH function](closingbalancemonth-function-dax.md)
