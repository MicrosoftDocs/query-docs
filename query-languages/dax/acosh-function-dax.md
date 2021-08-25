---
description: "Learn more about: ACOSH"
title: "ACOSH function (DAX) | Microsoft Docs"
ms.service: powerbi 
ms.date: 07/05/2020
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend 
recommendations: false

---
# ACOSH

Returns the inverse hyperbolic cosine of a number. The number must be greater than or equal to 1. The inverse hyperbolic cosine is the value whose hyperbolic cosine is *number*, so ACOSH(COSH(number)) equals number.  
  
## Syntax  
  
```dax
ACOSH(number)  
```
  
### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|number|Any real number equal to or greater than 1.|  
  
## Return value

Returns the inverse hyperbolic cosine of a number.  

## Remarks

[!INCLUDE [function-not-supported-in-directquery-mode](includes/function-not-supported-in-directquery-mode.md)]
  
## Example  
  
|Formula|Description|Result|  
|-----------|---------------|----------|  
|= ACOSH(1)|Inverse hyperbolic cosine of 1.|0|  
|= ACOSH(10)|Inverse hyperbolic cosine of 10.|2.993228|  
  
