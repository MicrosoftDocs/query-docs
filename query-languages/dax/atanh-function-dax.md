---
title: "ATANH function (DAX) | Microsoft Docs"
ms.service: powerbi 
ms.date: 03/25/2020
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend

---
# ATANH

Returns the inverse hyperbolic tangent of a number. Number must be between -1 and 1 (excluding -1 and 1). The inverse hyperbolic tangent is the value whose hyperbolic tangent is *number*, so ATANH(TANH(number)) equals *number*.  
  
## Syntax  
  
```dax
ATANH(number)  
```
  
### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|number|Any real number between 1 and -1.|  
  
## Return value

Returns the inverse hyperbolic tangent of a number.  
  
## Example  
  
|Formula|Description|Result|  
|-----------|---------------|----------|  
|=ATANH(0.76159416)|Inverse hyperbolic tangent of 0.76159416|1.00000001|  
|=ATANH(-0.1)||-0.100335348|  
||||  
  
## See also

[ATAN function &#40;DAX&#41;](atan-function-dax.md)  
  
