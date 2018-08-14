---
title: "NORM.S.DIST Function (DAX) | Microsoft Docs"
ms.prod: dax
ms.date: 8/14/2018
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# NORM.S.DIST Function
Returns the standard normal distribution (has a mean of zero and a standard deviation of one).
 
  
## Syntax  
  
```  
NORM.S.DIST(Z, Cumulative)
```  
  
#### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|**Z**|The value for which you want the distribution.|  
|**Cumulative**|Cumulative is a logical value that determines the form of the function. If cumulative is TRUE, NORM.S.DIST returns the cumulative distribution function; if FALSE, it returns the probability mass function.|
  
## Return Value  
Returns the standard normal distribution (has a mean of zero and a standard deviation of one).   
  
## Example  
  
```  
EVALUATE { NORM.S.DIST(1.333333, TRUE) }
```  
Returns

|[Value]  |
|---------|
|0.908788725604095    |


## See Also  

[NORM.INV Function](norm-inv-dax.md)  
[NORM.DIST Function](norm-dist-dax.md)
[NORM.S.INV](norm-s-inv-dax.md)   
  
