---
title: "T.DIST.2T Function (DAX) | Microsoft Docs"
ms.prod: dax
ms.date: 8/14/2018
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# T.DIST.2T Function
Returns the two-tailed Student's t-distribution.
 
  
## Syntax  
  
```  
T.DIST.2T(X,Deg_freedom)
```  
  
#### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|**X**|The numeric value at which to evaluate the distribution.|  
|**Deg_freedom** |An integer indicating the number of degrees of freedom.|
  
## Return Value  
Returns the two-tailed Student's t-distribution.
  
## Example  
  
```  
EVALUATE { T.DIST.2T(1.959999998, 60) }
```  
Returns

|[Value]  |
|---------|
|0.054644929975921     |


## See Also  

[T.DIST Function](t-dist-dax.md)   
[T.DIST.RT Function](t-dist-rt-dax.md)   
[T.INV Function](t-inv-dax.md)   
[T.INV.2t Function](t-inv-2t-dax.md)   
  
