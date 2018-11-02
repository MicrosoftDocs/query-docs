---
title: "QUOTIENT Function (DAX) | Microsoft Docs"
ms.service: powerbi 

ms.date: 5/22/2018
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# QUOTIENT Function (DAX)
Performs division and returns only the integer portion of the division result. Use this function when you want to discard the remainder of division.  
  
## Syntax  
  
```dax
QUOTIENT(<numerator>, <denominator>)  
```
  
#### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|**numerator**|The dividend, or number to divide.|  
|**denominator**|The divisor, or number to divide by.|  
  
## Return Value  
A whole number.  
  
## Remarks  
If either argument is non-numeric, QUOTIENT returns the **#VALUE!** error value.  
  
You can use a column reference instead of a literal value for either argument. However, if the column that you reference contains a 0 (zero), an error is returned for the entire column of values.  
  
## Example  
The following formulas return the same result, 2.  
  
```dax
=QUOTIENT(5,2)  
=QUOTIENT(10/2,2)  
```
  
## See Also  
[Math and Trig Functions &#40;DAX&#41;](math-and-trig-functions-dax.md)  
  
