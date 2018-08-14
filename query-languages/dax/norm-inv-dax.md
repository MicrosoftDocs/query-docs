---
title: "NORM.INV Function (DAX) | Microsoft Docs"
ms.prod: dax
ms.date: 8/14/2018
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# NORM.INV Function
The inverse of the normal cumulative distribution for the specified mean and standard deviation.
 
  
## Syntax  
  
```  
NORM.INV(Probability, Mean, Standard_dev)
```  
  
#### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|**Probability**|A probability corresponding to the normal distribution.|  
|**Mean**|The arithmetic mean of the distribution.|
|**Standard_dev**|The standard deviation of the distribution.|
  
## Return Value  
Returns the inverse of the normal cumulative distribution for the specified mean and standard deviation.    
  
## Example  
  
```  
EVALUATE { NORM.INV(0.908789, 40, 1.5) }
```  
Returns

|[Value]  |
|---------|
|42.00000200956628780274132    |


## See Also  

[NORM.S.INV](norm-s-inv-dax.md)   
[NORM.S.DIST Function](norm-s-dist-dax.md)   
[NORM.DIST Function](norm-dist-dax.md)   

  
