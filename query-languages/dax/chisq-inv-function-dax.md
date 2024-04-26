---
description: "Learn more about: CHISQ.INV"
title: "CHISQ.INV function (DAX) | Microsoft Docs"
---
# CHISQ.INV

[!INCLUDE[applies-to-measures-columns-tables-visual-calculations](includes/applies-to-measures-columns-tables-visual-calculations.md)]

Returns the inverse of the left-tailed probability of the chi-squared distribution.  
  
The chi-squared distribution is commonly used to study variation in the percentage of something across samples, such as the fraction of the day people spend watching television.  
  
## Syntax  
  
```dax
CHISQ.INV(probability,deg_freedom)  
```
  
### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|Probability|A probability associated with the chi-squared distribution.|  
|Deg_freedom|The number of degrees of freedom.|  
  
## Return value

Returns the inverse of the left-tailed probability of the chi-squared distribution.  
  
## Remarks

- If argument is nonnumeric, CHISQ.INV returns the #VALUE! error value.  
  
- If probability \< 0 or probability > 1, CHISQ.INV returns the #NUM! error value.  
  
- If deg_freedom is not an integer, it is rounded.  
  
- If deg_freedom \< 0 or deg_freedom > 10^10, CHISQ.INV returns the #NUM! error value.  

- [!INCLUDE [function-not-supported-in-directquery-mode](includes/function-not-supported-in-directquery-mode.md)]

## Example  
  
|Formula|Description|Result|  
|-----------|---------------|----------|  
|= CHISQ.INV(0.93,1)|Inverse of the left-tailed probability of the chi-squared distribution for 0.93, using 1 degree of freedom.|5.318520074|  
|= CHISQ.INV(0.6,2)|Inverse of the left-tailed probability of the chi-squared distribution for 0.6, using 2 degrees of freedom.|1.832581464|  
