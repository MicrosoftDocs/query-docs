---
title: "TRUNC function (DAX) | Microsoft Docs"
ms.service: powerbi 

ms.date: 11/07/2018
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# TRUNC function (DAX)
Truncates a number to an integer by removing the decimal, or fractional, part of the number.  
  
## Syntax  
  
```dax
TRUNC(<number>,<num_digits>)  
```
  
#### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|number|The number you want to truncate.|  
|num_digits|A number specifying the precision of the truncation; if omitted, 0 (zero)|  
  
## Return value  
A whole number.  
  
## Remarks  
TRUNC and INT are similar in that both return integers. TRUNC removes the fractional part of the number. INT rounds numbers down to the nearest integer based on the value of the fractional part of the number. INT and TRUNC are different only when using negative numbers: `TRUNC(-4.3)` returns -4, but `INT(-4.3)` returns -5 because -5 is the smaller number.  
  
## Example  
The following formula returns 3, the integer part of pi.  
  
```dax
=TRUNC(PI())  
```
  
## Example  
The following formula returns -8, the integer part of -8.9.  
  
```dax
=TRUNC(-8.9)  
```
  
## See also  
[Math and Trig functions &#40;DAX&#41;](math-and-trig-functions-dax.md)  
[ROUND function &#40;DAX&#41;](round-function-dax.md)  
[ROUNDUP function &#40;DAX&#41;](roundup-function-dax.md)  
[ROUNDDOWN function &#40;DAX&#41;](rounddown-function-dax.md)  
[MROUND function &#40;DAX&#41;](mround-function-dax.md)  
[INT function &#40;DAX&#41;](int-function-dax.md)  
  
