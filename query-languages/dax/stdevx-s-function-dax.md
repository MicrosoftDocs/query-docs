---
description: "Learn more about: STDEVX.S"
title: "STDEVX.S function (DAX)"
---
# STDEVX.S

[!INCLUDE[applies-to-measures-columns-tables-visual-calculations](includes/applies-to-measures-columns-tables-visual-calculations.md)]

Returns the standard deviation of a sample population.

## Syntax

```dax
STDEVX.S(<table>, <expression>)
```

### Parameters

|Term|Definition|
|--------|--------------|
|`table`  | Any DAX expression that returns a single scalar value, where the expression is to be evaluated multiple times (for each row/context).  |
|`expression`   | Any DAX expression that returns a single scalar value, where the expression is to be evaluated multiple times (for each row/context).   |

## Return value

A number with the standard deviation of a sample population.

## Exceptions

## Remarks

- STDEVX.S evaluates `expression` for each row of `table` and returns the standard deviation of `expression` assuming that `table` refers to a sample of the population. If `table` represents the entire population, then compute the standard deviation by using STDEVX.P.

- STDEVX.S uses the following formula:

    √[∑(x - x̃)<sup>2</sup>/(n-1)]

    where x̃ is the average value of x for the entire population and n is the population size.

- Blank rows are filtered out from `columnName` and not considered in the calculations.

- An error is returned if `columnName` contains less than 2 non-blank rows.

- [!INCLUDE [function-not-supported-in-directquery-mode](includes/function-not-supported-in-directquery-mode.md)]

## Example

The following example shows the formula for a calculated column that estimates the standard deviation of the unit price per product for a sample population, when the formula is used in the Product table.

```dax
= STDEVX.S(RELATEDTABLE(InternetSales_USD), InternetSales_USD[UnitPrice_USD] – (InternetSales_USD[DiscountAmount_USD]/InternetSales_USD[OrderQuantity]))
```
