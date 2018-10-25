---
title: "T.DIST Function (DAX) | Microsoft Docs"
ms.prod: dax
ms.date: 8/14/2018
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# T.DIST Function
Returns the Student's left-tailed t-distribution.
 
  
## Syntax  
  
```dax
T.DIST(X,Deg_freedom,Cumulative)
```
  
#### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|**X**|The numeric value at which to evaluate the distribution.|  
|**Deg_freedom** |An integer indicating the number of degrees of freedom.|
|**Cumulative**|A logical value that determines the form of the function. If cumulative is TRUE, T.DIST returns the cumulative distribution function; if FALSE, it returns the probability density function.|
  
## Return Value  
The Student's left-tailed t-distribution. 
  
## Example  
  
```dax
EVALUATE { T.DIST(60, 1, TRUE) } 
```dax
Returns

|[Value]  |
|---------|
|0.994695326367377     |


## See Also  

[T.DIST.2T Function](t-dist-2t-dax.md)   
[T.DIST.RT Function](t-dist-rt-dax.md)   
[T.INV Function](t-inv-dax.md)   
[T.INV.2t Function](t-inv-2t-dax.md)   
  
