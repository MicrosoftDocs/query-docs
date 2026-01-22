---
description: "Learn more about: SUM"
title: "SUM function (DAX)"
ms.topic: reference
---
# SUM

[!INCLUDE[applies-to-measures-columns-tables-visual-calculations](includes/applies-to-measures-columns-tables-visual-calculations.md)]

Adds all the numbers in a column.

## Syntax

```dax
SUM(<column>)
```

### Parameters

|Term|Definition|
|--------|--------------|
|`column`|The column that contains the numbers to sum.|

## Return value

A decimal number.

## Remarks

If you want to filter the values that you are summing, you can use the SUMX function and specify an expression to sum over.

## Example

The following example adds all the numbers that are contained in the column, Amt, from the table, Sales.

```dax
= SUM(Sales[Amt])
```

## Related content

- [SUMX](sumx-function-dax.md)
