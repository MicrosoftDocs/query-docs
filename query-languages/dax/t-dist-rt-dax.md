---
title: "T.DIST.RT Function (DAX) | Microsoft Docs"
ms.service: powerbi 

ms.date: 8/14/2018
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# T.DIST.RT Function
Returns the right-tailed Student's t-distribution.
 
  
## Syntax  
  
```dax
T.DIST.RT(X,Deg_freedom)
```
  
#### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|X|The numeric value at which to evaluate the distribution.|  
|Deg_freedom |An integer indicating the number of degrees of freedom.|
  
## Return value  
The right-tailed Student's t-distribution.
  
## Example  
  
```dax
EVALUATE { T.DIST.RT(1.959999998, 60) }
```

Returns

|[Value]  |
|---------|
|0.0273224649879605     |


## See Also  

[T.DIST Function](t-dist-dax.md)   
[T.DIST.2T Function](t-dist-2t-dax.md)   
[T.INV Function](t-inv-dax.md)   
[T.INV.2t Function](t-inv-2t-dax.md)   
  
