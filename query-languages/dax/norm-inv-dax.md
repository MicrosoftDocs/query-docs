---
title: "NORM.INV function (DAX) | Microsoft Docs"
ms.service: powerbi 
ms.date: 8/14/2018
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend

---
# NORM.INV
The inverse of the normal cumulative distribution for the specified mean and standard deviation.
 
  
## Syntax  
  
```dax
NORM.INV(Probability, Mean, Standard_dev)
```
  
### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|Probability|A probability corresponding to the normal distribution.|  
|Mean|The arithmetic mean of the distribution.|
|Standard_dev|The standard deviation of the distribution.|
  
## Return value  
Returns the inverse of the normal cumulative distribution for the specified mean and standard deviation.    
  
## Example  
  
```dax
EVALUATE { NORM.INV(0.908789, 40, 1.5) }
```

Returns

|[Value]  |
|---------|
|42.00000200956628780274132    |


## See also  

[NORM.S.INV](norm-s-inv-dax.md)   
[NORM.S.DIST function](norm-s-dist-dax.md)   
[NORM.DIST function](norm-dist-dax.md)   

  
