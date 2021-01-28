---
description: "Learn more about: T.DIST.2T"
title: "T.DIST.2T function (DAX) | Microsoft Docs"
ms.service: powerbi 
ms.date: 07/10/2020
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend

---
# T.DIST.2T

Returns the two-tailed Student's t-distribution.
  
## Syntax  
  
```dax
T.DIST.2T(X,Deg_freedom)
```
  
### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|X|The numeric value at which to evaluate the distribution.|  
|Deg_freedom |An integer indicating the number of degrees of freedom.|
  
## Return value

The two-tailed Student's t-distribution.

## Remarks

[!INCLUDE [function-not-supported-in-directquery-mode](includes/function-not-supported-in-directquery-mode.md)]

## Example  
  
```dax
EVALUATE { T.DIST.2T(1.959999998, 60) }
```

Returns

|[Value]  |
|---------|
|0.054644929975921     |

## See also  

[T.DIST](t-dist-dax.md)  
[T.DIST.RT](t-dist-rt-dax.md)  
[T.INV](t-inv-dax.md)  
[T.INV.2t](t-inv-2t-dax.md)  
  
