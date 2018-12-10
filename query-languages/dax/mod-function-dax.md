---
title: "MOD function (DAX) | Microsoft Docs"
ms.service: powerbi 
ms.date: 12/10/2018
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# MOD
Returns the remainder after a number is divided by a divisor. The result always has the same sign as the divisor.  
  
## Syntax  
  
```dax
MOD(<number>, <divisor>)  
```
  
#### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|number|The number for which you want to find the remainder after the division is performed.|  
|divisor|The number by which you want to divide.|  
  
## Return value  
A whole number.  
  
## Remarks  
If the divisor is 0 (zero), MOD returns an error. You cannot divide by 0.  
  
The MOD function can be expressed in terms of the INT function: MOD(n, d) = n - d*INT(n/d)  
  
## Example  
The following formula returns 1, the remainder of 3 divided by 2.  
  
```dax
=MOD(3,2)  
```
  
## Example  
The following formula returns -1, the remainder of 3 divided by 2. Note that the sign is always the same as the sign of the divisor.  
  
```dax
=MOD(-3,-2)  
```
  
## See also  
[Math and Trig functions &#40;DAX&#41;](math-and-trig-functions-dax.md)  
[ROUND function &#40;DAX&#41;](round-function-dax.md)  
[ROUNDUP function &#40;DAX&#41;](roundup-function-dax.md)  
[ROUNDDOWN function &#40;DAX&#41;](rounddown-function-dax.md)  
[MROUND function &#40;DAX&#41;](mround-function-dax.md)  
[INT function &#40;DAX&#41;](int-function-dax.md)  
  
