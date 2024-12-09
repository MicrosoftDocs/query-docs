---
description: "Learn more about: GCD"
title: "GCD function (DAX)"
---
# GCD

[!INCLUDE[applies-to-measures-columns-tables-visual-calculations](includes/applies-to-measures-columns-tables-visual-calculations.md)]

Returns the greatest common divisor of two or more integers. The greatest common divisor is the largest integer that divides both number1 and number2 without a remainder.  
  
## Syntax  
  
```dax
GCD(number1, [number2], ...)  
```
  
### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|`number1, number2, ...`|Number1 is required, subsequent numbers are optional. 1 to 255 values. If any value is not an integer, it is truncated.|  
  
## Return value

The greatest common divisor of two or more integers.  
  
## Remarks

- If any argument is nonnumeric, GCD returns the `#VALUE!` error value.  
  
- If any argument is less than zero, GCD returns the `#NUM!` error value.  
  
- One divides any value evenly.  
  
- A prime number has only itself and one as even divisors.  
  
- If a parameter to GCD is &gt;=2^53, GCD returns the `#NUM!` error value.  

- [!INCLUDE [function-not-supported-in-directquery-mode](includes/function-not-supported-in-directquery-mode.md)]

## Example  
  
|DAX expression|Description|Result|
|-----------|---------------|----------|  
|`= GCD(5, 2)`|Greatest common divisor of 5 and 2.|1|  
|`= GCD(24, 36)`|Greatest common divisor of 24 and 36.|12|  
|`= GCD(7, 1)`|Greatest common divisor of 7 and 1.|1|  
