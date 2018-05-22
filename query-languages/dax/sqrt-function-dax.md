---
title: "SQRT Function (DAX) | Microsoft Docs"
ms.prod: dax
ms.date: 5/22/2018
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# SQRT Function (DAX)
Returns the square root of a number.  
  
## Syntax  
  
```  
SQRT(<number>)  
```  
  
#### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|**number**|The number for which you want the square root, a column that contains numbers, or an expression that evaluates to a number.|  
  
## Return Value  
A decimal number.  
  
## Remarks  
If the number is negative, the SQRT function returns an error.  
  
## Example  
The following formula returns 5.  
  
```  
=SQRT(25)  
```  
  
## See Also  
[Math and Trig Functions &#40;DAX&#41;](math-and-trig-functions-dax.md)  
  
