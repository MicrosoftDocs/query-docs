---
title: "ACOSH Function (DAX) | Microsoft Docs"
ms.prod: powerbi 
ms.technology: dax
ms.date: 5/22/2018
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# ACOSH Function (DAX)
Returns the inverse hyperbolic cosine of a number. The number must be greater than or equal to 1. The inverse hyperbolic cosine is the value whose hyperbolic cosine is *number*, so ACOSH(COSH(number)) equals number.  
  
## Syntax  
  
```dax
ACOSH(number)  
```
  
#### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|number|Any real number equal to or greater than 1.|  
  
## Return Value  
Returns the inverse hyperbolic cosine of a number.  
  
## Example  
  
|Formula|Description|Result|  
|-----------|---------------|----------|  
|=ACOSH(1)|Inverse hyperbolic cosine of 1.|0|  
|=ACOSH(10)|Inverse hyperbolic cosine of 10.|2.993228|  
  
