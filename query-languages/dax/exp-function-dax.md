---
title: "EXP function (DAX) | Microsoft Docs"
ms.service: powerbi 
ms.date: 07/08/2020
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend

---
# EXP

Returns e raised to the power of a given number. The constant e equals 2.71828182845904, the base of the natural logarithm.  
  
## Syntax  
  
```dax
EXP(<number>)  
```
  
### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|number|The exponent applied to the base e. The constant e equals 2.71828182845904, the base of the natural logarithm.|  
  
## Return value

A decimal number.  
  
## Exceptions  
  
## Remarks

- EXP is the inverse of LN, which is the natural logarithm of the given number.  
  
- To calculate powers of bases other than e, use the exponentiation operator (^). For more information, see [DAX Operator Reference](dax-operator-reference.md).

## Example

The following formula calculates e raised to the power of the number contained in the column, `[Power]`.  
  
```dax
= EXP([Power])  
```
  
## See also

[Math and Trig functions &#40;DAX&#41;](math-and-trig-functions-dax.md)  
[LN function &#40;DAX&#41;](ln-function-dax.md)  
[EXP function &#40;DAX&#41;](exp-function-dax.md)  
[LOG function &#40;DAX&#41;](log-function-dax.md)  
[LOG function &#40;DAX&#41;](log-function-dax.md)  
