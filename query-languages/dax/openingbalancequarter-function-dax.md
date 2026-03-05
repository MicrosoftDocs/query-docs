---
description: "Learn more about: OPENINGBALANCEQUARTER"
title: "OPENINGBALANCEQUARTER function (DAX)"
ms.topic: reference
---
# OPENINGBALANCEQUARTER

[!INCLUDE[applies-to-measures-columns-tables-visual-calculations-discouraged](includes/applies-to-measures-columns-tables-visual-calculations-discouraged.md)]

Evaluates the `expression` at the date corresponding to the end of the previous quarter in the current context.

## Syntax

```
OPENINGBALANCEQUARTER(<expression>,<dates> or <calendar>[,<filter>])
```

### Parameters

|Term|Definition|
|--------|--------------|
|`expression`|An expression that returns a scalar value.|
|`dates or calendar`|A column that contains dates or a calendar reference.|
|`filter`|(optional) An expression that specifies a filter to apply to the current context.|

## Return value

A scalar value that represents the `expression` at the end of the previous quarter in the current context.

## Remarks

- The `dates` argument can be any of the following:
  - A reference to a date/time column.
  - A table expression that returns a single column of date/time values.
  - A Boolean expression that defines a single-column table of date/time values.

- Constraints on Boolean expressions are described in the topic, [CALCULATE function](calculate-function-dax.md).

- The `filter` expression has restrictions described in the topic, [CALCULATE function](calculate-function-dax.md).

- [!INCLUDE [function-not-supported-in-directquery-mode](includes/function-not-supported-in-directquery-mode.md)] 

## Example

The following sample formula creates a measure that calculates the 'Quarter Start Inventory Value' of the product inventory.

```dax
=
OPENINGBALANCEQUARTER (
    SUMX (
        ProductInventory,
        ProductInventory[UnitCost] * ProductInventory[UnitsBalance]
    ),
    DateTime[DateKey]
)
```

## Example for calendar based time intelligence

The following sample formula creates a measure that calculates the 'Quarter Start Inventory Value' of the product inventory in terms of fiscal calendar.

```dax
=
OPENINGBALANCEQUARTER (
    SUMX (
        ProductInventory,
        ProductInventory[UnitCost] * ProductInventory[UnitsBalance]
    ),
    FiscalCalendar
)
```

## Related content

- [OPENINGBALANCEWEEK function](openingbalanceweek-function-dax.md)
- [OPENINGBALANCEYEAR function](openingbalanceyear-function-dax.md)
- [OPENINGBALANCEMONTH function](openingbalancemonth-function-dax.md)
- [Time intelligence functions](time-intelligence-functions-dax.md)
- [CLOSINGBALANCEQUARTER function](closingbalancequarter-function-dax.md)
