---
description: "Learn more about: INT"
title: "INT function (DAX)"
---
# INT

[!INCLUDE[applies-to-measures-columns-tables-visual-calculations](includes/applies-to-measures-columns-tables-visual-calculations.md)]

Rounds a number down to the nearest integer.

## Syntax

```dax
INT(<number>)
```

### Parameters

|Term|Definition|
|--------|--------------|
|`number`|The number you want to round down to an integer|

## Return value

A whole number.

## Remarks

TRUNC and INT are similar in that both return integers. TRUNC removes the fractional part of the number. INT rounds numbers down to the nearest integer based on the value of the fractional part of the number. INT and TRUNC are different only when using negative numbers: `TRUNC(-4.3)` returns -4, but `INT(-4.3)` returns -5 because -5 is the lower number.

## Example

The following expression rounds the value to 1. If you use the ROUND function, the result would be 2.

```dax
= INT(1.5)
```

## Related content

[Math and Trig functions](math-and-trig-functions-dax.md)
[ROUND function](round-function-dax.md)
[ROUNDUP function](roundup-function-dax.md)
[ROUNDDOWN function](rounddown-function-dax.md)
[MROUND function](mround-function-dax.md)
