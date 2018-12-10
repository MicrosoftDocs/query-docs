---
title: "ISEVEN function (DAX) | Microsoft Docs"
ms.service: powerbi 
ms.date: 12/10/2018
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# ISEVEN
Returns TRUE if number is even, or FALSE if number is odd.  
  
## Syntax  
  
```dax
ISEVEN(number)  
```
  
#### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|number|The value to test. If number is not an integer, it is truncated.|  
  
## Return value  
Returns TRUE if number is even, or FALSE if number is odd.  
  
## Remarks  
If number is nonnumeric, ISEVEN returns the #VALUE! error value.  
  
