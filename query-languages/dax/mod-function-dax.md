---
description: "Learn more about: MOD"
title: "MOD function (DAX) | Microsoft Docs"
---
# MOD

[!INCLUDE[applies-to-measures-columns-tables-visual-calculations](includes/applies-to-measures-columns-tables-visual-calculations.md)]

Returns the remainder after a number is divided by a divisor. The result always has the same sign as the divisor.  
  
## Syntax  
  
```dax
MOD(<number>, <divisor>)  
```
  
### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|`number`|The number for which you want to find the remainder after the division is performed.|  
|`divisor`|The number by which you want to divide.|  
  
## Return value

A whole number.  
  
## Remarks

- If the divisor is 0 (zero), MOD returns an error. You cannot divide by 0.  
  
- The MOD function can be expressed in terms of the INT function: MOD(n, d) = n - d*INT(n/d)  
  
## Example 1

The following formula returns 1, the remainder of 3 divided by 2.  
  
```dax
= MOD(3,2)  
```
  
## Example 2

The following formula returns -1, the remainder of 3 divided by 2. Note that the sign is always the same as the sign of the divisor.  
  
```dax
= MOD(-3,-2)  
```
  
## Related content

[Math and Trig functions](math-and-trig-functions-dax.md)  
[ROUND function](round-function-dax.md)  
[ROUNDUP function](roundup-function-dax.md)  
[ROUNDDOWN function](rounddown-function-dax.md)  
[MROUND function](mround-function-dax.md)  
[INT function](int-function-dax.md)  
