---
description: "Learn more about: PRODUCT"
title: "PRODUCT function (DAX)"
---
# PRODUCT

[!INCLUDE[applies-to-measures-columns-tables-visual-calculations](includes/applies-to-measures-columns-tables-visual-calculations.md)]

Returns the product of the numbers in a column.

## Syntax

```dax
PRODUCT(<column>)
```

### Parameters

|Term|Definition|
|--------|--------------|
|`column`|The column that contains the numbers for which the product is to be computed.|

## Return value

A decimal number.

## Remarks

- To return the product of an expression evaluated for each row in a table, use [PRODUCTX function](productx-function-dax.md).

- Only the numbers in the column are counted. Blanks, logical values, and text are ignored. For example,

  `PRODUCT( Table[Column] )` is equivalent to `PRODUCTX( Table, Table[Column] )`.

- [!INCLUDE [function-not-supported-in-directquery-mode](includes/function-not-supported-in-directquery-mode.md)]
 
## Example

The following computes the product of the AdjustedRates column in an Annuity table:

```dax
= PRODUCT( Annuity[AdjustedRates] )
```

## Related content

[PRODUCTX](productx-function-dax.md)
