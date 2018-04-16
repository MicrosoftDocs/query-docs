---
title: "BETA.DIST Function (DAX) | Microsoft Docs"
ms.service: powerbi
ms.date: 4/13/2018
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# BETA.DIST Function (DAX)
Returns the beta distribution. The beta distribution is commonly used to study variation in the percentage of something across samples, such as the fraction of the day people spend watching television.  
  
## Syntax  
  
```  
BETA.DIST(x,alpha,beta,cumulative,[A],[B])  
```  
  
#### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|x|The value between A and B at which to evaluate the function|  
|Alpha|A parameter of the distribution.|  
|Beta|A parameter of the distribution.|  
|A|Optional. A lower bound to the interval of x.|  
|B|Optional. An upper bound to the interval of x.|  
  
## Return Value  
Returns the beta distribution.  
  
## Remarks  
If any argument is nonnumeric, BETA.DIST returns the #VALUE! error value. 

If any argument is not an integer, it is rounded. 
  
If alpha ≤ 0 or beta ≤ 0, BETA.DIST returns the #NUM! error value.  
  
If x &lt; A, x &gt; B, or A = B, BETA.DIST returns the #NUM! error value.  
  
If you omit values for A and B, BETA.DIST uses the standard cumulative beta distribution, so that A = 0 and B = 1.  
  
