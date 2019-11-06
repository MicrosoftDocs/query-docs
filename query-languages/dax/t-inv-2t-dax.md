---
title: "T.INV.2T function (DAX) | Microsoft Docs"
ms.service: powerbi 
ms.date: 8/14/2018
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend

---
# T.INV.2T
Returns the two-tailed inverse of the Student's t-distribution.
 
  
## Syntax  
  
```dax
T.INV.2T(Probability,Deg_freedom)
```
  
### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|Probability|The probability associated with the Student's t-distribution.|  
|Deg_freedom|The number of degrees of freedom with which to characterize the distribution.|
  
## Return value  
The two-tailed inverse of the Student's t-distribution. 
  
## Example  
  
```dax
EVALUATE { T.INV.2T(0.546449, 60) }
```

Returns

|[Value]  |
|---------|
|0.606533075825759    |


## See also  

[T.INV function](t-inv-dax.md)   
[T.DIST function](t-dist-dax.md)   
[T.DIST.2T function](t-dist-2t-dax.md)   
[T.DIST.RT function](t-dist-rt-dax.md)   


  
