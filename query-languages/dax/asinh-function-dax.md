---
description: "Learn more about: ASINH"
title: "ASINH function (DAX) | Microsoft Docs"
ms.service: powerbi 
ms.date: 07/05/2020
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend

---
# ASINH

Returns the inverse hyperbolic sine of a number. The inverse hyperbolic sine is the value whose hyperbolic sine is *number*, so ASINH(SINH(number)) equals *number*.  
  
## Syntax  
  
```dax
ASINH(number)  
```
  
### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|number|Any real number.|  
  
## Return value

Returns the inverse hyperbolic sine of a number.  

## Remarks

[!INCLUDE [function-not-supported-in-directquery-mode](includes/function-not-supported-in-directquery-mode.md)]

## Example  
  
|Formula|Description|Result|  
|-----------|---------------|----------|  
|= ASINH(-2.5)|Inverse hyperbolic sine of -2.5|-1.647231146|  
|= ASINH(10)|Inverse hyperbolic sine of 10|2.99822295|  
