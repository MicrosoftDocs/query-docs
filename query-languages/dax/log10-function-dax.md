---
description: "Learn more about: LOG10"
title: "LOG10 function (DAX) | Microsoft Docs"
ms.service: powerbi 
ms.subservice: dax 
ms.date: 07/08/2020
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend 
recommendations: false

---
# LOG10

Returns the base-10 logarithm of a number.  
  
## Syntax  
  
```dax
LOG10(<number>)  
```
  
### Parameters  
  
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
= LOG(100,10)  
= LOG(100)  
= LOG10(100)  
```
  
## See also

[Math and Trig functions](math-and-trig-functions-dax.md)  
[EXP function](exp-function-dax.md)  
[LOG function](log-function-dax.md)  
[LOG function](log-function-dax.md)  
  
