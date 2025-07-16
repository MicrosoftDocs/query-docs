---
description: "Learn more about: OPENINGBALANCEWEEK"
title: "OPENINGBALANCEWEEK function (DAX)"
---
# OPENINGBALANCEWEEK

[!INCLUDE[applies-to-measures-columns-tables-visual-calculations-discouraged](includes/applies-to-measures-columns-tables-visual-calculations-discouraged.md)]

Evaluates the `expression` at the date corresponding to the end of the previous week in the current context.  
Note: week functions only work with calendar based time intelligence.

## Syntax

```
OPENINGBALANCEWEEK(<expression>,<calendar>[,<filter>])
```

### Parameters

|Term|Definition|
|--------|--------------|
|`expression`|An expression that returns a scalar value.|
|`calendar`|A calendar reference.|
|`filter`|(optional) An expression that specifies a filter to apply to the current context.|

## Return value

A scalar value that represents the `expression` evaluated at the first date of the week in the current context.

## Remarks

- Constraints on Boolean expressions are described in the topic, [CALCULATE function](calculate-function-dax.md).

- The `filter` expression has restrictions described in the topic, [CALCULATE function](calculate-function-dax.md).

- [!INCLUDE [function-not-supported-in-directquery-mode](includes/function-not-supported-in-directquery-mode.md)]


## Example for calendar based time intelligence

The following sample formula creates a measure that calculates the 'Week Start Inventory Value' of the product inventory in terms of fiscal calendar.

```dax
=
OPENINGBALANCEWEEK (
    SUMX (
        ProductInventory,
        ProductInventory[UnitCost] * ProductInventory[UnitsBalance]
    ),
    FiscalCalendar
)
```

## Related content

[OPENINGBALANCEYEAR function](openingbalanceyear-function-dax.md)
[OPENINGBALANCEQUARTER function](openingbalancequarter-function-dax.md)
[OPENINGBALANCEMONTH function](openingbalancemonth-function-dax.md)
[Time intelligence functions](time-intelligence-functions-dax.md)
[CLOSINGBALANCEWEEK function](closingbalanceweek-function-dax.md)
