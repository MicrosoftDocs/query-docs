---
title: "EXP Function (DAX) | Microsoft Docs"
ms.service: powerbi
ms.date: 4/13/2018
ms.reviewer: Minewiskan
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# EXP Function (DAX)
Returns e raised to the power of a given number. The constant e equals 2.71828182845904, the base of the natural logarithm.  
  
## Syntax  
  
```  
EXP(<number>)  
```  
  
#### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|**number**|The exponent applied to the base e. The constant e equals 2.71828182845904, the base of the natural logarithm.|  
  
## Return Value  
A decimal number.  
  
## Exceptions  
  
## Remarks  
EXP is the inverse of LN, which is the natural logarithm of the given number.  
  
To calculate powers of bases other than e, use the exponentiation operator (^). For more information, see [DAX Operator Reference](dax-operator-reference.md).  
  
## Example  
The following formula calculates e raised to the power of the number contained in the column, `[Power]`.  
  
```  
=EXP([Power])  
```  
  
## See Also  
[Math and Trig Functions &#40;DAX&#41;](math-and-trig-functions-dax.md)  
[LN Function &#40;DAX&#41;](ln-function-dax.md)  
[EXP Function &#40;DAX&#41;](exp-function-dax.md)  
[LOG Function &#40;DAX&#41;](log-function-dax.md)  
[LOG Function &#40;DAX&#41;](log-function-dax.md)  
  
