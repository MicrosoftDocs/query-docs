---
description: "Learn more about: CLOSINGBALANCEYEAR"
title: "CLOSINGBALANCEYEAR function (DAX)"
---
# CLOSINGBALANCEYEAR

[!INCLUDE[applies-to-measures-columns-tables-visual-calculations-discouraged](includes/applies-to-measures-columns-tables-visual-calculations-discouraged.md)]

Evaluates the `expression` at the last date of the year in the current context.

## Syntax

```dax
CLOSINGBALANCEYEAR(<expression>,<dates|calendar>[,<filter>][,<year_end_date>])
```

### Parameters

|Term|Definition|
|--------|--------------|
|`expression`|An expression that returns a scalar value.|
|`dates/calendar`|A column that contains dates or a calendar reference.|
|`filter`|(optional) An expression that specifies a filter to apply to the current context.|
|`year_end_date`|(optional) A literal string with a date that defines the year-end date. The default is December 31.|

## Return value

A scalar value that represents the `expression` evaluated at the last date of the year in the current context.

## Remarks

- The `year_end_date` parameter is a string literal of a date, in the same locale as the locale of the client where the workbook was created. The year portion of the date is ignored.

- The `dates` argument can be any of the following:

  - A reference to a date/time column.

  - A table expression that returns a single column of date/time values.

  - A Boolean expression that defines a single-column table of date/time values.

    > [!NOTE]
    > Constraints on Boolean expressions are described in [CALCULATE function](calculate-function-dax.md).

    > [!NOTE]
    > The `filter` expression has restrictions described in [CALCULATE function](calculate-function-dax.md).

- In addition to `dates`, a calendar reference could also be used at second argument.

- [!INCLUDE [function-not-supported-in-directquery-mode](includes/function-not-supported-in-directquery-mode.md)]

## Example

The following sample formula creates a measure that calculates the 'Year End Inventory Value' of the product inventory.

```dax
= CLOSINGBALANCEYEAR(SUMX(ProductInventory,ProductInventory[UnitCost]*ProductInventory[UnitsBalance]),DateTime[DateKey])
```

## Example for calendar based time intelligence

The following sample formula creates a measure that calculates the 'Year End Inventory Value' of the product inventory in terms of fiscal calendar.

```dax
= CLOSINGBALANCEYEAR(SUMX(ProductInventory,ProductInventory[UnitCost]*ProductInventory[UnitsBalance]), FiscalCalendar)
```

## Related content

[Time intelligence functions](time-intelligence-functions-dax.md)
[CLOSINGBALANCEQUARTER function](closingbalancequarter-function-dax.md)
[CLOSINGBALANCEMONTH function](closingbalancemonth-function-dax.md)
[CLOSINGBALANCEWEEK function](closingbalanceweek-function-dax.md)
