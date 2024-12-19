---
description: "Learn more about: PRODUCTX"
title: "PRODUCTX function (DAX)"
---
# PRODUCTX

[!INCLUDE[applies-to-measures-columns-tables-visual-calculations](includes/applies-to-measures-columns-tables-visual-calculations.md)]

Returns the product of an expression evaluated for each row in a table.

## Syntax

```dax
PRODUCTX(<table>, <expression>)
```

### Parameters

|Term|Definition|
|--------|--------------|
|`table`|The table containing the rows for which the expression will be evaluated.|
|`expression`|The expression to be evaluated for each row of the table.|

## Return value

A decimal number.

## Remarks

- To return the product of the numbers in a column, use [PRODUCT](product-function-dax.md).

- The PRODUCTX function takes as its first argument a table, or an expression that returns a table. The second argument is a column that contains the numbers for which you want to compute the product, or an expression that evaluates to a column.

- Only the numbers in the column are counted. Blanks, logical values, and text are ignored.

- [!INCLUDE [function-not-supported-in-directquery-mode](includes/function-not-supported-in-directquery-mode.md)]

## Example

The following computes the future value of an investment:

```dax
= [PresentValue] * PRODUCTX( AnnuityPeriods, 1+[FixedInterestRate] )
```

## Related content

[PRODUCT](product-function-dax.md)
