---
title: "T.DIST.2T function (DAX) | Microsoft Docs"
ms.service: powerbi 
ms.date: 8/14/2018
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
  
## Example  
  
```dax
EVALUATE { T.DIST.2T(1.959999998, 60) }
```

Returns

|[Value]  |
|---------|
|0.054644929975921     |


## See also  

[T.DIST function](t-dist-dax.md)   
[T.DIST.RT function](t-dist-rt-dax.md)   
[T.INV function](t-inv-dax.md)   
[T.INV.2t function](t-inv-2t-dax.md)   
  
