---
description: "Learn more about: FALSE"
title: "FALSE function (DAX)"
---
# FALSE

[!INCLUDE[applies-to-measures-columns-tables-visual-calculations](includes/applies-to-measures-columns-tables-visual-calculations.md)]

Returns the logical value `FALSE`.

## Syntax

```dax
FALSE()
```

## Return value

Always `FALSE`.

## Remarks

The word `FALSE` is also interpreted as the logical value `FALSE`.

## Example

The formula returns the logical value `FALSE` when the value in the column, 'InternetSales_USD'[SalesAmount_USD], is less than or equal to 200000.

```dax
= IF(SUM('InternetSales_USD'[SalesAmount_USD]) >200000, TRUE(), false())
```

The following table shows the results when the example formula is used with 'ProductCategory'[ProductCategoryName] in Row Labels and 'DateTime'[CalendarYear] in Column Labels.

|Row Labels|2005|2006|2007|2008|-|Grand Total|
|---------------|-----------------|----|----|----|----|----|
|Accessories|``FALSE``|``FALSE``|``TRUE``|``TRUE``|``FALSE``|``TRUE``|
|Bikes|``TRUE``|``TRUE``|``TRUE``|``TRUE``|``FALSE``|``TRUE``|
|Clothing|``FALSE``|``FALSE``|``FALSE``|``FALSE``|``FALSE``|``TRUE``|
|Components|``FALSE``|``FALSE``|``FALSE``|``FALSE``|``FALSE``|``FALSE``|
||``FALSE``|``FALSE``|``FALSE``|``FALSE``|``FALSE``|``FALSE``|
|Grand Total|``TRUE``|``TRUE``|``TRUE``|``TRUE``|``FALSE``|``TRUE``|

## Related content

[TRUE function](true-function-dax.md)
[NOT function](not-function-dax.md)
[IF function](if-function-dax.md)
