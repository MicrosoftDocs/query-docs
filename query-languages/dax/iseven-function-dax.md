---
description: "Learn more about: ISEVEN"
title: "ISEVEN function (DAX) | Microsoft Docs"
ms.service: powerbi 
ms.date: 07/08/2020
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend 
recommendations: false

---
# ISEVEN

Returns TRUE if number is even, or FALSE if number is odd.  
  
## Syntax  
  
```dax
ISEVEN(number)  
```
  
### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|number|The value to test. If number is not an integer, it is truncated.|  
  
## Return value

Returns TRUE if number is even, or FALSE if number is odd.  
  
## Remarks

- If number is nonnumeric, ISEVEN returns the #VALUE! error value.  

- [!INCLUDE [function-not-supported-in-directquery-mode](includes/function-not-supported-in-directquery-mode.md)]
