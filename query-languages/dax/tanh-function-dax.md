---
title: "TANH function (DAX) | Microsoft Docs"
ms.service: powerbi 
ms.date: 08/04/2020
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend

---
# TANH

Returns the hyperbolic tangent of a number.  
  
## Syntax  
  
```dax
TANH(number)  
```
  
### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|number|Required. Any real number.|  
  
## Return value

Returns the hyperbolic tangent of a number.  
  
## Remarks

- The formula for the hyperbolic tangent is:  
  
  ![Formula](media/dax-tanh-formula.png)  

- [!INCLUDE [function-not-supported-in-directquery-mode](includes/function-not-supported-in-directquery-mode.md)]

## Example  
  
|Formula|Description|Result|  
|-----------|---------------|----------|  
|= TANH(-2)|Hyperbolic tangent of -2 (-0.96403)|-0.964028|  
|= TANH(0)|Hyperbolic tangent of 0 (0)|0|  
|= TANH(0.5)|Hyperbolic tangent of 0.5 (0.462117)|0.462117|  
