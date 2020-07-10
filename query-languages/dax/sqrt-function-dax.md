---
title: "SQRT function (DAX) | Microsoft Docs"
ms.service: powerbi 
ms.date: 07/10/2020
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend

---
# SQRT

Returns the square root of a number.  
  
## Syntax  
  
```dax
SQRT(<number>)  
```
  
### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|number|The number for which you want the square root, a column that contains numbers, or an expression that evaluates to a number.|  
  
## Return value

A decimal number.  
  
## Remarks

If the number is negative, the SQRT function returns an error.  
  
## Example

The following formula,  
  
```dax
= SQRT(25)  
```
  
## See also

[Math and Trig functions](math-and-trig-functions-dax.md)  
