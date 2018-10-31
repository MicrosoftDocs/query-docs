---
title: "T.INV.2T Function (DAX) | Microsoft Docs"
ms.prod: powerbi 
ms.technology: dax
ms.date: 8/14/2018
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# T.INV.2T Function
Returns the two-tailed inverse of the Student's t-distribution.
 
  
## Syntax  
  
```dax
T.INV.2T(Probability,Deg_freedom)
```
  
#### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|**Probability**|The probability associated with the Student's t-distribution.|  
|**Deg_freedom** |The number of degrees of freedom with which to characterize the distribution.|
  
## Return Value  
The two-tailed inverse of the Student's t-distribution. 
  
## Example  
  
```dax
EVALUATE { T.INV.2T(0.546449, 60) }
```dax
Returns

|[Value]  |
|---------|
|0.606533075825759    |


## See Also  

[T.INV Function](t-inv-dax.md)   
[T.DIST Function](t-dist-dax.md)   
[T.DIST.2T Function](t-dist-2t-dax.md)   
[T.DIST.RT Function](t-dist-rt-dax.md)   


  
