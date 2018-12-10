---
title: "LOG function (DAX) | Microsoft Docs"
ms.service: powerbi 

ms.date: 12/10/2018
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# LOG
Returns the logarithm of a number to the base you specify.  
  
## Syntax  
  
```dax
LOG(<number>,<base>)  
```
  
#### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|number|The positive number for which you want the logarithm.|  
|base|The base of the logarithm. If omitted, the base is 10.|  
  
## Return value  
A decimal number.  
  
## Remarks  
You might receive an error if the value is too large to be displayed.  
  
The function LOG10 is similar, but always returns the common logarithm, meaning the logarithm for the base 10.  
  
## Example  
The following formulas return the same result, 2.  
  
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
  
