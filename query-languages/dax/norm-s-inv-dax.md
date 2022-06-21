---
description: "Learn more about: NORM.S.INV"
title: "NORM.S.INV function (DAX) | Microsoft Docs"
ms.service: powerbi 
ms.subservice: dax 
ms.date: 07/08/2020
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend 
recommendations: false

---
# NORM.S.INV

Returns the inverse of the standard normal cumulative distribution. The distribution has a mean of zero and a standard deviation of one.

## Syntax  
  
```dax
NORM.S.INV(Probability)
```
  
### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|Probability|A probability corresponding to the normal distribution.|  
  
## Return value

The inverse of the standard normal cumulative distribution. The distribution has a mean of zero and a standard deviation of one.
  
## Remarks

[!INCLUDE [function-not-supported-in-directquery-mode](includes/function-not-supported-in-directquery-mode.md)]

## Example  
  
```dax
EVALUATE { NORM.S.INV(0.908789) }
```

Returns

|[Value]  |
|---------|
|1.33333467304411    |

## See also  

[NORM.INV](norm-inv-dax.md)  
[NORM.S.DIST function](norm-s-dist-dax.md)  
[NORM.DIST function](norm-dist-dax.md)  
