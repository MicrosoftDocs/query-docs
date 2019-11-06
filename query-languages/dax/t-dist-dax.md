---
title: "T.DIST function (DAX) | Microsoft Docs"
ms.service: powerbi 
ms.date: 8/14/2018
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend

---
# T.DIST
Returns the Student's left-tailed t-distribution.
 
  
## Syntax  
  
```dax
T.DIST(X,Deg_freedom,Cumulative)
```
  
### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|X|The numeric value at which to evaluate the distribution.|  
|Deg_freedom |An integer indicating the number of degrees of freedom.|
|Cumulative|A logical value that determines the form of the function. If cumulative is TRUE, T.DIST returns the cumulative distribution function; if FALSE, it returns the probability density function.|
  
## Return value  
The Student's left-tailed t-distribution. 
  
## Example  
  
```dax
EVALUATE { T.DIST(60, 1, TRUE) } 
```

Returns

|[Value]  |
|---------|
|0.994695326367377     |


## See also  

[T.DIST.2T function](t-dist-2t-dax.md)   
[T.DIST.RT function](t-dist-rt-dax.md)   
[T.INV function](t-inv-dax.md)   
[T.INV.2t function](t-inv-2t-dax.md)   
  
