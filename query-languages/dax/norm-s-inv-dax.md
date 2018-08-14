---
title: "NORM.S.INV Function (DAX) | Microsoft Docs"
ms.prod: dax
ms.date: 8/14/2018
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# NORM.S.INV Function
Returns the inverse of the standard normal cumulative distribution. The distribution has a mean of zero and a standard deviation of one.
 
  
## Syntax  
  
```  
NORM.S.INV(Probability)
```  
  
#### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|**Probability**|A probability corresponding to the normal distribution.|  
  
## Return Value  
The inverse of the standard normal cumulative distribution. The distribution has a mean of zero and a standard deviation of one.
  
## Example  
  
```  
EVALUATE { NORM.S.INV(0.908789) }
```  
Returns

|[Value]  |
|---------|
|1.33333467304411    |


## See Also  

[NORM.INV](norm-inv-dax.md)   
[NORM.S.DIST Function](norm-s-dist-dax.md)   
[NORM.DIST Function](norm-dist-dax.md)   

  
