---
description: "Learn more about: DISTINCTCOUNT"
title: "DISTINCTCOUNT function (DAX)"
ms.topic: reference
---
# DISTINCTCOUNT

[!INCLUDE[applies-to-measures-columns-tables-visual-calculations](includes/applies-to-measures-columns-tables-visual-calculations.md)]

Counts the number of distinct values in a column.

## Syntax

```dax
DISTINCTCOUNT(<column>)
```

### Parameters

|Term  |Description|
|---------|---------|
|`column`| The column that contains the values to be counted |

## Return value

The number of distinct values in `column`.

## Remarks

- The only argument allowed to this function is a column. You can use columns containing any type of data. When the function finds no rows to count, it returns a BLANK, otherwise it returns the count of distinct values.

- DISTINCTCOUNT function counts the BLANK value. To skip the BLANK value, use the [DISTINCTCOUNTNOBLANK](distinctcountnoblank-function-dax.md) function.

- [!INCLUDE [function-not-supported-in-directquery-mode](includes/function-not-supported-in-directquery-mode.md)]

## Example

The following example shows how to count the number of distinct sales orders in the column ResellerSales_USD[SalesOrderNumber].

```dax
= DISTINCTCOUNT(ResellerSales_USD[SalesOrderNumber])
```

Using the above measure in a table with calendar year in the side and product category on top returns the following results:

|Row Labels|Accessories|Bikes|Clothing|Components|-|Grand Total|
|-----|-----|-----|-----|-----|-----|-----|
|2005|135|345|242|205||366|
|2006|356|850|644|702||1015|
|2007|531|1234|963|1138||1521|
|2008|293|724|561|601||894|
||||||1|1|
|**Grand Total**|**1315**|**3153**|**2410**|**2646**|**1**|**3797**|

### Understanding distinct count totals

Distinct count totals are not additive. The Grand Total is not the sum of the values in each category.

In the table above, you might expect the Grand Total for 2005 (366) to equal the sum of Accessories (135) + Bikes (345) + Clothing (242) + Components (205) = 927. However, the actual Grand Total is 366, which is much lower.

This happens because the same order can appear in multiple categories. For example, if order #1001 contains both a bike and an accessory, that order is counted once in the Bikes column and once in the Accessories column. But when calculating the Grand Total for the row, order #1001 is only counted once because it's still just one distinct order.

This is the correct and expected behavior of distinct counts:

- **Category values**: Count distinct orders within that specific category only.
- **Row totals**: Count distinct orders across all categories for that year - each order is counted only once, regardless of how many categories it appears in.
- **Grand Total**: Count distinct orders across the entire dataset.

If you need totals that add up, consider using [COUNT](count-function-dax.md) or [COUNTROWS](countrows-function-dax.md) instead. However, be aware that these functions count rows, not distinct values, and will give different results.

## Related content

[COUNT function](count-function-dax.md)
[COUNTA function](counta-function-dax.md)
[COUNTAX function](countax-function-dax.md)
[COUNTX function](countx-function-dax.md)
[Statistical functions](statistical-functions-dax.md)
