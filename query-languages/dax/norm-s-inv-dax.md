---
title: "NORM.S.INV function (DAX) | Microsoft Docs"
ms.service: powerbi 
ms.date: 8/14/2018
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend

---
# NORM.S.INV
Returns the inverse of the standard normal cumulative distribution. The distribution has a mean of zero and a standard deviation of one.
 
  
## Syntax  
  
```dax
NORM.S.INV(Probability)
```
  
### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|Probability|A probability corresponding to the normal distribution.|  
  
## Return value  
The inverse of the standard normal cumulative distribution. The distribution has a mean of zero and a standard deviation of one.
  
## Example  
  
```dax
EVALUATE { NORM.S.INV(0.908789) }
```

Returns

|[Value]  |
|---------|
|1.33333467304411    |


## See also  

[NORM.INV](norm-inv-dax.md)   
[NORM.S.DIST function](norm-s-dist-dax.md)   
[NORM.DIST function](norm-dist-dax.md)   

  
