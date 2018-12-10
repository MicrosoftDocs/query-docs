---
title: "LN function (DAX) | Microsoft Docs"
ms.service: powerbi 
ms.date: 12/10/2018
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# LN
Returns the natural logarithm of a number. Natural logarithms are based on the constant e (2.71828182845904).  
  
## Syntax  
  
```dax
LN(<number>)  
```
  
#### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|number|The positive number for which you want the natural logarithm.|  
  
## Return value  
A decimal number.  
  
## Remarks  
LN is the inverse of the EXP function.  
  
## Example  
The following example returns the natural logarithm of the number in the column, `[Values]`.  
  
```dax
=LN([Values])  
```
  
## See also  
[Math and Trig functions &#40;DAX&#41;](math-and-trig-functions-dax.md)  
[EXP function &#40;DAX&#41;](exp-function-dax.md)  
  
