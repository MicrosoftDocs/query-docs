---
title: "T.INV function (DAX) | Microsoft Docs"
ms.service: powerbi 

ms.date: 8/14/2018
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# T.INV function
Returns the left-tailed inverse of the Student's t-distribution.
 
  
## Syntax  
  
```dax
T.INV(Probability,Deg_freedom)
```
  
#### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|Probability|The probability associated with the Student's t-distribution.|  
|Deg_freedom|The number of degrees of freedom with which to characterize the distribution.|
  
## Return value  
The left-tailed inverse of the Student's t-distribution. 
  
## Example  
  
```dax
EVALUATE { T.INV(0.75, 2) }
```

Returns

|[Value]  |
|---------|
|0.816496580927726   |


## See also  

[T.INV.2T function](t-inv-2t-dax.md)   
[T.DIST function](t-dist-dax.md)   
[T.DIST.2T function](t-dist-2t-dax.md)   
[T.DIST.RT function](t-dist-rt-dax.md)   


  
