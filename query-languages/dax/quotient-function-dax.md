---
title: "QUOTIENT function (DAX) | Microsoft Docs"
ms.service: powerbi 
ms.date: 07/10/2020
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend

---
# QUOTIENT

Performs division and returns only the integer portion of the division result. Use this function when you want to discard the remainder of division.  
  
## Syntax  
  
```dax
QUOTIENT(<numerator>, <denominator>)  
```
  
### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|numerator|The dividend, or number to divide.|  
|denominator|The divisor, or number to divide by.|  
  
## Return value

A whole number.  
  
## Remarks

- If either argument is non-numeric, QUOTIENT returns the **#VALUE!** error value.  
  
- You can use a column reference instead of a literal value for either argument. However, if the column that you reference contains a 0 (zero), an error is returned for the entire column of values.  
  
## Example

The following formulas return the same result, 2.  
  
```dax
= QUOTIENT(5,2)
```

```dax
= QUOTIENT(10/2,2)  
```
  
## See also

[Math and Trig functions](math-and-trig-functions-dax.md)  
