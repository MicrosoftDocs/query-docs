---
description: "Learn more about: SQRT"
title: "SQRT function (DAX)"
ms.topic: reference
---
# SQRT

[!INCLUDE[applies-to-measures-columns-tables-visual-calculations](includes/applies-to-measures-columns-tables-visual-calculations.md)]

Returns the square root of a number.

## Syntax

```dax
SQRT(<number>)
```

### Parameters

|Term|Definition|
|--------|--------------|
|`number`|The number for which you want the square root, a column that contains numbers, or an expression that evaluates to a number.|

## Return value

A decimal number.

## Remarks

If the number is negative, the SQRT function returns an error.

## Example

The following formula,

```dax
= SQRT(25)
```

## Related content

- [Math and Trig functions](math-and-trig-functions-dax.md)
