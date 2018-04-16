---
title: "TRUNC Function (DAX) | Microsoft Docs"
ms.service: powerbi
ms.date: 4/13/2018
ms.reviewer: Minewiskan
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# TRUNC Function (DAX)
Truncates a number to an integer by removing the decimal, or fractional, part of the number.  
  
## Syntax  
  
```  
TRUNC(<number>,<num_digits>)  
```  
  
#### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|**number**|The number you want to truncate.|  
|**num_digits**|A number specifying the precision of the truncation; if omitted, 0 (zero)|  
  
## Return Value  
A whole number.  
  
## Remarks  
TRUNC and INT are similar in that both return integers. TRUNC removes the fractional part of the number. INT rounds numbers down to the nearest integer based on the value of the fractional part of the number. INT and TRUNC are different only when using negative numbers: `TRUNC(-4.3)` returns -4, but `INT(-4.3)` returns -5 because -5 is the smaller number.  
  
## Example  
The following formula returns 3, the integer part of pi.  
  
```  
=TRUNC(PI())  
```  
  
## Example  
The following formula returns -8, the integer part of -8.9.  
  
```  
=TRUNC(-8.9)  
```  
  
## See Also  
[Math and Trig Functions &#40;DAX&#41;](math-and-trig-functions-dax.md)  
[ROUND Function &#40;DAX&#41;](round-function-dax.md)  
[ROUNDUP Function &#40;DAX&#41;](roundup-function-dax.md)  
[ROUNDDOWN Function &#40;DAX&#41;](rounddown-function-dax.md)  
[MROUND Function &#40;DAX&#41;](mround-function-dax.md)  
[INT Function &#40;DAX&#41;](int-function-dax.md)  
  
