---
description: "Learn more about: LN"
title: "LN function (DAX)"
---
# LN

[!INCLUDE[applies-to-measures-columns-tables-visual-calculations](includes/applies-to-measures-columns-tables-visual-calculations.md)]

Returns the natural logarithm of a number. Natural logarithms are based on the constant e (2.71828182845904).  
  
## Syntax  
  
```dax
LN(<number>)  
```
  
### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|`number`|The positive number for which you want the natural logarithm.|  
  
## Return value

A decimal number.  
  
## Remarks

LN is the inverse of the EXP function.  
  
## Example

The following example returns the natural logarithm of the number in the column, `[Values]`.  
  
```dax
= LN([Values])  
```
  
## Related content

[Math and Trig functions](math-and-trig-functions-dax.md)  
[EXP function](exp-function-dax.md)  
