---
title: "FACT Function (DAX) | Microsoft Docs"
ms.service: powerbi 

ms.date: 11/07/2018
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# FACT Function (DAX)
Returns the factorial of a number, equal to the series 1*2\*3\*...\* , ending in the given number.  
  
## Syntax  
  
```dax
FACT(<number>)  
```
  
#### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|number|The non-negative number for which you want to calculate the factorial.|  
  
## Return value  
A decimal number.  
  
## Remarks  
If the number is not an integer, it is truncated and an error is returned. If the result is too large, an error is returned.  
  
## Example  
The following formula returns the factorial for the series of integers in the column, `[Values]`.  
  
```dax
=FACT([Values])  
```

The following table shows the expected results:  
  
|Values|Results|  
|----------|-----------|  
|0|1|  
|1|1|  
|2|2|  
|3|6|  
|4|24|  
|5|120|  
|170|7.257415615308E+306|  
  
## See Also  
[Math and Trig Functions &#40;DAX&#41;](math-and-trig-functions-dax.md)  
[TRUNC Function &#40;DAX&#41;](trunc-function-dax.md)  
  
