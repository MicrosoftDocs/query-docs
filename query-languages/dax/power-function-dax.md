---
title: "POWER function (DAX) | Microsoft Docs"
ms.service: powerbi 
ms.date: 07/10/2020
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend

---
# POWER

Returns the result of a number raised to a power.  
  
## Syntax  
  
```dax
POWER(<number>, <power>)  
```
  
### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|number|The base number, which can be any real number.|  
|power|The exponent to which the base number is raised.|  
  
## Return value

A decimal number.  
  
## Example

The following example returns 25.  
  
```dax
= POWER(5,2)  
```
  
## See also

[Math and Trig functions](math-and-trig-functions-dax.md)  
