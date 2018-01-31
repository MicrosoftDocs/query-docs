---
title: "CHISQ.INV Function (DAX) | Microsoft Docs"
ms.custom: ""
ms.date: "12/28/2017"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "analysis-services"
  - "daxlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: c03e389b-7e0b-4550-99f8-a177dc7c9378
caps.latest.revision: 5
author: "Minewiskan"
ms.author: "owend"
manager: "kfile"
---
# CHISQ.INV Function (DAX)
Returns the inverse of the left-tailed probability of the chi-squared distribution.  
  
The chi-squared distribution is commonly used to study variation in the percentage of something across samples, such as the fraction of the day people spend watching television.  
  
## Syntax  
  
```  
CHISQ.INV(probability,deg_freedom)  
```  
  
#### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|Probability|A probability associated with the chi-squared distribution.|  
|Deg_freedom|The number of degrees of freedom.|  
  
## Return Value  
Returns the inverse of the left-tailed probability of the chi-squared distribution.  
  
## Remarks  
If argument is nonnumeric, CHISQ.INV returns the #VALUE! error value.  
  
If probability &amp;lt; 0 or probability &amp;gt; 1, CHISQ.INV returns the #NUM! error value.  
  
If deg_freedom is not an integer, it is rounded.  
  
If deg_freedom &amp;lt; 1 or deg_freedom &amp;gt; 10^10, CHISQ.INV returns the #NUM! error value.  
  
## Example  
  
|Formula|Description|Result|  
|-----------|---------------|----------|  
|=CHISQ.INV(0.93,1)|Inverse of the left-tailed probability of the chi-squared distribution for 0.93, using 1 degree of freedom.|5.318520074|  
|=CHISQ.INV(0.6,2)|Inverse of the left-tailed probability of the chi-squared distribution for 0.6, using 2 degrees of freedom.|1.832581464|  
  
