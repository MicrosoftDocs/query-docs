---
description: "Learn more about: PI"
title: "PI function (DAX) | Microsoft Docs"
ms.service: powerbi 
ms.date: 07/10/2020
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend 
recommendations: false

---
# PI

Returns the value of Pi, 3.14159265358979, accurate to 15 digits.  
  
## Syntax  
  
```dax
PI()  
```
  
## Return value

A decimal number with the value of Pi, 3.14159265358979, accurate to 15 digits.  
  
## Remarks

Pi is a mathematical constant. In DAX, Pi is represented as a real number accurate to 15 digits, the same as Excel.  
  
## Example

The following formula calculates the area of a circle given the radius in the column, `[Radius]`.  
  
```dax
= PI()*([Radius]*2)  
```
  
## See also

[Math and Trig functions](math-and-trig-functions-dax.md)  
