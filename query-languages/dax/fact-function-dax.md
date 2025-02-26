---
description: "Learn more about: FACT"
title: "FACT function (DAX)"
---
# FACT

[!INCLUDE[applies-to-measures-columns-tables-visual-calculations](includes/applies-to-measures-columns-tables-visual-calculations.md)]

Returns the factorial of a number, equal to the series 1*2\*3\*...\* , ending in the given number.

## Syntax

```dax
FACT(<number>)
```

### Parameters

|Term|Definition|
|--------|--------------|
|`number`|The non-negative number for which you want to calculate the factorial.|

## Return value

A decimal number.

## Remarks

- If the number is not an integer, it is truncated and an error is returned. If the result is too large, an error is returned.

- [!INCLUDE [function-not-supported-in-directquery-mode](includes/function-not-supported-in-directquery-mode.md)]

## Example

The following formula returns the factorial for the series of integers in the column, `[Values]`.

```dax
= FACT([Values])
```

The following table shows the expected results:

|Values|Results|
|----------|-----------|
|0|1|
|1|1|
|2|2|
|3|6|
|4|24|
|5|120|
|170|7.257415615308E+306|

## Related content

[Math and Trig functions](math-and-trig-functions-dax.md)
[TRUNC function](trunc-function-dax.md)
