---
description: "Learn more about: ISODD"
title: "ISODD function (DAX) | Microsoft Docs"
ms.service: powerbi 
ms.date: 07/08/2020
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend 
recommendations: false

---
# ISODD

Returns TRUE if number is odd, or FALSE if number is even.  
  
## Syntax  
  
```dax
ISODD(number)  
```
  
### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|number|The value to test. If number is not an integer, it is truncated.|  
  
## Return value

Returns TRUE if number is odd, or FALSE if number is even.  
  
## Remarks

- If number is nonnumeric, ISODD returns the #VALUE! error value.  

- [!INCLUDE [function-not-supported-in-directquery-mode](includes/function-not-supported-in-directquery-mode.md)]
