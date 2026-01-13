---
description: "Learn more about: SIGN"
title: "SIGN function (DAX)"
ms.topic: reference
---
# SIGN

[!INCLUDE[applies-to-measures-columns-tables-visual-calculations](includes/applies-to-measures-columns-tables-visual-calculations.md)]

Determines the sign of a number, the result of a calculation, or a value in a column. The function returns 1 if the number is positive, 0 (zero) if the number is zero, or -1 if the number is negative.

## Syntax

```dax
SIGN(<number>)
```

### Parameters

|Term|Definition|
|--------|--------------|
|`number`|Any real number, a column that contains numbers, or an expression that evaluates to a number.|

## Return value

A whole number. The possible Return values are 1, 0, and -1.

|Return value|Description|
|----------------|---------------|
|1|The number is positive|
|0|The number is zero|
|-1|The number is negative|

## Example

The following formula returns the sign of the result of the expression that calculates sale price minus cost.

```dax
= SIGN( ([Sale Price] - [Cost]) )
```

## Related content

[Math and Trig functions](math-and-trig-functions-dax.md)
