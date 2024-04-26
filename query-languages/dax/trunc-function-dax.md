---
description: "Learn more about: TRUNC"
title: "TRUNC function (DAX) | Microsoft Docs"
---
# TRUNC

[!INCLUDE[applies-to-measures-columns-tables-visual-calculations](includes/applies-to-measures-columns-tables-visual-calculations.md)]

Truncates a number to an integer by removing the decimal, or fractional, part of the number.  
  
## Syntax  
  
```dax
TRUNC(<number>,<num_digits>)  
```
  
### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|number|The number you want to truncate.|  
|num_digits|A number specifying the precision of the truncation; if omitted, 0 (zero)|  
  
## Return value

A whole number.  
  
## Remarks

TRUNC and INT are similar in that both return integers. TRUNC removes the fractional part of the number. INT rounds numbers down to the nearest integer based on the value of the fractional part of the number. INT and TRUNC are different only when using negative numbers: `TRUNC(-4.3)` returns -4, but `INT(-4.3)` returns -5 because -5 is the smaller number.  
  
## Example 1

The following formula returns 3, the integer part of pi.  
  
```dax
= TRUNC(PI())  
```
  
## Example 2

The following formula returns -8, the integer part of -8.9.  
  
```dax
= TRUNC(-8.9)  
```
  
## Related content

[Math and Trig functions](math-and-trig-functions-dax.md)  
[ROUND](round-function-dax.md)  
[ROUNDUP](roundup-function-dax.md)  
[ROUNDDOWN](rounddown-function-dax.md)  
[MROUND](mround-function-dax.md)  
[INT](int-function-dax.md)  
