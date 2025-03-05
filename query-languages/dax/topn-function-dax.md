---
description: "Learn more about: TOPN"
title: "TOPN function (DAX)"
---
# TOPN

[!INCLUDE[applies-to-measures-columns-tables-visual-calculations](includes/applies-to-measures-columns-tables-visual-calculations.md)]

Returns the top N rows of the specified table.

## Syntax

```dax
TOPN(<N_Value>, <Table>, <OrderBy_Expression>, [<Order>[, <OrderBy_Expression>, [<Order>]]…])
```

### Parameters

|Parameter|Definition|
|-------------|--------------|
|`N_Value`|The number of rows to return. Any DAX expression that returns a scalar value, where the expression is to be evaluated multiple times (for each row/context). See Remarks to better understand when the number of rows returned could be larger than `n_value`.  |
|`Table`|Any DAX expression that returns a table of data from where to extract the top 'n' rows. See Remarks to better understand when an empty table is returned.  |
|`OrderBy_Expression`|(Optional) Any DAX expression where the result value is used to sort the table and evaluated for each row of `table`.  |
|`Order`|(Optional) A value that specifies how to sort `OrderBy_Expression` values:<br /><br /> - `0` (zero) or  `FALSE`. Sorts in descending order of values of `Order`. Default when `Order` parameter is omitted. <br /><br /> - `1` or `TRUE`. Ranks in ascending order of `OrderBy`.|

## Return value

A table with the top N rows of `Table` or an empty table if `N_Value` is 0 (zero) or less. Rows are not sorted in any particular order.

## Remarks

- If there is a tie, in `Order_By` values, at the N-th row of the table, then all tied rows are returned. Then, when there are ties at the N-th row the function might return more than n rows.

- If N_Value is 0 (zero) or less, TOPN returns an empty table.

- TOPN does not guarantee any sort order for the results.

- [!INCLUDE [function-not-supported-in-directquery-mode](includes/function-not-supported-in-directquery-mode.md)]

## Example

The following measure formula returns the top 10 sold products by sales amount.

```dax
= SUMX(
        TOPN(
            10, 
            SUMMARIZE(
                    InternetSales, 
                    InternetSales[ProductKey], 
                    "TotalSales", SUM(InternetSales[SalesAmount])
            ),
            [TotalSales], DESC
        ),
        [TotalSales]
)
 
```
