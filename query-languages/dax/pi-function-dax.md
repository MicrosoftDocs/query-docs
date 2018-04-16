---
title: "PI Function (DAX) | Microsoft Docs"
ms.service: powerbi
ms.date: 4/13/2018
ms.reviewer: minewiskan
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# PI Function (DAX)
Returns the value of Pi, 3.14159265358979, accurate to 15 digits.  
  
## Syntax  
  
```  
PI()  
```  
  
## Return Value  
A decimal number with the value of Pi, 3.14159265358979, accurate to 15 digits.  
  
## Remarks  
Pi is a mathematical constant. In DAX, Pi is represented as a real number accurate to 15 digits, the same as Excel.  
  
## Example  
The following formula calculates the area of a circle given the radius in the column, `[Radius]`.  
  
```  
=PI()*([Radius]*2)  
```  
  
## See Also  
[Math and Trig Functions &#40;DAX&#41;](math-and-trig-functions-dax.md)  
  
