---
title: "NORM.DIST Function (DAX) | Microsoft Docs"
ms.prod: dax
ms.date: 8/14/2018
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# NORM.DIST Function
Returns the normal distribution for the specified mean and standard deviation. 
 
  
## Syntax  
  
```  
NORM.DIST(X, Mean, Standard_dev, Cumulative)  
```  
  
#### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|**X**|The value for which you want the distribution.|  
|**Mean** |The arithmetic mean of the distribution.|
|**Standard_dev**|The standard deviation of the distribution.|
|**Cumulative**|A logical value that determines the form of the function. If cumulative is TRUE, NORM.DIST returns the cumulative distribution function; if FALSE, it returns the probability mass function.|
  
## Return Value  
The normal distribution for the specified mean and standard deviation.  
  
## Example  
  
```  
EVALUATE { NORM.DIST(42, 40, 1.5, TRUE) }
```  
Returns

|[Value]  |
|---------|
|0.908788780274132     |


## See Also  

[NORM.S.DIST Function](norm-s-dist-dax.md)   
[NORM.INV Function](norm-inv-dax.md)   
[NORM.S.INV](norm-s-inv-dax.md)   
  
