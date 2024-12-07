---
description: "Learn more about: LOG10"
title: "LOG10 function (DAX) | Microsoft Docs"
---
# LOG10

[!INCLUDE[applies-to-measures-columns-tables-visual-calculations](includes/applies-to-measures-columns-tables-visual-calculations.md)]

Returns the base-10 logarithm of a number.  
  
## Syntax  
  
```dax
LOG10(<number>)  
```
  
### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|`number`|A positive number for which you want the base-10 logarithm.|  
  
## Return value

A decimal number.  
  
## Remarks

The LOG function lets you change the base of the logarithm, instead of using the base 10.  
  
## Example

The following formulas return the same result, 2:  
  
```dax
= LOG(100,10)  
= LOG(100)  
= LOG10(100)  
```
  
## Related content

[Math and Trig functions](math-and-trig-functions-dax.md)  
[EXP function](exp-function-dax.md)  
[LOG function](log-function-dax.md)  
[LOG function](log-function-dax.md)  
  
