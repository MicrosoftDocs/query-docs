---
description: "Learn more about: ABS"
title: "ABS function (DAX) | Microsoft Docs"
ms.service: powerbi 
ms.subservice: dax
ms.date: 06/21/2022
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend 
recommendations: false

---

# ABS

Returns the absolute value of a number.  
  
## Syntax  
  
```dax
ABS(<number>)  
```
  
### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|number|The number for which you want the absolute value.|  
  
## Return value

A decimal number.  
  
## Remarks

The absolute value of a number is a decimal number, whole or decimal, without its sign. You can use the ABS function to ensure that only non-negative numbers are returned from expressions when nested in functions that require a positive number.  
  
## Example

The following example returns the absolute value of the difference between the list price and the dealer price, which you might use in a new calculated column, **DealerMarkup**.  
  
```dax
= ABS([DealerPrice]-[ListPrice])  
```
  
## See also

[Math and Trig functions](math-and-trig-functions-dax.md)  
[SIGN function](sign-function-dax.md)  
