---
title: "T.INV Function (DAX) | Microsoft Docs"
ms.prod: powerbi 
ms.technology: dax
ms.date: 8/14/2018
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# T.INV Function
Returns the left-tailed inverse of the Student's t-distribution.
 
  
## Syntax  
  
```dax
T.INV(Probability,Deg_freedom)
```
  
#### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|**Probability**|The probability associated with the Student's t-distribution.|  
|**Deg_freedom** |The number of degrees of freedom with which to characterize the distribution.|
  
## Return Value  
The left-tailed inverse of the Student's t-distribution. 
  
## Example  
  
```dax
EVALUATE { T.INV(0.75, 2) }
```dax
Returns

|[Value]  |
|---------|
|0.816496580927726   |


## See Also  

[T.INV.2T Function](t-inv-2t-dax.md)   
[T.DIST Function](t-dist-dax.md)   
[T.DIST.2T Function](t-dist-2t-dax.md)   
[T.DIST.RT Function](t-dist-rt-dax.md)   


  
