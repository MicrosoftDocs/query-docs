---
description: "Learn more about: ROUND"
title: "ROUND function (DAX)"
ms.topic: reference
---
# ROUND

[!INCLUDE[applies-to-measures-columns-tables-visual-calculations](includes/applies-to-measures-columns-tables-visual-calculations.md)]

Rounds a number to the specified number of digits.

## Syntax

```dax
ROUND(<number>, <num_digits>)
```

### Parameters

|Term|Definition|
|--------|--------------|
|`number`|The number you want to round.|
|`num_digits`|The number of digits to which you want to round. A negative value rounds digits to the left of the decimal point; a value of zero rounds to the nearest integer.|

## Return value

A decimal number.

## Remarks

- If `num_digits` is greater than 0 (zero), then number is rounded to the specified number of decimal places.

- If `num_digits` is 0, the number is rounded to the nearest integer.

- If `num_digits` is less than 0, the number is rounded to the left of the decimal point.

- Ties are broken by rounding half away from zero (also known as commercial rounding).
  | Examples | Result |
  | --- | --- |
  | `= ROUND(1.15, 1)` | 1.2 |
  | `= ROUND(-1.15, 1)` | -1.2 |

- Related functions
  - To always round up (away from zero), use the ROUNDUP function.
  - To always round down (toward zero), use the ROUNDDOWN function.
  - To round a number to a specific multiple (for example, to round to the nearest multiple of 0.5), use the MROUND function.
  - Use the functions TRUNC and INT to obtain the integer portion of the number.

## Example 1

The following formula rounds 2.15 up, to one decimal place. The expected result is 2.2.

```dax
= ROUND(2.15,1)
```

## Example 2

The following formula rounds 21.5 to one decimal place to the left of the decimal point. The expected result is 20.

```dax
= ROUND(21.5,-1)
```

## Related content
- [Math and Trig functions](math-and-trig-functions-dax.md)
- [ROUND](round-function-dax.md)
- [ROUNDDOWN](rounddown-function-dax.md)
- [MROUND](mround-function-dax.md)
- [INT](int-function-dax.md)
- [TRUNC](trunc-function-dax.md)

