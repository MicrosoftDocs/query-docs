---
title: "LOG10 function (DAX) | Microsoft Docs"
ms.service: powerbi 
ms.date: 12/10/2018
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# LOG10
Returns the base-10 logarithm of a number.  
  
## Syntax  
  
```dax
LOG10(<number>)  
```
  
#### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|number|A positive number for which you want the base-10 logarithm.|  
  
## Return value  
A decimal number.  
  
## Remarks  
The LOG function lets you change the base of the logarithm, instead of using the base 10.  
  
## Example  
The following formulas return the same result, 2:  
  
```dax
=LOG(100,10)  
=LOG(100)  
=LOG10(100)  
```
  
## See also  
[Math and Trig functions &#40;DAX&#41;](math-and-trig-functions-dax.md)  
[EXP function &#40;DAX&#41;](exp-function-dax.md)  
[LOG function &#40;DAX&#41;](log-function-dax.md)  
[LOG function &#40;DAX&#41;](log-function-dax.md)  
  
