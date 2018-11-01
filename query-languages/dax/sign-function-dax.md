---
title: "SIGN Function (DAX) | Microsoft Docs"
ms.service: powerbi 

ms.date: 5/22/2018
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# SIGN Function (DAX)
Determines the sign of a number, the result of a calculation, or a value in a column. The function returns 1 if the number is positive, 0 (zero) if the number is zero, or -1 if the number is negative.  
  
## Syntax  
  
```dax
SIGN(<number>)  
```
  
#### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|**number**|Any real number, a column that contains numbers, or an expression that evaluates to a number.|  
  
## Return Value  
A whole number. The possible return values are 1, 0, and -1.  
  
|Return Value|Description|  
|----------------|---------------|  
|1|The number is positive|  
|0|The number is zero|  
|-1|The number is negative|  
  
## Example  
The following formula returns the sign of the result of the expression that calculates sale price minus cost.  
  
```dax
=SIGN( ([Sale Price] - [Cost]) )  
```
  
## See Also  
[Math and Trig Functions &#40;DAX&#41;](math-and-trig-functions-dax.md)  
  
