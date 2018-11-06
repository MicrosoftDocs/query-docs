---
title: "ISODD Function (DAX) | Microsoft Docs"
ms.service: powerbi 

ms.date: 11/07/2018
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# ISODD Function (DAX)
Returns TRUE if number is odd, or FALSE if number is even.  
  
## Syntax  
  
```dax
ISODD(number)  
```
  
#### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|number|The value to test. If number is not an integer, it is truncated.|  
  
## Return Value  
Returns TRUE if number is odd, or FALSE if number is even.  
  
## Remarks  
If number is nonnumeric, ISODD returns the #VALUE! error value.  
  
