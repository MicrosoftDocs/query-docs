---
description: "Learn more about: PI"
title: "PI function (DAX)"
---
# PI

[!INCLUDE[applies-to-measures-columns-tables-visual-calculations](includes/applies-to-measures-columns-tables-visual-calculations.md)]

Returns the value of Pi, 3.14159265358979, accurate to 15 digits.

## Syntax

```dax
PI()
```

## Return value

A decimal number with the value of Pi, 3.14159265358979, accurate to 15 digits.

## Remarks

Pi is a mathematical constant. In DAX, Pi is represented as a real number accurate to 15 digits, the same as Excel.

## Example

The following formula calculates the area of a circle given the radius in the column, `[Radius]`.

```dax
= PI()*([Radius]*2)
```

## Related content

[Math and Trig functions](math-and-trig-functions-dax.md)
