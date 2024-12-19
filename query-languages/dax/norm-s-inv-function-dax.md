---
description: "Learn more about: NORM.S.INV"
title: "NORM.S.INV function (DAX)"
---
# NORM.S.INV

[!INCLUDE[applies-to-measures-columns-tables-visual-calculations](includes/applies-to-measures-columns-tables-visual-calculations.md)]

Returns the inverse of the standard normal cumulative distribution. The distribution has a mean of zero and a standard deviation of one.

## Syntax

```dax
NORM.S.INV(Probability)
```

### Parameters

|Term|Definition|
|--------|--------------|
|`Probability`|A probability corresponding to the normal distribution.|

## Return value

The inverse of the standard normal cumulative distribution. The distribution has a mean of zero and a standard deviation of one.

## Remarks

[!INCLUDE [function-not-supported-in-directquery-mode](includes/function-not-supported-in-directquery-mode.md)]

## Example

```dax
EVALUATE { NORM.S.INV(0.908789) }
```

Returns

|[Value]  |
|---------|
|1.33333467304411    |

## Related content

[NORM.INV](norm-inv-function-dax.md)
[NORM.S.DIST function](norm-s-dist-function-dax.md)
[NORM.DIST function](norm-dist-function-dax.md)
